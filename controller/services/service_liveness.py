import threading
from typing import List
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsTime
from rvkinh_message_protocol import Worker


MARK_ALIVE_LOCK = threading.Lock()
WORKER_LAST_SEEN_TIMESTAMPS_MS = {}


@injectable()
class ServiceLiveness:
    @autowired
    def __init__(self, utils_time: Autowired(UtilsTime)):
        self.utils_time = utils_time

    def mark_alive(self, worker: Worker) -> bool:
        with MARK_ALIVE_LOCK:
            WORKER_LAST_SEEN_TIMESTAMPS_MS[worker] = self.utils_time.get_timestamp_ms_now()
            print('ServiceLiveness.mark_alive() ' + str(worker) + ' is alive')
        return True

    def is_alive(self, worker: Worker) -> bool:
        # If we have never seen this worker before
        if worker not in WORKER_LAST_SEEN_TIMESTAMPS_MS:
            return False

        # Find timestamps and their difference
        last_seen_timestamp_ms = WORKER_LAST_SEEN_TIMESTAMPS_MS[worker]
        current_timestamp_ms = self.utils_time.get_timestamp_ms_now()
        delta = current_timestamp_ms - last_seen_timestamp_ms

        # Accept that this worker is alive if it was seen less than 3 minutes ago
        if delta < 3 * 60 * 1000:
            return True
        else:
            return False

    def get_workers_alive(self) -> List[Worker]:
        results = []
        for worker in WORKER_LAST_SEEN_TIMESTAMPS_MS:
            if self.is_alive(worker):
                results.append(worker)
        return results
