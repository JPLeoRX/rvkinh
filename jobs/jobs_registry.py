print("jobs_registry: Started initialization")
from jobs.job_attack_syn_flood import JobAttackSynFlood
JOB_ATTACK_SYN_FLOOD = JobAttackSynFlood()

from jobs.job_attack_ping_flood import JobAttackPingFlood
JOB_ATTACK_PING_FLOOD = JobAttackPingFlood()
print("jobs_registry: Finished initialization")
