from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PortscanCheckSingleInput(BaseModel):
    target_ip_address: str
    target_port: int

    def __init__(self, target_ip_address: str, target_port: int) -> None:
        super().__init__(target_ip_address=target_ip_address, target_port=target_port)
