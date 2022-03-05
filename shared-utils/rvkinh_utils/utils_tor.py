import threading
import time
from stem import Signal
from stem.control import Controller
from injectable import injectable


TOR_CHANGE_IP_LOCK = threading.Lock()
TOR_PORT = 9051
TOR_PASSWORD = 'password'


@injectable
class UtilsTor:
    def change_ip_tor(self):
        with TOR_CHANGE_IP_LOCK:
            time.sleep(0.6)
            with Controller.from_port(port=TOR_PORT) as controller:
                controller.authenticate(password=TOR_PASSWORD)
                controller.signal(Signal.NEWNYM)
            time.sleep(0.6)
