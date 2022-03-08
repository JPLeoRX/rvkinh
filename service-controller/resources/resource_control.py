from typing import List
from fastapi import APIRouter, Request, Depends, HTTPException
from rvkinh_message_protocol import AttackOrchestration, Worker, PortscanCheckAllInput, PortscanCheckAllOutput, PortscanCheckMultipleInput, PortscanCheckMultipleOutput, PortscanCheckSingleInput, PortscanCheckSingleOutput
from tekleo_common_utils import UtilsEnv
from services.service_attack_orchestration import ServiceAttackOrchestration
from services.service_liveness import ServiceLiveness
from services.service_portscan import ServicePortscan


router_control = APIRouter()
service_attack_orchestration = ServiceAttackOrchestration()
service_liveness = ServiceLiveness()
service_portscan = ServicePortscan()


# Load API KEY
utils_env = UtilsEnv()
utils_env.load_environment_variables(['CONTROL_API_KEY'])
control_api_key = utils_env.get_environment_variable('CONTROL_API_KEY')
if len(control_api_key) == 0:
    print('resource_control: Warning!!! Control api key was not specified')


# API KEY authentication method
def authorize_control(request: Request) -> bool:
    if "Api-Key" not in request.headers:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if request.headers["Api-Key"] != control_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True


@router_control.post("/attack/orchestration/start", response_model=bool)
def attack_orchestration_start(attack_orchestration: AttackOrchestration, authorized: bool = Depends(authorize_control)) -> bool:
    return service_attack_orchestration.set(attack_orchestration)


@router_control.get("/attack/orchestration/stop", response_model=bool)
def attack_orchestration_stop(authorized: bool = Depends(authorize_control)) -> bool:
    return service_attack_orchestration.set(AttackOrchestration({}, {}))


@router_control.get("/attack/status", response_model=AttackOrchestration)
def attack_status(authorized: bool = Depends(authorize_control)) -> AttackOrchestration:
    return service_attack_orchestration.get()


@router_control.get("/system/workers_alive", response_model=List[Worker])
def system_workers_alive(authorized: bool = Depends(authorize_control)) -> List[Worker]:
    return service_liveness.get_workers_alive()


@router_control.post("/portscan/check/single", response_model=PortscanCheckSingleOutput)
def check_single(input: PortscanCheckSingleInput, authorized: bool = Depends(authorize_control)) -> PortscanCheckSingleOutput:
    return service_portscan.check_single(input.target_ip_address, input.target_port)


@router_control.post("/portscan/check/multiple", response_model=PortscanCheckMultipleOutput)
def check_multiple(input: PortscanCheckMultipleInput, authorized: bool = Depends(authorize_control)) -> PortscanCheckMultipleOutput:
    return service_portscan.check_multiple(input.target_ip_address, input.list_of_target_ports)


@router_control.post("/portscan/check/all", response_model=PortscanCheckAllOutput)
def check_all(input: PortscanCheckAllInput, authorized: bool = Depends(authorize_control)) -> PortscanCheckAllOutput:
    return service_portscan.check_all(input.target_ip_address)
