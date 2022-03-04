import os
import rvkinh_proxy_utils
from injectable import load_injection_container
load_injection_container()
load_injection_container(str(os.path.dirname(rvkinh_proxy_utils.__file__)))
from fastapi import FastAPI
from channel_listener import ChannelListener


app = FastAPI()
listener = ChannelListener()
listener.register()
