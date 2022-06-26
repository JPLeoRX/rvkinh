print("jobs_registry: Started initialization")

from jobs.job_controller_get_goal import JobControllerGetGoal
JOB_CONTROLLER_GET_GOAL = JobControllerGetGoal()

from jobs.job_controller_notify_alive import JobControllerNotifyAlive
JOB_CONTROLLER_NOTIFY_ALIVE = JobControllerNotifyAlive()

print("jobs_registry: Finished initialization")
