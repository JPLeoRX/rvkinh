# Run dependency injections
import os
import rvkinh_proxy_utils
from injectable import load_injection_container
load_injection_container()
load_injection_container(str(os.path.dirname(rvkinh_proxy_utils.__file__)))


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from interceptor import Interceptor
from rvkinh_proxy_utils import UtilsEnv


app = FastAPI()

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Interceptor
utils_env = UtilsEnv()
interceptor = Interceptor()
@app.middleware("http")
async def intercept(request: Request, call_next):
    return await interceptor.intercept(utils_env.get_rabbitmq_config(), request, receive_timeout_in_seconds=10)
