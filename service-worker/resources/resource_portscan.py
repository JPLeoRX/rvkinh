import time
import concurrent.futures
from itertools import repeat
from fastapi import APIRouter
from rvkinh_message_protocol import PortscanCheckAllInput, PortscanCheckAllOutput, PortscanCheckSingleInput, PortscanCheckSingleOutput, PortscanCheckMultipleInput, PortscanCheckMultipleOutput
from services.service_scapy import ServiceScapy


TOP_PORTS = [
    20, 21, 22, 23, 53, 80, 443, 853, 992,

    # From https://secbot.com/docs/ports/common-ports
    7210, # MaxDB
    3306, # MySQL
    1521, 1830, # Oracle DB
    5432, # PostgreSQL
    1433, 1434, # SQL Server (MSSQL)
    9200, 9300, # Elasticsearch
    27017, 27018, 27019, 28017, # MongoDB
    6379, # Redis
    7574, 8983, # Solr
    8000, # Django
    8005, 8009, 8080, 8081, 8443, 8181, # Tomcat
    6443, 8080, # Kubernetes
    2181, 2888, 3888, # ZooKeeper

    # From https://www.jhipster.tech/common-ports/
    3000, # Grafana
    5000, # Logstash
    9090, # Prometheus
    9092, # Kafka

    4200, # Angular
]

TOP_PORTS = list(set(TOP_PORTS))

router_portscan = APIRouter()
service_scapy = ServiceScapy()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=24)

# Check on
# 178.62.102.230
# 68.183.43.171

@router_portscan.post("/portscan/check/single", response_model=PortscanCheckSingleOutput)
def check_single(input: PortscanCheckSingleInput) -> PortscanCheckSingleOutput:
    t1 = time.time()
    target_ip_address, target_port, open = service_scapy.check_port(input.target_ip_address, input.target_port)
    t2 = time.time()
    t = t2 - t1

    print('resource_portscan.check_single(): Checked 1 port at ' + input.target_ip_address + ' in ' + str(round(t, 3)) + ' s')
    return PortscanCheckSingleOutput(input.target_ip_address, input.target_port, open)


@router_portscan.post("/portscan/check/multiple", response_model=PortscanCheckMultipleOutput)
def check_multiple(input: PortscanCheckMultipleInput) -> PortscanCheckMultipleOutput:
    t1 = time.time()
    map_of_target_ports = {}
    list_of_target_open_ports = []
    for result in executor.map(service_scapy.check_port, repeat(input.target_ip_address), input.list_of_target_ports):
        target_ip_address, target_port, open = result[0], result[1], result[2]
        map_of_target_ports[target_port] = open
        if open:
            list_of_target_open_ports.append(target_port)
    t2 = time.time()
    t = t2 - t1

    print('resource_portscan.check_multiple(): Checked ' + str(len(input.list_of_target_ports)) + ' ports at ' + input.target_ip_address + ' in ' + str(round(t, 3)) + ' s')
    return PortscanCheckMultipleOutput(input.target_ip_address, input.list_of_target_ports, map_of_target_ports, list_of_target_open_ports)


@router_portscan.post("/portscan/check/all", response_model=PortscanCheckAllOutput)
def check_all(input: PortscanCheckAllInput) -> PortscanCheckAllOutput:
    t1 = time.time()
    list_of_target_open_ports = []
    for result in executor.map(service_scapy.check_port, repeat(input.target_ip_address), TOP_PORTS):
        target_ip_address, target_port, open = result[0], result[1], result[2]
        if open:
            list_of_target_open_ports.append(target_port)
    t2 = time.time()
    t = t2 - t1

    print('resource_portscan.check_all(): Checked ' + str(len(TOP_PORTS)) + ' ports at ' + input.target_ip_address + ' in ' + str(round(t, 3)) + ' s')
    return PortscanCheckAllOutput(input.target_ip_address, list_of_target_open_ports)
