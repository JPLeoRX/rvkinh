from fastapi import APIRouter
from message_protocol.portscan_check_all_input import PortscanCheckAllInput
from message_protocol.portscan_check_single_input import PortscanCheckSingleInput
from message_protocol.portscan_check_single_output import PortscanCheckSingleOutput
from services.service_portscan import ServicePortscan


router_portscan = APIRouter()
service_portscan = ServicePortscan()


@router_portscan.post("/portscan/check/single", response_model=PortscanCheckSingleOutput)
def check_single(input: PortscanCheckSingleInput) -> PortscanCheckSingleOutput:
    open = service_portscan.check_port(input.target_ip_address, input.target_ip_port)[2]
    return PortscanCheckSingleOutput(input.target_ip_address, input.target_ip_port, open)

def check_multiple():
    pass

def check_all(input: PortscanCheckAllInput):
    pass