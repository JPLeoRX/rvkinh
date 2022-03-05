# Preparations
- Port scanner

# Attacks
#### DoS:
- SYN flood
- Ping (ICMP) flood
- HTTP GET flood


# Run
#### Worker AIKO
```shell script
docker run --name=rvkinh-service-worker-aiko --rm -tid -e CLUSTER_ID=temp_c -e WORKER_ID=temp_w -e CONTROLLER_URL=http://142.93.38.82:8888 jpleorx/rvkinh-service-worker-aiko:latest
```

#### Worker HARU
```shell script
docker run --name=rvkinh-service-worker-haru --rm -tid -e CLUSTER_ID=temp_c -e WORKER_ID=temp_w -e CONTROLLER_URL=http://142.93.38.82:8888 jpleorx/rvkinh-service-worker-haru:latest
```

#### Controller
```shell script
docker run --name=rvkinh-service-controller --rm -tid -p 8888:8888 jpleorx/rvkinh-service-controller:latest
```


