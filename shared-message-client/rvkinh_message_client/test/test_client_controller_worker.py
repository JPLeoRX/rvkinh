from rvkinh_message_protocol import Worker
from rvkinh_message_client.client_controller import ClientController

c = ClientController()
base_url = 'http://142.93.38.82:8888'
api_key = 'SC9J867CZp'
worker = Worker('cluster-test', 'worker-test')
print('ping():', c.ping(base_url))
print('worker_alive():', c.worker_alive(base_url, api_key, worker))
print('worker_goal_akio():', c.worker_goal_akio(base_url, api_key, worker))
print('worker_goal_haru():', c.worker_goal_haru(base_url, api_key, worker))
