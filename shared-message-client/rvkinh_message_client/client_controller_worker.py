import requests
from pydantic import parse_obj_as
from injectable import injectable
from rvkinh_message_protocol import Worker


@injectable
class ClientControllerWorker:
    def worker_alive(self, base_url: str, worker: Worker, timeout_in_seconds: int = 10):
        url = base_url + "/worker/alive"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=worker.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)
