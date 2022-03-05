from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class GoalAkioOutput(BaseModel):
    http_flood_target_urls: List[str]
    ping_flood_target_ip_address: str
    syn_flood_target_ip_address: str
    syn_flood_target_port: int

    def __init__(self, http_flood_target_urls: List[str], ping_flood_target_ip_address: str, syn_flood_target_ip_address: str, syn_flood_target_port: int) -> None:
        super().__init__(http_flood_target_urls=http_flood_target_urls, ping_flood_target_ip_address=ping_flood_target_ip_address, syn_flood_target_ip_address=syn_flood_target_ip_address, syn_flood_target_port=syn_flood_target_port)
