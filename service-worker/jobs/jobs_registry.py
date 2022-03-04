print("jobs_registry: Started initialization")

from worker.jobs import JobAttackHttpFlood
JOB_ATTACK_HTTP_FLOOD = JobAttackHttpFlood()

from worker.jobs import JobAttackPingFlood
JOB_ATTACK_PING_FLOOD = JobAttackPingFlood()

from worker.jobs import JobAttackSynFlood
JOB_ATTACK_SYN_FLOOD = JobAttackSynFlood()

print("jobs_registry: Finished initialization")
