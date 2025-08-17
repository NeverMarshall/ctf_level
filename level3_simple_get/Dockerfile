FROM python:3.11-slim
RUN useradd -m -s /bin/bash player && echo "player:player" | chpasswd
RUN mkdir -p /web/hidden && chown -R player:player /web
USER player
RUN echo "flag{easy_get}" > /web/hidden/flag
WORKDIR /web
EXPOSE 8001
CMD ["python3", "-m", "http.server", "8001"]
