## Example

```yaml
networks:
  macvlan_net:
    name: macvlan_net
    driver: macvlan
    enable_ipv6: true
    driver_opts:
      parent: eth0
    ipam:
      config:
        - subnet: "192.168.0.0/24"
          gateway: "192.168.0.1"
        - subnet: "fd00::/64"
          gateway: "fd00::1"
```

