FROM ubuntu:22.04
RUN apt update && apt install -y gcc libcap2-bin sudo
RUN useradd -m -s /bin/bash lowpriv && echo "lowpriv:lowpriv" | chpasswd
RUN gpasswd -d lowpriv sudo || true

RUN echo "flag{root_capabilities_escalation}" > /root/flag5.txt && chmod 600 /root/flag5.txt
COPY rootshell.c /home/lowpriv/rootshell.c

RUN gcc /home/lowpriv/rootshell.c -o /home/lowpriv/rootshell && chown lowpriv:lowpriv /home/lowpriv/rootshell && chmod 755 /home/lowpriv/rootshell && setcap cap_setuid+ep /home/lowpriv/rootshell
USER lowpriv
WORKDIR /home/lowpriv
CMD ["sleep", "infinity"]
