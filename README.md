# DTG - "Docker Threat Grid" Project

Project aiming to improve interaction with Threat Grid and expand on your static analyses capabilityes.
(Threat Grid script can be used as standalone tool outside of Docker build.)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

What software packages you need to get started with running container :

```
Docker
Python3
```

### Installing

Start docker daemon service :

```
systemctl start docker.service
```

Build container from path where Dockerfile is stored :

```
docker build --tag forensiccontainer:1.0 .
```

Run container that listens to localhost :

```
docker run -d -p 127.0.0.1:4200:4200 -p 127.0.0.1:9090:9090 --name malware forensiccontainer:1.0
```

Test run radare webserver on 9090 port that we mapped in container run :
```
r2 -e http.bind=0.0.0.0 -c='H' /path/sample.exe
```

Stopping container -

```
docker stop malware ; docker rm malware
```

### Threat Grid Script features -

```
  ________                    __  ______     _     __      ___          _                   
 /_  __/ /_  ________  ____ _/ /_/ ____/____(_)___/ /     /   |  ____  (_)     ____  __  __ 
  / / / __ \/ ___/ _ \/ __ `/ __/ / __/ ___/ / __  /_____/ /| | / __ \/ /     / __ \/ / / / 
 / / / / / / /  /  __/ /_/ / /_/ /_/ / /  / / /_/ /_____/ ___ |/ /_/ / / _   / /_/ / /_/ /  
/_/ /_/ /_/_/   \___/\__,_/\__/\____/_/  /_/\__,_/     /_/  |_/ .___/_/ (_) / .___/\__, /   
                                                             /_/           /_/    /____/    
                                                                                            
[?] Choose option: 1. List users samples. (private, last 5)
 > 1. List users samples. (private, last 5)
   2. List organisation samples. (private, last 5)
   3. Sample search. (Any IoC)
   4. Download a sample. (Sample ID)
   5. Submit a url.
   6. Submit a File.
   
```
