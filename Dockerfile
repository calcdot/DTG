FROM ubuntu:latest

COPY ThreatGrid-Api.py /usr/local/bin/ThreatGrid-Api.py
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y tzdata && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y python3.8 openssh-server byobu curl git htop man p7zip-full vim nano shellinabox python3-pip python python3-tk && \
  mkdir /var/run/sshd && \
  chmod +x /usr/local/bin/ThreatGrid-Api.py
  pip3 install inquirer && \
  echo 'root: < PASSWORD >' | chpasswd && \
  sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
  sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
  echo "export VISIBLE=now" >> /etc/profile && \
  echo "alias radaresubmit='r2 -e http.bind=0.0.0.0 -c=H '" >> /root/.bashrc && \
  git clone https://github.com/radareorg/radare2 /root/.radare2 && \
  sh /root/.radare2/sys/install.sh && \ 
  rm -rf /var/lib/apt/lists/*

WORKDIR /root
ENV HOME /root
ENV NOTVISIBLE "in users profile"
EXPOSE 4200
EXPOSE 9090
COPY theme.css /usr/theme.css
COPY Services.sh /root/.Services.sh
CMD ["sh", "/root/.Services.sh"]
