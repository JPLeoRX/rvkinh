# Initial setup
FROM python:3.8
RUN apt-get update

# Install system utils
RUN apt-get install -y ffmpeg libsm6 libxext6 libgl1
RUN apt-get install -y apt-utils software-properties-common
RUN apt-get install -y iputils-ping nmap netcat
RUN apt-get install -y vim wget curl git

# Install TOR
RUN apt-get install -y tor
RUN tor --version

# Install privoxy
RUN apt-get install -y privoxy
RUN privoxy --version

# Common dependencies
RUN pip install requests==2.25.1
RUN pip install fastapi==0.63.0
RUN pip install uvicorn==0.13.3
RUN pip install injectable==3.4.4
RUN pip install simplestr==0.5.0
RUN pip install stem==1.8.0
RUN pip install aiohttp==3.8.1
RUN pip install scapy==2.4.5
RUN pip install stem==1.8.0
RUN pip install tekleo-common-message-protocol==0.0.0.3
RUN pip install tekleo-common-utils==0.0.1.0

# Our message protocol
COPY ./shared-message-protocol /shared-message-protocol
WORKDIR /shared-message-protocol
RUN python setup.py sdist bdist_wheel && pip install .

# Our utils
COPY ./shared-utils /shared-utils
WORKDIR /shared-utils
RUN python setup.py sdist bdist_wheel && pip install .

# Our message client
COPY ./shared-message-client /shared-message-client
WORKDIR /shared-message-client
RUN python setup.py sdist bdist_wheel && pip install .

# Main app
COPY ./worker-akio /app
WORKDIR /app
RUN chmod a+x main.sh

# Run command
CMD './main.sh'
