from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PortscanCheckMultipleInput(BaseModel):
    target_ip_address: str
    list_of_target_ip_ports: List[int]

    def __init__(self, target_ip_address: str, list_of_target_ip_ports: List[int]) -> None:
        super().__init__(target_ip_address=target_ip_address, list_of_target_ip_ports=list_of_target_ip_ports)
