# Run dependency injections
import os
import threading

from injectable import load_injection_container
load_injection_container()

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
from jobs.jobs_registry import JOB_ATTACK_SYN_FLOOD
thread1 = threading.Thread(target=JOB_ATTACK_SYN_FLOOD.job_loop)
thread1.start()

# Shutdown handler
@app.on_event('shutdown')
def shutdown_event():
    print('shutdown_event(): Started')
    JOB_ATTACK_SYN_FLOOD.kill()
    thread1.join()
    print('shutdown_event(): Finished')