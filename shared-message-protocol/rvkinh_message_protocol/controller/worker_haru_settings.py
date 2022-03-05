from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class WorkerHaruSettings(BaseModel):
    parallel_min_requests: int
    parallel_max_requests: int
    proxy_type: str                         # "tor" or "none"
    proxy_ip_change_frequency: int

    def __init__(self, parallel_min_requests: int, parallel_max_requests: int, proxy_type: str, proxy_ip_change_frequency: int) -> None:
        super().__init__(parallel_min_requests=parallel_min_requests, parallel_max_requests=parallel_max_requests, proxy_type=proxy_type, proxy_ip_change_frequency=proxy_ip_change_frequency)
