from fastapi import APIRouter
from jobs.jobs_registry import JOB_ATTACK_SYN_FLOOD, JOB_ATTACK_PING_FLOOD, JOB_ATTACK_HTTP_FLOOD
from message_protocol.job_attack_http_flood_start_input import JobAttackHttpFloodStartInput
from message_protocol.job_attack_http_flood_status_output import JobAttackHttpFloodStatusOutput
from message_protocol.job_attack_ping_flood_start_input import JobAttackPingFloodStartInput
from message_protocol.job_attack_ping_flood_status_output import JobAttackPingFloodStatusOutput
from message_protocol.job_attack_syn_flood_start_input import JobAttackSynFloodStartInput
from message_protocol.job_attack_syn_flood_status_output import JobAttackSynFloodStatusOutput

router_jobs = APIRouter()

# Attack syn flood
#-----------------------------------------------------------------------------------------------------------------------
@router_jobs.post("/job/attack/syn_flood/start", response_model=bool)
def attack_syn_flood_start(input: JobAttackSynFloodStartInput) -> bool:
    if JOB_ATTACK_SYN_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_SYN_FLOOD.set_target(input.target_ip_address, input.target_port)
        return JOB_ATTACK_SYN_FLOOD.start()


@router_jobs.get("/job/attack/syn_flood/status", response_model=JobAttackSynFloodStatusOutput)
def attack_syn_flood_status() -> JobAttackSynFloodStatusOutput:
    target_ip_address = JOB_ATTACK_SYN_FLOOD.target_ip_address
    if target_ip_address is None:
        target_ip_address = ''
    target_port = JOB_ATTACK_SYN_FLOOD.target_port
    if target_port is None:
        target_port = -1
    is_running = JOB_ATTACK_SYN_FLOOD.is_running()
    return JobAttackSynFloodStatusOutput(target_ip_address, target_port, is_running)


@router_jobs.get("/job/attack/syn_flood/stop", response_model=bool)
def attack_syn_flood_stop() -> bool:
    if not JOB_ATTACK_SYN_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_SYN_FLOOD.clean_target()
        return JOB_ATTACK_SYN_FLOOD.stop()
#-----------------------------------------------------------------------------------------------------------------------



# Attack ping flood
#-----------------------------------------------------------------------------------------------------------------------
@router_jobs.post("/job/attack/ping_flood/start", response_model=bool)
def attack_ping_flood_start(input: JobAttackPingFloodStartInput) -> bool:
    if JOB_ATTACK_PING_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_PING_FLOOD.set_target(input.target_ip_address)
        return JOB_ATTACK_PING_FLOOD.start()


@router_jobs.get("/job/attack/ping_flood/status", response_model=JobAttackPingFloodStatusOutput)
def attack_ping_flood_status() -> JobAttackPingFloodStatusOutput:
    target_ip_address = JOB_ATTACK_PING_FLOOD.target_ip_address
    if target_ip_address is None:
        target_ip_address = ''
    is_running = JOB_ATTACK_PING_FLOOD.is_running()
    return JobAttackPingFloodStatusOutput(target_ip_address, is_running)


@router_jobs.get("/job/attack/ping_flood/stop", response_model=bool)
def attack_ping_flood_stop() -> bool:
    if not JOB_ATTACK_PING_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_PING_FLOOD.clean_target()
        return JOB_ATTACK_PING_FLOOD.stop()
#-----------------------------------------------------------------------------------------------------------------------



# Attack http flood
#-----------------------------------------------------------------------------------------------------------------------
@router_jobs.post("/job/attack/http_flood/start", response_model=bool)
def attack_http_flood_start(input: JobAttackHttpFloodStartInput) -> bool:
    if JOB_ATTACK_HTTP_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_HTTP_FLOOD.set_target(input.target_ip_address)
        return JOB_ATTACK_HTTP_FLOOD.start()


@router_jobs.get("/job/attack/http_flood/status", response_model=JobAttackHttpFloodStatusOutput)
def attack_http_flood_status() -> JobAttackHttpFloodStatusOutput:
    target_ip_address = JOB_ATTACK_HTTP_FLOOD.target_ip_address
    if target_ip_address is None:
        target_ip_address = ''
    is_running = JOB_ATTACK_HTTP_FLOOD.is_running()
    return JobAttackHttpFloodStatusOutput(target_ip_address, is_running)


@router_jobs.get("/job/attack/http_flood/stop", response_model=bool)
def attack_http_flood_stop() -> bool:
    if not JOB_ATTACK_HTTP_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_HTTP_FLOOD.clean_target()
        return JOB_ATTACK_HTTP_FLOOD.stop()
#-----------------------------------------------------------------------------------------------------------------------
