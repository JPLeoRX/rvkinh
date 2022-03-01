from services.service_portscan import ServicePortscan

service = ServicePortscan()

r = service.check_ports_sequential('hackthissite.org', [22, 80, 443])
print(r)

r = service.check_ports_parallel('hackthissite.org', [22, 80, 443])
print(r)