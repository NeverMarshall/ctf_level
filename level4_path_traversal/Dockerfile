FROM python:3.11-slim

RUN useradd -m -s /bin/bash player && echo "player:player" | chpasswd

WORKDIR /app
RUN pip install flask

COPY app.py /app/app.py

RUN mkdir /app/files && echo "HELLO!" > /app/files/readme.txt
RUN echo "flag{path_traversal_success}" > /flag.txt

RUN chown -R player:player /app /flag.txt
USER player
EXPOSE 8004
CMD ["python", "app.py"]
