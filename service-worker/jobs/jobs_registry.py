print("jobs_registry: Started initialization")

from jobs.job_attack_http_flood import JobAttackHttpFlood
JOB_ATTACK_HTTP_FLOOD = JobAttackHttpFlood()

from jobs.job_attack_ping_flood import JobAttackPingFlood
JOB_ATTACK_PING_FLOOD = JobAttackPingFlood()

from jobs.job_attack_syn_flood import JobAttackSynFlood
JOB_ATTACK_SYN_FLOOD = JobAttackSynFlood()

print("jobs_registry: Finished initialization")
