from fastapi import APIRouter
from jobs.jobs_registry import JOB_ATTACK_SYN_FLOOD
from message_protocol.job_attack_syn_flood_input import JobAttackSynFloodInput

router_jobs = APIRouter()


@router_jobs.post("/job/attack/syn_flood/start", response_model=bool)
def attack_syn_flood_start(input: JobAttackSynFloodInput) -> bool:
    if JOB_ATTACK_SYN_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_SYN_FLOOD.set_target(input.target_ip_address, input.target_port)
        return JOB_ATTACK_SYN_FLOOD.start()


@router_jobs.get("/job/attack/syn_flood/is_running", response_model=bool)
def attack_syn_flood_is_running() -> bool:
    return JOB_ATTACK_SYN_FLOOD.is_running()


@router_jobs.get("/job/attack/syn_flood/stop", response_model=bool)
def attack_syn_flood_stop() -> bool:
    if not JOB_ATTACK_SYN_FLOOD.is_running():
        return False
    else:
        JOB_ATTACK_SYN_FLOOD.clean_target()
        return JOB_ATTACK_SYN_FLOOD.stop()
