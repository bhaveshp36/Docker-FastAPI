# Docker-FastAPI
## simple app based on Python-FastAPI with Dockerfile.

**Docker Installation**

>https://docs.docker.com/engine/install/ 

**Building Docker Image**

cd into the directory where dockerfile is located 

> $ sudo docker build . *image-name*

**eg.**

> $ sudo docker build . fastapi

**Running Docker Image**
> $ sudo systemctl start docker
> $ sudo docker run -d -p *host-port*:*docker-port* *image-name*

**eg.**

>$ sudo docker run -d -p 8080:8000 fastapi

**Testing Container**

go to '*host-ip*:8080'

**eg.**
192.168.0.101:8080/docs
