# Initial setup
FROM python:3.8
RUN apt-get update && apt-get upgrade -y

# Install system utils
RUN apt-get install -y apt-utils software-properties-common
RUN apt-get install -y iputils-ping nmap netcat
RUN apt-get install -y vim wget curl git

# Common dependencies
RUN pip install requests==2.25.1
RUN pip install fastapi==0.63.0
RUN pip install uvicorn==0.13.3
RUN pip install injectable==3.4.4
RUN pip install pika==1.1.0
RUN pip install simplestr==0.5.0

# Proxy message protocol
COPY ./proxy-message-protocol /proxy-message-protocol
WORKDIR /proxy-message-protocol
RUN python setup.py sdist bdist_wheel && pip install .

# Proxy utils
COPY ./proxy-utils /proxy-utils
WORKDIR /proxy-utils
RUN python setup.py sdist bdist_wheel && pip install .

# Main app
COPY ./service-central /app
WORKDIR /app
RUN chmod a+x main.sh

# Run command
CMD './main.sh'
