from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class Worker(BaseModel):
    cluster_id: str
    worker_id: str

    def __init__(self, cluster_id: str, worker_id: str) -> None:
        super().__init__(cluster_id=cluster_id, worker_id=worker_id)
