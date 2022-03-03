from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class JobAttackPingFloodStartInput(BaseModel):
    target_ip_address: str

    def __init__(self, target_ip_address: str) -> None:
        super().__init__(target_ip_address=target_ip_address)
