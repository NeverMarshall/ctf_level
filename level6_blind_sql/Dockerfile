FROM python:3.11-slim

RUN useradd -m -s /bin/bash player
WORKDIR /app
RUN apt-get update && apt-get install -y curl &&  pip install flask

COPY app.py /app/app.py

RUN chown -R player:player /app
USER player

EXPOSE 8006
CMD ["python", "app.py"]
