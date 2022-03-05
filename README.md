# Preparations
- Port scanner

# Attacks
#### DoS:
- SYN flood
- Ping (ICMP) flood
- HTTP GET flood

# Run (worker only)
```shell script
docker run --name=rvkinh-service-worker --rm -ti -p 9543:9543 jpleorx/rvkinh-service-worker:latest
```

# Run (worker with receiver)
```shell script
docker run --name=rvkinh-service-worker --rm -tid --network='host' -p 9543:9543 jpleorx/rvkinh-service-worker:latest
docker run --name=rvkinh-service-worker-receiver --rm -tid --network='host' -e WORKER_PROXY_CLUSTER_ID=c2 -e WORKER_PROXY_WORKER_ID=w1 -e WORKER_PROXY_CLIENT_PROXIED_BASE_URL=http://127.0.0.1:9543/ -e WORKER_PROXY_RABBITMQ_HOST=142.93.38.82 -e WORKER_PROXY_RABBITMQ_PORT=5672 -e WORKER_PROXY_RABBITMQ_USERNAME=myUser -e WORKER_PROXY_RABBITMQ_PASSWORD=myPassword -p 7777:7777 jpleorx/rvkinh-service-worker-receiver:latest
```