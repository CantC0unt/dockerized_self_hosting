## Example

```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    platform: linux/arm64
    hostname: jellyfin
    networks:
      macvlan_net:
        ipv4_address: 192.168.0.8
    cap_add:
      - NET_BIND_SERVICE
    volumes:
      - ./config:/config
      - ./cache:/cache
      - type: bind
        source: /mnt/share/jellyfin/music
        target: /music
      - type: bind
        source: /mnt/share/jellyfin/movies
        target: /movies
      - type: bind
        source: /mnt/share/jellyfin/shows
        target: /shows
      - type: bind
        source: ./fonts
        target: /usr/local/share/fonts/custom
        read_only: true
    restart: unless-stopped
    environment:
      - JELLYFIN_PublishedServerUrl=http://jelly.fin
    extra_hosts:
      - 'host.docker.internal:host-gateway'

networks:
  macvlan_net:
    external: true
```


## "The Guide"

### Install Directory

The install can be done in any directory, I am going to use a new directory in home for convenience. If you choose to install somewhere else, dont forget to make the change the install directory in the other commands.

```bash
mkdir ~/dockerized_jellyfin
```


### Jellyfin Compose 

![Static Badge](https://img.shields.io/badge/image-jellyfin/jellyfin:latest-pink)

[![Docker Image Version (tag)](https://img.shields.io/docker/v/jellyfin/jellyfin/latest)](https://hub.docker.com/r/jellyfin/jellyfin)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/jellyfin/jellyfin/latest)](https://hub.docker.com/r/jellyfin/jellyfin)
[![Docker Pulls](https://img.shields.io/docker/pulls/jellyfin/jellyfin)](https://hub.docker.com/r/jellyfin/jellyfin)
[![Docker Stars](https://img.shields.io/docker/stars/jellyfin/jellyfin)](https://hub.docker.com/r/jellyfin/jellyfin)

[![GitHub Repo stars](https://img.shields.io/github/stars/jellyfin/jellyfin)](https://github.com/jellyfin/jellyfin)
[![GitHub forks](https://img.shields.io/github/forks/jellyfin/jellyfin)](https://github.com/jellyfin/jellyfin)
[![GitHub License](https://img.shields.io/github/license/jellyfin/jellyfin)](https://github.com/jellyfin/jellyfin)
[![GitHub last commit](https://img.shields.io/github/last-commit/jellyfin/jellyfin)](https://github.com/jellyfin/jellyfin)

```yaml
jellyfin:
  image: jellyfin/jellyfin
  container_name: jellyfin
  hostname: jellyfin
  networks:
    macvlan_net:
      ipv4_address: <static ip for jellyfin>
  cap_add:
    - NET_BIND_SERVICE
  volumes:
    - ./config:/config
    - ./cache:/cache
    - type: bind
      source: <path to data dir>
      target: <dir as seen by jellyfin>
    - type: bind
      source: ./fonts
      target: /usr/local/share/fonts/custom
      read_only: true
  restart: unless-stopped
  environment:
    - JELLYFIN_PublishedServerUrl=<server url>
  extra_hosts:
    - 'host.docker.internal:host-gateway'
```

|value|replace with|conditions|
|-|-|-|
|`<static ip for jellyfin>`|Any local IP|It _**MUST NOT**_ be assigned to another device by your DHCP server.<br> Use an IP outside of DHCP range.
|`<path to data dir>`|Any directory|
|`<dir as seen by jellyfin>`|Any directory|
|`<server url>`|Any url|Dont use existing TLD or a reachable URL

\* you can add as many data directory binds as you want. using just one with sub directories for category folders will also work.


### Jellyfin Volumes

```bash
mkdir ~/dockerized_jellyfin/config ~/dockerized_jellyfin/cache ~/dockerized_jellyfin/fonts
```

\* your data directories must exist at the configured path

|volume|mapped volume|uses|
|-|-|-|
|`./config`|`/config`|Store JELLYFIN configurations
|`./cache`|`/cache`|Store JELLYFIN cache
|`./fonts`|`/usr/local/share/fonts/custom`|Store Fonts for WebUI

### Run

\* macvlan_net must be up before this is started

\** you can replace the network configuration in the compose file with the one from `macvlan_net/docker-compose.yml`

```bash
docker compose -f ~/dockerized_jellyfin/docker-compose.yml up -d
```


### Docker Logs

```bash
docker logs jellyfin
```

