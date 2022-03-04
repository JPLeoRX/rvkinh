from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class JobAttackHttpFloodStatusOutput(BaseModel):
    target_url: str
    is_running: bool

    def __init__(self, target_url: str, is_running: bool) -> None:
        super().__init__(target_url=target_url, is_running=is_running)
