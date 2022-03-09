import time
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsEnv
from rvkinh_message_protocol import Worker
from rvkinh_utils import AbstractJob
from rvkinh_message_client import ClientController



@injectable
class JobControllerNotifyAlive(AbstractJob):
    @autowired
    def __init__(self, client_controller: Autowired(ClientController), utils_env: Autowired(UtilsEnv)):
        super().__init__()
        self.client_controller = client_controller
        self.utils_env = utils_env
        self.utils_env.load_environment_variables(['CLUSTER_ID', 'WORKER_ID', 'CONTROLLER_URL', 'WORKER_API_KEY'])
        self.cluster_id = self.utils_env.get_environment_variable('CLUSTER_ID')
        self.worker_id = self.utils_env.get_environment_variable('WORKER_ID')
        self.controller_url = self.utils_env.get_environment_variable('CONTROLLER_URL')
        self.worker_api_key = self.utils_env.get_environment_variable('WORKER_API_KEY')
        self.worker = Worker(self.cluster_id, self.worker_id)

    def job_iteration(self):
        print('JobControllerNotifyAlive.job_iteration(): Started')

        # Try to notify alive
        try:
            self.client_controller.worker_alive(self.controller_url, self.worker_api_key, self.worker)
        except:
            # Sleep and return
            print('JobControllerNotifyAlive.job_iteration(): WARNING!!! Failed to notify alive to ' + str(self.controller_url))
            print('JobControllerNotifyAlive.job_iteration(): Sleeping...')
            time.sleep(30)
            print('JobControllerNotifyAlive.job_iteration(): Finished')

        # Sleep and return
        print('JobControllerNotifyAlive.job_iteration(): Notified alive to ' + str(self.controller_url))
        print('JobControllerNotifyAlive.job_iteration(): Sleeping...')
        time.sleep(60)
        print('JobControllerNotifyAlive.job_iteration(): Finished')
