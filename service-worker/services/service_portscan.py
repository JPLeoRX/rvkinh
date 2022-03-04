import concurrent.futures
import socket
import socks
import time
from itertools import repeat
from typing import List, Dict
from injectable import injectable, autowired, Autowired

from worker.services import ServiceTor


@injectable
class ServicePortscan:
    @autowired
    def __init__(self, service_tor: Autowired(ServiceTor)):
        self.THREAD_COUNT = 24
        self.service_tor = service_tor
        self.proxy_host, self.proxy_port = service_tor.get_proxy()

    def check_port(self, target_ip_address: str, target_port: int, timeout: float = 1.0) -> (str, int, bool):
        ''' Try to connect to a specified host on a specified port.
        If the connection takes longer then the TIMEOUT we set we assume
        the host is down. If the connection is a success we can safely assume
        the host is up and listing on port x. If the connection fails for any
        other reason we assume the host is down and the port is closed.'''

        # Create and configure the socket.
        sock = socks.socksocket()
        sock.settimeout(timeout)
        sock.set_proxy(socks.HTTP, self.proxy_host, self.proxy_port)

        # the SO_REUSEADDR flag tells the kernel to reuse a local
        # socket in TIME_WAIT state, without waiting for its natural
        # timeout to expire.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Like connect(address), but return an error indicator instead
        # of raising an exception for errors returned by the C-level connect()
        # call (other problems, such as “host not found,” can still raise exceptions).
        # The error indicator is 0 if the operation succeeded, otherwise the value of
        # the errnovariable. This is useful to support, for example, asynchronous connects.
        connected = sock.connect_ex((target_ip_address, target_port)) == 0

        # Mark the socket closed.
        # The underlying system resource (e.g. a file descriptor)
        # is also closed when all file objects from makefile() are closed.
        # Once that happens, all future operations on the socket object will fail.
        # The remote end will receive no more data (after queued data is flushed).
        sock.close()

        # return True if port is open or False if port is closed.
        return target_ip_address, target_port, connected

    def check_ports_sequential(self, target_ip_address: str, list_of_target_ports: List[int], timeout: float = 1.0) -> Dict[int, bool]:
        results_map = {}

        t1 = time.time()
        for target_port in list_of_target_ports:
            result = self.check_port(target_ip_address, target_port, timeout)
            results_map[result[1]] = result[2]
        t2 = time.time()
        t = t2 - t1

        print('ServicePortscan.check_ports_sequential(): Checked ' + str(len(list_of_target_ports)) + ' ports at ' + target_ip_address + ' in ' + str(round(t, 3)) + ' s')
        return results_map

    def check_ports_parallel(self, target_ip_address: str, list_of_target_ports: List[int], timeout: float = 1.0) -> Dict[int, bool]:
        results_map = {}

        t1 = time.time()
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.THREAD_COUNT)
        for result in executor.map(self.check_port, repeat(target_ip_address), list_of_target_ports, repeat(timeout)):
            results_map[result[1]] = result[2]
        t2 = time.time()
        t = t2 - t1

        print('ServicePortscan.check_ports_parallel(): Checked ' + str(len(list_of_target_ports)) + ' ports at ' + target_ip_address + ' in ' + str(round(t, 3)) + ' s')
        return results_map
