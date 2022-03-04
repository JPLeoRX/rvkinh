from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PortscanCheckSingleOutput(BaseModel):
    target_ip_address: str
    target_port: int
    open: bool

    def __init__(self, target_ip_address: str, target_port: int, open: bool) -> None:
        super().__init__(target_ip_address=target_ip_address, target_port=target_port, open=open)
