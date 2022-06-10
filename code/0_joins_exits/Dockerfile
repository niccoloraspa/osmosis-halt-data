FROM ubuntu:20.04

# Requirements
RUN apt update
RUN apt install -y jq 
RUN apt install -y wget

# Download osmosis binary
ADD https://github.com/osmosis-labs/osmosis/releases/download/v9.0.0/osmosisd-9.0.0-linux-amd64 /usr/bin/osmosisd
RUN chmod +x /usr/bin/osmosisd

# Copy scripts
WORKDIR /app
COPY scripts/get_data.sh /app
RUN chmod +x get_data.sh
RUN mkdir -p /app/data/tx

COPY docker-entrypoint.sh /bin/
RUN chmod +x /bin/docker-entrypoint.sh
ENTRYPOINT ["/bin/docker-entrypoint.sh"]

