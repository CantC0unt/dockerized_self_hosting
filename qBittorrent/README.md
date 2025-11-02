## Example

```yaml
services:
  qbittorrent:
    image: lscr.io/linuxserver/qbittorrent:latest
    container_name: qbittorrent
    platform: linux/arm64
    hostname: qbittorrent
    networks:
      macvlan_net:
        ipv4_address: 192.168.0.9
    environment:
      TZ: 'Asia/Kolkata'
      PUID: '0'
      PGID: '0'
      WEBUI_PORT: '80'
      TORRENTING_PORT: '6881'
    volumes:
      - ./config:/config
      - /mnt/share/jellyfin/movies:/movies
      - /mnt/share/jellyfin/shows:/shows
      - /mnt/share/jellyfin/music:/music
    restart: unless-stopped

networks:
  macvlan_net:
    external: true
```


## "The Guide"

### Install Directory

The install can be done in any directory, I am going to use a new directory in home for convenience. If you choose to install somewhere else, dont forget to make the change the install directory in the other commands.

```bash
mkdir ~/dockerized_qbittorrent
```

### qBittorrent Compose 

![Static Badge](https://img.shields.io/badge/image-linuxserver/qbittorrent:latest-pink)

[![Docker Image Version](https://img.shields.io/docker/v/linuxserver/qbittorrent)](https://hub.docker.com/r/linuxserver/qbittorrent)
[![Docker Image Size](https://img.shields.io/docker/image-size/linuxserver/qbittorrent)](https://hub.docker.com/r/linuxserver/qbittorrent)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/qbittorrent)](https://hub.docker.com/r/linuxserver/qbittorrent)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/qbittorrent)](https://hub.docker.com/r/linuxserver/qbittorrent)

[![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-qbittorrent)](https://github.com/linuxserver/docker-qbittorrent)
[![GitHub forks](https://img.shields.io/github/forks/linuxserver/docker-qbittorrent)](https://github.com/linuxserver/docker-qbittorrent)
[![GitHub License](https://img.shields.io/github/license/linuxserver/docker-qbittorrent)](https://github.com/linuxserver/docker-qbittorrent)
[![GitHub last commit](https://img.shields.io/github/last-commit/linuxserver/docker-qbittorrent)](https://github.com/linuxserver/docker-qbittorrent)

\* image is pulled from lscr not dockerhub

```yaml
qbittorrent:
  image: lscr.io/linuxserver/qbittorrent:latest
  container_name: qbittorrent
  hostname: qbittorrent
  networks:
    macvlan_net:
      ipv4_address: <static ip for qbittorrent>
  environment:
    TZ: '<timezone>'
    PUID: '<user id>'
    PGID: '<user group id>'
    WEBUI_PORT: '80'
    TORRENTING_PORT: '6881'
  volumes:
    - ./config:/config
    - <download dir on your device>:<download dir as seen by qbittorrent>
  restart: unless-stopped
```

|value|replace with|conditions|
|-|-|-|
|`<static ip for qbittorrent>`|Any local IP|It _**MUST NOT**_ be assigned to another device by your DHCP server.<br> Use an IP outside of DHCP range.
|`<timezone>`|Your Timezone|
|`<user id>`|Any User ID|The User _**MUST**_ have write access to download directories and config directory
|`<user group id>`|Any Group ID| Group _**MUST**_ contain the configured User ID
|`<download dir on your device>`|Any directory|
|`<download dir as seen by qbittorrent>`|Any directory|

\* you can add as many download directory binds as you want. using just one with sub directories for category folders will also work.


### qBittorrent Volumes

```bash
mkdir ~/dockerized_qbittorrent/config
```

|volume|mapped volume|uses|
|-|-|-|
|`./config`|`/config`|Store QBITTORRENT configurations


### Run

\* macvlan_net must be up before this is started

\** you can replace the network configuration in the compose file with the one from `macvlan_net/docker-compose.yml`

```bash
docker compose -f ~/dockerized_qbittorrent/docker-compose.yml up -d
```


### Docker Logs

```bash
docker logs qbittorrent
```

