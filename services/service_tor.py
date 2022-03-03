import threading
import time
from injectable import injectable
from stem import Signal
from stem.control import Controller


TOR_CHANGE_IP_LOCK = threading.Lock()


@injectable
class ServiceTor:
    def get_proxy(self) -> (str, int):
        return '127.0.0.1', 8118

    def change_ip_tor(self) -> bool:
        with TOR_CHANGE_IP_LOCK:
            try:
                time.sleep(0.6)
                with Controller.from_port(port=9051) as controller:
                    controller.authenticate(password='password')
                    controller.signal(Signal.NEWNYM)
                print("ServiceTor.change_ip_tor(): Generated new IP")
                time.sleep(0.6)
                return True

            except:
                print('WARNING! Failed to change TOR ip!')

        return False
