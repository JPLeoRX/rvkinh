from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class JobAttackHttpFloodStartInput(BaseModel):
    target_url: str

    def __init__(self, target_url: str) -> None:
        super().__init__(target_url=target_url)
