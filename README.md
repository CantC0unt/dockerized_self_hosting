# Dockerized Self Hosting
This repository contains configs (mostly docker compose files) for self hosting some services. Everything is tested for RPI but should work on any linux based system (Hopefully™)

## Motivation
I like hosting things myself over using service providers wherever I can.
However, when you host a lot things together on the same device, the setups become intertwined and a pain handle. So we have docker to the rescue. I'm also using MACVLAN because I like the separation of entities.  

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
└── install.sh
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

- [ ] **I will eventually add the install commands here once I am done with the install scripts**