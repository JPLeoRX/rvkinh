# HOW TO - Install Docker, docker-compose and run Tor Flood Attack on Ubuntu
This was tested on Ubuntu 20.04, but should probably work on 18.04 as well.

## Update your system and install common libraries (optional)
```shell script
apt-get update && apt-get upgrade -y
apt-get install -y ca-certificates curl gnupg lsb-release
apt-get install -y apt-utils software-properties-common vim wget curl git
apt-get install -y iputils-ping nmap netcat
```

## Install Docker
```shell script
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
```

## Install Docker compose
```shell script
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

docker-compose --version
```

## Increase swap memory to 6GB (optional, but needed for almost any base-level servers)
```shell script
sudo fallocate -l 6G /swapfile && sudo chmod 600 /swapfile
sudo mkswap /swapfile && sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
free -h
```

## Download and run Tor Flood Attack
```shell script
docker login --username jpleorx
docker run --name=tekleo-security --rm -tid -p 9543:9543 jpleorx/tekleo:tekleo-security
```
