FROM ubuntu:22.04

RUN apt update && apt install -y sudo
RUN useradd -m -s /bin/bash player && echo "player:player" | chpasswd
RUN adduser player sudo
RUN mkdir -p /opt/locked_dir
RUN chmod 711 /opt/locked_dir
RUN bash -c 'echo "flag{sudo_or_sneaky}" > /opt/locked_dir/flag.txt'
RUN chmod 644 /opt/locked_dir/flag.txt
RUN ls -ld /opt/locked_dir
RUN ls -l /opt/locked_dir/flag.txt
USER player
CMD ["sleep", "infinity"]
