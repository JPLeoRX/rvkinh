import time
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsEnv
from rvkinh_message_protocol import Worker
from rvkinh_utils import AbstractJob
from rvkinh_message_client import ClientControllerWorker



@injectable
class JobControllerGetGoal(AbstractJob):
    @autowired
    def __init__(self, client_controller_worker: Autowired(ClientControllerWorker), utils_env: Autowired(UtilsEnv)):
        super().__init__()
        self.client_controller_worker = client_controller_worker
        self.utils_env = utils_env
        self.utils_env.load_environment_variables(['CLUSTER_ID', 'WORKER_ID', 'CONTROLLER_URL'])
        self.cluster_id = self.utils_env.get_environment_variable('CLUSTER_ID')
        self.worker_id = self.utils_env.get_environment_variable('WORKER_ID')
        self.controller_url = self.utils_env.get_environment_variable('CONTROLLER_URL')
        self.worker = Worker(self.cluster_id, self.worker_id)

    def job_iteration(self):
        print('JobControllerGetGoal.job_iteration(): Started')
        goal = self.client_controller_worker.worker_goal_haru(self.controller_url, self.worker)
        print('JobControllerGetGoal.job_iteration(): Retrieved goal ' + str(goal) + ' from ' + str(self.controller_url))
        print('JobControllerGetGoal.job_iteration(): Sleeping...')
        time.sleep(20)
        print('JobControllerGetGoal.job_iteration(): Finished')
