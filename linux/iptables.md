# iptables

一个设置防火墙的工具

```bash
#iptables -t nat -F // clear all nat rules
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 172.104.61.139:80
iptables -t nat -A POSTROUTING -j MASQUERADE
iptables -A FORWARD -i eth0 -p tcp --dport 80 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination 172.104.61.139:443

iptables -A FORWARD -i eth0 -p tcp --dport 443 -j ACCEPT
iptables -t nat -A POSTROUTING -j MASQUERADE
## add rule to mapping local port
iptables -t nat -A PREROUTING -p tcp --dport 8081 -j REDIRECT --to-port 8080
```
iptables -A FORWARD -i eth0 -o eth1 -p tcp --syn --dport 80 -m conntrack --ctstate NEW -j ACCEPT

114.235.209.77
## 参考

```text


--to offset
Set the offset from which it starts looking for any matching. If not passed, default is the packet size.

--to-destination [ipaddr][-ipaddr][:port[-port]]
which can specify a single new destination IP address, an inclusive range of IP addresses, and optionally, a port range  (which  is  only
valid  if the rule also specifies -p tcp or -p udp).  If no port range is specified, then the destination port will never be modified. If
no IP address is specified then only the destination port will be modified.

          In Kernels up to 2.6.10 you can add several --to-destination options. For those  kernels,  if  you  specify  more  than  one  destination
          address, either via an address range or multiple --to-destination options, a simple round-robin (one after another in cycle) load balanc-
          ing takes place between these addresses.  Later Kernels (>= 2.6.11-rc1) don’t have the ability to NAT to multiple ranges anymore.

```

1. https://linux-training.be/networking/ch14.html#:~:text=The%20nat%20table%20in%20iptables,look%20at%20the%20NAT%20table.