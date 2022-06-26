import threading
from injectable import injectable
from rvkinh_message_protocol import WorkerHaruSettings


WORKER_SETTINGS = WorkerHaruSettings(-1, -1, '', -1)
WORKER_SETTINGS_LOCK = threading.Lock()


@injectable
class StorageSettings:
    def get_worker_settings(self) -> WorkerHaruSettings:
        return WORKER_SETTINGS

    def set_worker_settings(self, worker_settings: WorkerHaruSettings):
        with WORKER_SETTINGS_LOCK:
            # Copy new
            WORKER_SETTINGS.parallel_min_requests = worker_settings.parallel_min_requests
            WORKER_SETTINGS.parallel_max_requests = worker_settings.parallel_max_requests
            WORKER_SETTINGS.proxy_type = worker_settings.proxy_type
            WORKER_SETTINGS.proxy_ip_change_frequency = worker_settings.proxy_ip_change_frequency
