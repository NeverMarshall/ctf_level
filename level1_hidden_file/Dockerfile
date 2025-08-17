FROM ubuntu:20.04

RUN apt update && apt install -y openssh-server sudo && mkdir -p /run/sshd 
RUN useradd -m -s /bin/bash player && echo "player:player" | chpasswd && usermod -aG sudo player
RUN echo "flag{hidden_file_found}" > /home/player/.hidden_file.txt && chown player:player /home/player/.hidden_file.txt && chmod 644 /home/player/.hidden_file.txt
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
