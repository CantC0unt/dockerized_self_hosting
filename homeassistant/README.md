## Example

```yaml
services:
  homeassistant:
    image: ghcr.io/home-assistant/home-assistant:stable
    container_name: homeassistant
    platform: linux/arm64
    hostname: homeassistant
    networks:
      macvlan_net:
        ipv4_address: 192.168.0.7
    environment:
      TZ: 'Asia/Kolkata'
    volumes:
      - ./config:/config
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
    privileged: true


networks:
  macvlan_net:
    external: true
```


### Home Assistant Compose 

![Static Badge](https://img.shields.io/badge/image-homeassistant/home--assistant:stable-pink)

[![Docker Image Version](https://img.shields.io/docker/v/homeassistant/home-assistant/stable)](https://hub.docker.com/r/homeassistant/home-assistant)
[![Docker Image Size](https://img.shields.io/docker/image-size/homeassistant/home-assistant/stable)](https://hub.docker.com/r/homeassistant/home-assistant)
[![Docker Pulls](https://img.shields.io/docker/pulls/homeassistant/home-assistant)](https://hub.docker.com/r/homeassistant/home-assistant)
[![Docker Stars](https://img.shields.io/docker/stars/homeassistant/home-assistant)](https://hub.docker.com/r/homeassistant/home-assistant)

[![GitHub Repo stars](https://img.shields.io/github/stars/home-assistant/core)](https://github.com/home-assistant/core)
[![GitHub forks](https://img.shields.io/github/forks/home-assistant/core)](https://github.com/home-assistant/core)
[![GitHub License](https://img.shields.io/github/license/home-assistant/core)](https://github.com/home-assistant/core)
[![GitHub last commit](https://img.shields.io/github/last-commit/home-assistant/core)](https://github.com/home-assistant/core)

\* image is pulled from ghcr not dockerhub

```yaml
homeassistant:
  image: ghcr.io/home-assistant/home-assistant:stable
  container_name: homeassistant
  hostname: homeassistant
  networks:
    macvlan_net:
      ipv4_address: <static ip for homeassistant>
  environment:
    TZ: '<timezone>'
  volumes:
    - ./config:/config
    - /etc/localtime:/etc/localtime:ro
  restart: unless-stopped
  privileged: true
```

|value|replace with|conditions|
|-|-|-|
|`<static ip for homeassistant>`|Any local IP|It _**MUST NOT**_ be assigned to another device by your DHCP server.<br> Use an IP outside of DHCP range.
|`<timezone>`|Your Timezone|


### Home Assistant Volumes

```bash
mkdir ~/dockerized_homeassistant/config
```

|volume|mapped volume|uses|
|-|-|-|
|`./config`|`/config`|Store HOME ASSISTANT configurations
|`/etc/localtime`|`/etc/localtime`|Read-Only access to get Date-Time info


### Run

\* macvlan_net must be up before this is started

\** you can replace the network configuration in the compose file with the one from `macvlan_net/docker-compose.yml`

```bash
docker compose -f ~/dockerized_homeassistant/docker-compose.yml up -d
```


### Docker Logs

```bash
docker logs homeassistant
```