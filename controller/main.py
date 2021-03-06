# Run dependency injections
import os
import tekleo_common_utils
import rvkinh_utils
from injectable import load_injection_container
load_injection_container()
load_injection_container(str(os.path.dirname(tekleo_common_utils.__file__)))
load_injection_container(str(os.path.dirname(rvkinh_utils.__file__)))

# FastAPI app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.resource_control import router_control
from resources.resource_ping import router_ping
from resources.resource_worker import router_worker

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
app.include_router(router_control)
app.include_router(router_ping)
app.include_router(router_worker)
