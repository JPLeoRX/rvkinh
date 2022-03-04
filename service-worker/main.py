# Run dependency injections
import os
import tekleo_common_utils
from injectable import load_injection_container
load_injection_container()
load_injection_container()
load_injection_container(str(os.path.dirname(tekleo_common_utils.__file__)))


import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.resource_jobs import router_jobs
from resources.resource_ping import router_ping
from resources.resource_portscan import router_portscan


app = FastAPI()

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(router_jobs)
app.include_router(router_ping)
app.include_router(router_portscan)

# Initialize jobs
from jobs.jobs_registry import JOB_ATTACK_HTTP_FLOOD, JOB_ATTACK_PING_FLOOD, JOB_ATTACK_SYN_FLOOD
thread1 = threading.Thread(target=JOB_ATTACK_HTTP_FLOOD.job_loop)
thread1.start()
thread2 = threading.Thread(target=JOB_ATTACK_PING_FLOOD.job_loop)
thread2.start()
thread3 = threading.Thread(target=JOB_ATTACK_SYN_FLOOD.job_loop)
thread3.start()


# Shutdown handler
@app.on_event('shutdown')
def shutdown_event():
    print('shutdown_event(): Started')
    JOB_ATTACK_HTTP_FLOOD.kill()
    thread1.join()
    JOB_ATTACK_PING_FLOOD.kill()
    thread2.join()
    JOB_ATTACK_SYN_FLOOD.kill()
    thread3.join()
    print('shutdown_event(): Finished')