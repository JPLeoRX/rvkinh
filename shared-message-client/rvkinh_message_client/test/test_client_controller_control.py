from rvkinh_message_protocol import AttackOrchestration
from rvkinh_message_client.client_controller import ClientController

c = ClientController()
base_url = 'http://142.93.38.82:8888'
api_key = 'c2uXRF7RLR'
print('ping():', c.ping(base_url))
print('system_workers_alive():', c.system_workers_alive(base_url, api_key))
print('attack_orchestration_status():', c.attack_orchestration_start(base_url, api_key, AttackOrchestration({}, {})))
print('attack_orchestration_status():', c.attack_orchestration_status(base_url, api_key))
print('attack_orchestration_stop():', c.attack_orchestration_stop(base_url, api_key))
