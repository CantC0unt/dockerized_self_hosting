## Example

```yaml
services:

  unbound:
    container_name: unbound
    image: klutchell/unbound:latest
    platform: linux/arm64
    hostname: unbound
    networks:
      macvlan_net:
        ipv4_address: 192.168.0.5
    volumes:
      - './unbound:/etc/unbound/custom.conf.d'
    cap_add:
      - NET_BIND_SERVICE
    restart: unless-stopped

  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    platform: linux/arm64
    hostname: pihole
    networks:
      macvlan_net:
        ipv4_address: 192.168.0.6
        ipv6_address: fd00::6
    environment:
      TZ: 'Asia/Kolkata'
      FTLCONF_webserver_api_password: 'pihole'
      FTLCONF_dns_listeningMode: 'all'
      FTLCONF_dns_upstreams: '192.168.0.5#53'
      FTLCONF_dhcp_start: '192.168.0.15'
      FTLCONF_dhcp_end: '192.168.0.249'
      FTLCONF_dhcp_router: '192.168.0.1'
      FTLCONF_dhcp_active: 'true'
      FTLCONF_dhcp_ipv6: 'true'
      DNSMASQ_USER: 'root'
    depends_on:
      - unbound
    volumes:
      - './etc-pihole:/etc/pihole'
      - './etc-dnsmasq.d:/etc/dnsmasq.d'
    cap_add:
      - CHOWN
      - NET_ADMIN
      - NET_BIND_SERVICE
      - NET_RAW
      - SYS_TIME
      - SYS_NICE
    restart: unless-stopped

networks:
  macvlan_net:
    external: true
```

```conf
server:
  interface: 0.0.0.0
  port: 53
  access-control: 192.168.0.0/16 allow
  do-ip4: yes
  do-udp: yes
  do-tcp: yes  
  do-ip6: yes
  verbosity: 1
  root-hints: /etc/unbound/custom.conf.d/root.hints
```


## "The Guide"

### Install Directory

The install can be done in any directory, I am going to use a new directory in home for convenience. If you choose to install somewhere else, dont forget to make the change the install directory in the other commands.

```bash
mkdir ~/dockerized_pihole_with_unbound
```


### Unbound Compose 

![Static Badge](https://img.shields.io/badge/image-klutchell/unbound:latest-pink)

[![Docker Image Version](https://img.shields.io/docker/v/klutchell/unbound)](https://hub.docker.com/r/klutchell/unbound)
[![Docker Image Size](https://img.shields.io/docker/image-size/klutchell/unbound)](https://hub.docker.com/r/klutchell/unbound)
[![Docker Pulls](https://img.shields.io/docker/pulls/klutchell/unbound)](https://hub.docker.com/r/klutchell/unbound)
[![Docker Stars](https://img.shields.io/docker/stars/klutchell/unbound)](https://hub.docker.com/r/klutchell/unbound)

[![GitHub Repo stars](https://img.shields.io/github/stars/klutchell/unbound-docker)](https://github.com/klutchell/unbound-docker)
[![GitHub forks](https://img.shields.io/github/forks/klutchell/unbound-docker)](https://github.com/klutchell/unbound-docker)
[![GitHub License](https://img.shields.io/github/license/klutchell/unbound-docker)](https://github.com/klutchell/unbound-docker)
[![GitHub last commit](https://img.shields.io/github/last-commit/klutchell/unbound-docker)](https://github.com/klutchell/unbound-docker)

```yaml
  unbound:
    container_name: unbound
    image: klutchell/unbound:latest
    platform: linux/arm64
    hostname: unbound
    networks:
      macvlan_net:
        ipv4_address: <static ip for unbound>
    volumes:
      - './unbound:/etc/unbound/custom.conf.d'
    cap_add:
      - NET_BIND_SERVICE
    restart: unless-stopped
```

|value|replace with|conditions|
|-|-|-|
|`<static ip for unbound>`|Any local IP|It _**MUST NOT**_ be assigned to another device by your DHCP server.<br> Use an IP outside of DHCP range.


### Unbound Volumes

```bash
mkdir ~/dockerized_pihole_with_unbound/unbound
```
|volume|mapped volume|uses|
|-|-|-|
|`./unbound`|`/etc/unbound/custom.conf.d`|Store UNBOUND configurations


### Unbound Root Hints

```bash
wget https://www.internic.net/domain/named.root -qO- | tee ~/dockerized_pihole_with_unbound/unbound/root.hints
```


### Unbound Config

```conf
server:
  interface: 0.0.0.0
  port: 53
  access-control: 192.168.0.0/<ip range> allow
  do-ip4: yes
  do-udp: yes
  do-tcp: yes  
  do-ip6: yes
  verbosity: 1
  root-hints: /etc/unbound/custom.conf.d/root.hints
```

|value|replace with|conditions|
|-|-|-|
|`<ip range>`|`integer >= 16`|This is used to allow incoming requests from clients <br> At the minimum, the static IP for PiHole must be inlcuded in the range.


### PiHole Compose 

![Static Badge](https://img.shields.io/badge/image-pihole/pihole:latest-pink)

[![Docker Image Version](https://img.shields.io/docker/v/pihole/pihole)](https://hub.docker.com/r/pihole/pihole)
[![Docker Image Size](https://img.shields.io/docker/image-size/pihole/pihole)](https://hub.docker.com/r/pihole/pihole)
[![Docker Pulls](https://img.shields.io/docker/pulls/pihole/pihole)](https://hub.docker.com/r/pihole/pihole)
[![Docker Stars](https://img.shields.io/docker/stars/pihole/pihole)](https://hub.docker.com/r/pihole/pihole)

[![GitHub Repo stars](https://img.shields.io/github/stars/pi-hole/docker-pi-hole)](https://github.com/pi-hole/docker-pi-hole)
[![GitHub forks](https://img.shields.io/github/forks/pi-hole/docker-pi-hole)](https://github.com/pi-hole/docker-pi-hole)
[![GitHub License](https://img.shields.io/github/license/pi-hole/docker-pi-hole)](https://github.com/pi-hole/docker-pi-hole)
[![GitHub last commit](https://img.shields.io/github/last-commit/pi-hole/docker-pi-hole)](https://github.com/pi-hole/docker-pi-hole)

```yaml
pihole:
    container_name: pihole
    image: pihole/pihole:latest
    hostname: pihole
    networks:
      macvlan_net:
        ipv4_address: <static ip for pihole>
        ipv6_address: <static ipv6 for pihole - ULA>
    environment:
      TZ: 'Asia/Kolkata'
      FTLCONF_webserver_api_password: 'pihole'
      FTLCONF_dns_listeningMode: 'all' #post-configurable
      FTLCONF_dns_upstreams: '<static ip for unbound>#53' #post-configurable
      FTLCONF_dhcp_start: '<first assignable ip>' #post-configurable
      FTLCONF_dhcp_end: '<last assignable ip>' #post-configurable
      FTLCONF_dhcp_router: '<router ip>' #post-configurable
      FTLCONF_dhcp_active: 'true' #post-configurable
      FTLCONF_dhcp_ipv6: 'true' #post-configurable
      DNSMASQ_USER: 'root'
    depends_on:
      - unbound
    volumes:
      - './etc-pihole:/etc/pihole'
      - './etc-dnsmasq.d:/etc/dnsmasq.d'
    cap_add:
      - CHOWN
      - NET_ADMIN
      - NET_BIND_SERVICE
      - NET_RAW
      - SYS_TIME
      - SYS_NICE
    restart: unless-stopped

networks:
  macvlan_net:
    external: true
```

\* all configs marked `#post-configurable` can be configured later through pihole WebUI. Configuring it through compose will make it unconfigurable from WebUI.

|value|replace with|conditions|
|-|-|-|
|`<static ip for pihole>`|Any local IP|It _**MUST NOT**_ be assigned to another device by your DHCP server.<br> Use an IP outside of DHCP range.
|`<static ipv6 for pihole - ULA>`|Any ULA IP|It _**MUST NOT**_ be assigned to another device.
|`<static ip for unbound>`|Any local IP|It _**MUST**_ be assigned to unbound service.
|`<first assignable ip>`|Any local IP|
|`<last assignable ip>`|Any local IP|
|`<router ip>`|Any local IP|It _**MUST**_ be assigned to your router.


### PiHole Volumes

```bash
mkdir ~/dockerized_pihole_with_unbound/etc-pihole ~/dockerized_pihole_with_unbound/etc-dnsmasq.d
```
|volume|mapped volume|uses|
|-|-|-|
|`./etc-pihole`|`/etc/pihole`|Store PIHOLE configurations
|`./etc-dnsmasq.d`|`/etc/dnsmasq.d`|Store DNSMASQ configurations


### Run

\* macvlan_net must be up before this is started

\** you can replace the network configuration in the compose file with the one from `macvlan_net/docker-compose.yml `

```bash
docker compose -f ~/dockerized_pihole_with_unbound/docker-compose.yml up -d
```


### Unbound Docker Logs

```bash
docker logs unbound
```


### PiHole Docker Logs

```bash
docker logs pihole
```


### Router Config

1. Turn off DHCP Server for IPv4
2. Set IPv6 DHCP to RADVD or SLAAC
3. Enable ULA prefix
   1. ULA Prefix = `fd00::` or `fc00::` based on ULA IPs used in this config
   2. ULA Prefix Length = `64`
4. Disable RDNSS


### RPI / Base Device Config

Assign a static IP to your _**device**_ running the PiHole container so that PiHole can get online as the DHCP Server

