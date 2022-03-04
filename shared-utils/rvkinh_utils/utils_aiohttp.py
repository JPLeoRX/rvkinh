import asyncio
import json
import time
import traceback
from typing import Dict, Any, List, Tuple
import aiohttp.client_exceptions
from aiohttp import ClientSession
from rvkinh_message_protocol import HttpResponse, HttpParallelResponse
from injectable import injectable


HTTP_STATUS_CODE_SUCCESS = 200
HTTP_STATUS_CODE_UNAUTHORIZED = 401
HTTP_STATUS_CODE_FORBIDDEN = 403
HTTP_STATUS_CODE_NOT_FOUND = 404
HTTP_STATUS_CODE_METHOD_NOT_ALLOWED = 405
HTTP_STATUS_CODE_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_STATUS_CODE_TOO_MANY_REQUESTS = 429
HTTP_STATUS_CODE_INTERNAL_SERVER_ERROR = 500
HTTP_STATUS_CODE_BAD_GATEWAY = 502
HTTP_STATUS_CODE_SERVICE_UNAVAILABLE = 503
HTTP_STATUS_CODE_EXCEPTION_TIMEOUT = -1000
HTTP_STATUS_CODE_EXCEPTION_PROXY_ERROR = -2000
HTTP_STATUS_CODE_EXCEPTION_CONNECTION_ERROR = -3000
HTTP_STATUS_CODE_EXCEPTION_SERVER_DISCONNECTED_ERROR = -4000
HTTP_STATUS_CODE_EXCEPTION_CLIENT_OS_ERROR = -5000
HTTP_STATUS_CODE_EXCEPTION_CLIENT_RESPONSE_ERROR = -6000


@injectable
class UtilsAiohttp:
    async def http_get_with_aiohttp(self, session: ClientSession, url: str, headers: Dict = {}, proxy: str = None, timeout: int = 10, ignore_json: bool = False, ignore_body: bool = False) -> HttpResponse:
        # Make request
        try:
            response = await session.get(url=url, headers=headers, proxy=proxy, timeout=timeout)
        except asyncio.exceptions.TimeoutError as e1:
            return HttpResponse(HTTP_STATUS_CODE_EXCEPTION_TIMEOUT, None, None)
        except aiohttp.client_exceptions.ClientHttpProxyError as e2:
            return HttpResponse(HTTP_STATUS_CODE_EXCEPTION_PROXY_ERROR, None, None)
        except aiohttp.client_exceptions.ClientConnectorError as e3:
            return HttpResponse(HTTP_STATUS_CODE_EXCEPTION_CONNECTION_ERROR, None, None)
        except aiohttp.client_exceptions.ServerDisconnectedError as e4:
            return HttpResponse(HTTP_STATUS_CODE_EXCEPTION_SERVER_DISCONNECTED_ERROR, None, None)
        except aiohttp.client_exceptions.ClientOSError as e5:
            return HttpResponse(HTTP_STATUS_CODE_EXCEPTION_CLIENT_OS_ERROR, None, None)
        except aiohttp.client_exceptions.ClientResponseError as e6:
            return HttpResponse(HTTP_STATUS_CODE_EXCEPTION_CLIENT_RESPONSE_ERROR, None, None)
        except Exception as e7:
            print(traceback.format_exc())
            return HttpResponse(0, None, None)

        # Read JSON
        response_json = None
        if not ignore_json:
            try:
                response_json = await response.json(content_type=None)
            except json.decoder.JSONDecodeError as e:
                pass

        # Read BODY
        response_content = None
        if not ignore_body:
            try:
                response_content = await response.read()
            except:
                pass

        return HttpResponse(response.status, response_json, response_content)

    async def http_get_with_aiohttp_parallel(self, session: ClientSession, list_of_urls: List[str], headers: Dict = {}, proxy: str = None, timeout: int = 10, ignore_json: bool = False, ignore_body: bool = False) -> HttpParallelResponse:
        t1 = time.time()
        responses = await asyncio.gather(*[self.http_get_with_aiohttp(session, url, headers, proxy, timeout, ignore_json, ignore_body) for url in list_of_urls])
        t2 = time.time()
        execution_time = t2 - t1
        return HttpParallelResponse(responses, execution_time)

    def debug_stats(self, url: str, responses: List[HttpResponse], t: float):
        print('UtilsAiohttp.debug_stats(): ' + url)
        success_responses = len([r for r in responses if 200 <= r.status_code <= 299])
        redirect_responses = len([r for r in responses if 300 <= r.status_code <= 399])
        client_error_responses = len([r for r in responses if 400 <= r.status_code <= 499])
        not_found_responses = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_NOT_FOUND])
        method_not_allowed_responses = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_METHOD_NOT_ALLOWED])
        server_error_responses = len([r for r in responses if 500 <= r.status_code <= 599])
        proxy_errors = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_EXCEPTION_PROXY_ERROR])
        connection_errors = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_EXCEPTION_CONNECTION_ERROR])
        timeouts = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_EXCEPTION_TIMEOUT])
        server_disconnected_error = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_EXCEPTION_SERVER_DISCONNECTED_ERROR])
        client_os_error = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_EXCEPTION_CLIENT_OS_ERROR])
        client_response_error = len([r for r in responses if r.status_code == HTTP_STATUS_CODE_EXCEPTION_CLIENT_RESPONSE_ERROR])

        print('UtilsAiohttp.debug_stats(): Total responses count: ' + str(len(responses)))
        if success_responses > 0:
            print('UtilsAiohttp.debug_stats(): Success responses: ' + str(success_responses))
        if redirect_responses > 0:
            print('UtilsAiohttp.debug_stats(): Redirect responses: ' + str(redirect_responses))
        if client_error_responses > 0:
            responses_4xx = [r for r in responses if 400 <= r.status_code <= 499]
            codes = set([r.status_code for r in responses_4xx])
            print('UtilsAiohttp.debug_stats(): Client error responses (4XX): ' + str(client_error_responses) + ', codes ' + str(codes))
        if not_found_responses > 0:
            print('UtilsAiohttp.debug_stats(): Not found responses (' + str(HTTP_STATUS_CODE_NOT_FOUND) + '): ' + str(not_found_responses))
        if method_not_allowed_responses > 0:
            print('UtilsAiohttp.debug_stats(): Method not allowed responses (' + str(HTTP_STATUS_CODE_METHOD_NOT_ALLOWED) + '): ' + str(method_not_allowed_responses))
        if server_error_responses > 0:
            print('UtilsAiohttp.debug_stats(): Server error responses (5XX): ' + str(server_error_responses))
        if proxy_errors > 0:
            print('UtilsAiohttp.debug_stats(): Proxy errors (in client): ' + str(proxy_errors))
        if connection_errors > 0:
            print('UtilsAiohttp.debug_stats(): Connections errors (in client): ' + str(connection_errors))
        if timeouts > 0:
            print('UtilsAiohttp.debug_stats(): Timeouts (in client): ' + str(timeouts))
        if server_disconnected_error > 0:
            print('UtilsAiohttp.debug_stats(): Server disconnected (in client): ' + str(server_disconnected_error))
        if client_os_error > 0:
            print('UtilsAiohttp.debug_stats(): Client OS error (in client): ' + str(client_os_error))
        if client_response_error > 0:
            print('UtilsAiohttp.debug_stats(): Client response error (in client): ' + str(client_response_error))

        print('UtilsAiohttp.debug_stats(): Execution time is ' + str(round(t, 2)) + ' s,' + ' speed is ' + str(round(len(responses) / t, 2)) + ' r/s')
        print('UtilsAiohttp.debug_stats(): ')
