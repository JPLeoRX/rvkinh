from fastapi import APIRouter
from rvkinh_message_protocol import AttackOrchestration
from services.service_attack_orchestration import ServiceAttackOrchestration


router_attack_orchestration = APIRouter()
service_attack_orchestration = ServiceAttackOrchestration()


@router_attack_orchestration.post("/attack/orchestration/start", response_model=bool)
def attack_orchestration_start(attack_orchestration: AttackOrchestration) -> bool:
    return service_attack_orchestration.set(attack_orchestration)


@router_attack_orchestration.get("/attack/orchestration/stop", response_model=bool)
def attack_orchestration_stop() -> bool:
    return service_attack_orchestration.set(AttackOrchestration({}, {}))


@router_attack_orchestration.get("/attack/status", response_model=AttackOrchestration)
def attack_status() -> AttackOrchestration:
    return service_attack_orchestration.get()
