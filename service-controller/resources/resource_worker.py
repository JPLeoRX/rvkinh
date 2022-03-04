from fastapi import APIRouter
from rvkinh_message_protocol import Worker
from services.service_liveness import ServiceLiveness

router_worker = APIRouter()
service_liveness = ServiceLiveness()


@router_worker.post("/worker/alive", response_model=bool)
def worker_alive(worker: Worker) -> bool:
    return service_liveness.mark_alive(worker)
