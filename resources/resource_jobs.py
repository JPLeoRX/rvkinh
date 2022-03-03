from fastapi import APIRouter
from jobs.jobs_registry import JOB_ATTACK_SYN_FLOOD
from message_protocol.job_attack_syn_flood_start_input import JobAttackSynFloodStartInput
from message_protocol.job_attack_syn_flood_status_output import JobAttackSynFloodStatusOutput

router_jobs = APIRouter()


@router_jobs.post("/job/attack/syn_flood/start", response_model=bool)
def attack_syn_flood_start(input: JobAttackSynFloodStartInput) -> bool:
    if JOB_ATTACK_SYN_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_SYN_FLOOD.set_target(input.target_ip_address, input.target_port)
        return JOB_ATTACK_SYN_FLOOD.start()


@router_jobs.get("/job/attack/syn_flood/status", response_model=JobAttackSynFloodStatusOutput)
def attack_syn_flood_is_running() -> JobAttackSynFloodStatusOutput:
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
