from typing import Dict, List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PortscanCheckMultipleOutput(BaseModel):
    target_ip_address: str
    list_of_target_ip_ports: List[int]
    map_of_target_ports: Dict[int, bool]

    def __init__(self, target_ip_address: str, list_of_target_ip_ports: List[int], map_of_target_ports: Dict[int, bool]) -> None:
        super().__init__(target_ip_address=target_ip_address, list_of_target_ip_ports=list_of_target_ip_ports, map_of_target_ports=map_of_target_ports)
