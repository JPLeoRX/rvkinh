import threading
from typing import List
from injectable import injectable


HTTP_FLOOD_TARGET_URLS = []
PING_FLOOD_TARGET_IP_ADDRESS = ""
SYN_FLOOD_TARGET_IP_ADDRESS = ""
SYN_FLOOD_TARGET_PORT = -1
STORAGE_TARGET_LOCK = threading.Lock()


@injectable
class StorageTarget:
    def get_ping_flood_target_ip_address(self) -> str:
        return PING_FLOOD_TARGET_IP_ADDRESS

    def get_syn_flood_target_ip_address(self) -> str:
        return SYN_FLOOD_TARGET_IP_ADDRESS

    def get_syn_flood_target_port(self) -> int:
        return SYN_FLOOD_TARGET_PORT

    def set_ping_flood_target_ip_address(self, ping_flood_target_ip_address: str):
        with STORAGE_TARGET_LOCK:
            global PING_FLOOD_TARGET_IP_ADDRESS
            PING_FLOOD_TARGET_IP_ADDRESS = ping_flood_target_ip_address

    def set_syn_flood_target_ip_address(self, syn_flood_target_ip_address: str):
        with STORAGE_TARGET_LOCK:
            global SYN_FLOOD_TARGET_IP_ADDRESS
            SYN_FLOOD_TARGET_IP_ADDRESS = syn_flood_target_ip_address

    def set_syn_flood_target_port(self, syn_flood_target_port: int):
        with STORAGE_TARGET_LOCK:
            global SYN_FLOOD_TARGET_PORT
            SYN_FLOOD_TARGET_PORT = syn_flood_target_port
