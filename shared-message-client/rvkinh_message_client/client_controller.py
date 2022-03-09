from typing import List
import requests
from pydantic import parse_obj_as
from injectable import injectable
from rvkinh_message_protocol import Worker, GoalHaru, GoalAkio, AttackOrchestration


@injectable
class ClientController:
    def ping(self, base_url: str, timeout_in_seconds: int = 10) -> bool:
        url = base_url + "/ping"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def worker_alive(self, base_url: str, api_key: str, worker: Worker, timeout_in_seconds: int = 10) -> bool:
        url = base_url + "/worker/alive"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.post(url, data=worker.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def worker_goal_haru(self, base_url: str, api_key: str, worker: Worker, timeout_in_seconds: int = 10) -> GoalHaru:
        url = base_url + "/worker/goal/haru"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.post(url, data=worker.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return GoalHaru.parse_obj(response_json)

    def worker_goal_akio(self, base_url: str, api_key: str, worker: Worker, timeout_in_seconds: int = 10) -> GoalAkio:
        url = base_url + "/worker/goal/akio"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.post(url, data=worker.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return GoalAkio.parse_obj(response_json)

    def attack_orchestration_start(self, base_url: str, api_key: str, attack_orchestration: AttackOrchestration, timeout_in_seconds: int = 10) -> bool:
        url = base_url + "/attack/orchestration/start"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.post(url, data=attack_orchestration.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def attack_orchestration_stop(self, base_url: str, api_key: str, timeout_in_seconds: int = 10) -> bool:
        url = base_url + "/attack/orchestration/stop"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def attack_orchestration_status(self, base_url: str, api_key: str, timeout_in_seconds: int = 10) -> AttackOrchestration:
        url = base_url + "/attack/orchestration/status"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return AttackOrchestration.parse_obj(response_json)

    def system_workers_alive(self, base_url: str, api_key: str, timeout_in_seconds: int = 10) -> List[Worker]:
        url = base_url + "/system/workers_alive"
        headers = {'Content-Type': 'application/json', 'Api-Key': api_key}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(List[Worker], response_json)
