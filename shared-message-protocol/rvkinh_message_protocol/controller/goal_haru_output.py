from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from rvkinh_message_protocol.controller.worker_haru_settings import WorkerHaruSettings


@gen_str_repr_eq
class GoalHaruOutput(BaseModel):
    http_flood_target_urls: List[str]
    worker_settings: WorkerHaruSettings

    def __init__(self, http_flood_target_urls: List[str], worker_settings: WorkerHaruSettings) -> None:
        super().__init__(http_flood_target_urls=http_flood_target_urls, worker_settings=worker_settings)
