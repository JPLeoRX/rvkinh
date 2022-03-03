import threading
import time
import traceback


class AbstractJob:
    def __init__(self):
        self.lock = threading.Lock()
        self.started = False
        self.stopped = False
        self.killed = False

    def kill(self) -> bool:
        with self.lock:
            self.killed = True
            return True

    def start(self) -> bool:
        with self.lock:
            if not self.started:
                self.started = True
                return True
        return False

    def stop(self):
        with self.lock:
            if self.started and not self.stopped:
                self.stopped = True
                return True
        return False

    def is_running(self):
        return self.started and not self.stopped

    def idle(self):
        time.sleep(10)

    def job_iteration(self):
        pass

    def job_loop(self):
        while not self.killed:
            # If this job hasn't started yet
            if not self.started:
                self.idle()
                continue

            # If this job was stopped
            if self.started and self.stopped:
                self.started = False
                self.stopped = False
                continue

            # If this job shoul run
            if self.started and not self.stopped:
                try:
                    self.job_iteration()
                except:
                    print(traceback.format_exc())

