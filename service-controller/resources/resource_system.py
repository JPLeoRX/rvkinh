from typing import List
from fastapi import APIRouter
from rvkinh_message_protocol import Worker
from services.service_liveness import ServiceLiveness


router_system = APIRouter()
service_liveness = ServiceLiveness()


@router_system.get("/system/workers_alive", response_model=List[Worker])
def system_workers_alive() -> List[Worker]:
    return service_liveness.get_workers_alive()
