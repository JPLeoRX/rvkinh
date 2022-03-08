import concurrent.futures
from itertools import repeat
import time
from typing import List
from injectable import injectable, autowired, Autowired
from rvkinh_utils import UtilsScapy
from rvkinh_message_protocol import PortscanCheckSingleOutput, PortscanCheckMultipleOutput, PortscanCheckAllOutput

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

@injectable
class ServicePortscan:
    @autowired
    def __init__(self, utils_scapy: Autowired(UtilsScapy)):
        self.utils_scapy = utils_scapy
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=24)

    def check_single(self, target_ip_address: str, target_port: int) -> PortscanCheckSingleOutput:
        t1 = time.time()
        target_ip_address, target_port, open = self.utils_scapy.check_port(target_ip_address, target_port)
        t2 = time.time()
        t = t2 - t1
        print('ServicePortscan.check_single(): Checked 1 port at ' + target_ip_address + ' in ' + str(round(t, 3)) + ' s')
        return PortscanCheckSingleOutput(target_ip_address, target_port, open)

    def check_multiple(self, target_ip_address: str, list_of_target_ports: List[int]) -> PortscanCheckMultipleOutput:
        t1 = time.time()
        map_of_target_ports = {}
        list_of_target_open_ports = []
        for result in self.executor.map(self.utils_scapy.check_port, repeat(target_ip_address), list_of_target_ports):
            target_ip_address, target_port, open = result[0], result[1], result[2]
            map_of_target_ports[target_port] = open
            if open:
                list_of_target_open_ports.append(target_port)
        t2 = time.time()
        t = t2 - t1
        print('ServicePortscan.check_multiple(): Checked ' + str(len(list_of_target_ports)) + ' ports at ' + target_ip_address + ' in ' + str(round(t, 3)) + ' s')
        return PortscanCheckMultipleOutput(target_ip_address, list_of_target_ports, map_of_target_ports, list_of_target_open_ports)

    def check_all(self, target_ip_address: str) -> PortscanCheckAllOutput:
        t1 = time.time()
        list_of_target_open_ports = []
        for result in self.executor.map(self.utils_scapy.check_port, repeat(target_ip_address), TOP_PORTS):
            target_ip_address, target_port, open = result[0], result[1], result[2]
            if open:
                list_of_target_open_ports.append(target_port)
        t2 = time.time()
        t = t2 - t1
        print('ServicePortscan.check_all(): Checked ' + str(len(TOP_PORTS)) + ' ports at ' + target_ip_address + ' in ' + str(round(t, 3)) + ' s')
        return PortscanCheckAllOutput(target_ip_address, list_of_target_open_ports)
