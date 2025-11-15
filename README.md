# Dockerized Self Hosting
This repository contains configs (mostly docker compose files) for self hosting some services. Everything is tested for RPI but should work on any linux based system (Hopefully™)


## Motivation
I like hosting things myself over using service providers wherever I can.
However, when you host a lot things together on the same device, the setups become intertwined and a pain handle. So we have docker to the rescue. I'm also using MACVLAN because I like the separation of entities.  


## Components
 1. Home Automation
    - [Home Assistant](https://www.home-assistant.io/) - Open source home automation that puts local control and privacy first.
 2. Media Streaming/Hoarding
    - [Jellyfin](https://jellyfin.org/) - Media solution that puts you in control of your media.Stream to any device from your own server.
 3. Pocket Alternative - bookmark anything
    - [KaraKeep](https://www.home-assistant.io/) - Quickly save links, notes, and images and karakeep will automatically tag them for you using AI for faster retrieval.
 4. AdBlock and Privacy
    - [Pihole](https://pi-hole.net/) - Network-wide Ad Blocking with 
    - [Unbound](https://nlnetlabs.nl/projects/unbound/about/) - a validating, recursive, caching DNS resolver
 5. Torrent
    - [qBittorrent](https://www.qbittorrent.org/) - open-source software alternative to µTorrent - Fast, bulk torrent downloads from the desktop
 6. NAS/Shared Storage
    - [Samba](https://www.samba.org/) - SMB and Active Directory protocols for Linux and UNIX-like systems


## Structures

This Repository

```
root
├── <service>
│   ├── README.md
│   ├── <config>
│   └── install.sh
.
.
.
├── LICENSE
├── README.md
├── install.sh
└── docker-compose.yml
```

Install Directory for dockerized services

```
root
├── dockerized_<service>
│   ├── docker-compose.yml
|   ├── <volume>
│   └── install.log
.
.
.
```

(there can be multiple volumes and services)

## Usage

### "I know what I'm doing"
Copy the `config` (mostly `docker-compose.yml`) and modify it as you see fit.


### "I want to change the configs, but I dont fully know what I'm doing"
Check `README.md` under the service you want to install / modify.


### "I don't care, just get it up and running"

_**I will eventually™ add the install commands here once I am done with the install scripts, for now check `README.md` under the service you want to install / modify**_

