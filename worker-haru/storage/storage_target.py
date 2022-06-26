import threading
from typing import List
from injectable import injectable


HTTP_FLOOD_TARGET_URLS = []
HTTP_FLOOD_TARGET_URLS_LOCK = threading.Lock()


@injectable
class StorageTarget:
    def get_http_flood_target_urls(self) -> List[str]:
        return HTTP_FLOOD_TARGET_URLS

    def set_http_flood_target_urls(self, http_flood_target_urls: List[str]):
        with HTTP_FLOOD_TARGET_URLS_LOCK:
            # Clear old
            HTTP_FLOOD_TARGET_URLS.clear()

            # Copy new
            for t in http_flood_target_urls:
                HTTP_FLOOD_TARGET_URLS.append(t)
