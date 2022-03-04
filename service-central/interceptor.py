import json
import time
from injectable import injectable, autowired, Autowired
from fastapi import Request, Response
from rvkinh_proxy_message_protocol import ProxyRequest, ProxyChannel, ProxyErrorResponse, ProxyResponse, RabbitmqConfig
from rvkinh_proxy_utils import UtilsRabbitmq, UtilsId


@injectable
class Interceptor:
    @autowired
    def __init__(self, utils_id: Autowired(UtilsId), utils_rabbitmq: Autowired(UtilsRabbitmq)):
        self.utils_id = utils_id
        self.utils_rabbitmq = utils_rabbitmq

    async def intercept(self, rabbitmq_config: RabbitmqConfig, request: Request, sleep_interval_in_seconds: float = 0.2, receive_timeout_in_seconds: float = 2.0) -> Response:
        # Track IDs
        id = self.utils_id.generate_uuid()
        request_id = 'request-' + id
        response_id = 'response-' + id

        # Get cluster and worker
        request_base_url = str(request.base_url)
        request_url = str(request.url)
        print('intercept(): REQUEST BASE URL = ' + str(request_base_url))
        print('intercept(): REQUEST URL = ' + str(request_url))
        trimmed_path_url = request_url.replace(request_base_url, '')
        print('intercept(): TRIMMED PATH URL = ' + trimmed_path_url)
        trimmed_path_url_parts = trimmed_path_url.split('/')
        print('intercept(): TRIMMED PATH URL PARTS = ' + str(trimmed_path_url_parts))
        if len(trimmed_path_url_parts) < 2:
            error_response = ProxyErrorResponse(id, 'NO_CLUSTER_OR_WORKER_ID', 'The request has invalid url format, please use http://localhost:8888/cluster_id/worker_id/docs format')
            return Response(content=str(error_response.json()), media_type="application/json", status_code=500)
        cluster_id = trimmed_path_url_parts[0]
        worker_id = trimmed_path_url_parts[1]
        print('intercept(): CLUSTER ID = ' + str(cluster_id))
        print('intercept(): WORKER ID = ' + str(worker_id))
        remaining_path_url_parts = trimmed_path_url_parts[2:]
        print('intercept(): REMAINING PATH URL PARTS = ' + str(remaining_path_url_parts))
        forwarded_request_url = request_base_url + '/'.join(remaining_path_url_parts)
        print('intercept(): FORWARDED REQUEST URL = ' + str(forwarded_request_url))

        # Build new request, and send it to rabbit
        proxy_request = await self.build_proxy_request(request, forwarded_request_url)
        self.utils_rabbitmq.send(rabbitmq_config, request_id, str(proxy_request.json()))

        # Build new channel, and send it to rabbit
        proxy_channel = ProxyChannel(id, request_id, response_id)
        rabbit_proxy_channel_name = 'channels|' + cluster_id + '|' + worker_id
        print('intercept(): RABBIT PROXY CHANNEL NAME = ' + str(rabbit_proxy_channel_name))
        self.utils_rabbitmq.send(rabbitmq_config, rabbit_proxy_channel_name, str(proxy_channel.json()))

        # Hold a small pause, to allow client to catch-up and send the response
        time.sleep(sleep_interval_in_seconds)

        # Wait for response
        proxy_response_message = self.utils_rabbitmq.receive(rabbitmq_config, response_id, timeout_in_seconds=receive_timeout_in_seconds)
        if proxy_response_message is None:
            error_response = ProxyErrorResponse(id, 'NO_RESPONSE_FROM_WORKER', 'The worker didn\'t provide any response within given time limit')
            return Response(content=str(error_response.json()), media_type="application/json", status_code=500)
        else:
            proxy_response = ProxyResponse.parse_obj(json.loads(proxy_response_message))
            return Response(content=proxy_response.content, status_code=proxy_response.status_code, headers=proxy_response.headers)

    async def build_proxy_request(self, request: Request, forwarded_request_url: str) -> ProxyRequest:
        return ProxyRequest(
            request.method,
            forwarded_request_url,
            str(request.base_url),
            request.headers,
            request.query_params,
            request.path_params,
            request.cookies,
            await request.body(),
            request.client
        )
