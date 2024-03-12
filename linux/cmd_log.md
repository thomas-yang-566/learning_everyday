```bash
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10028 -j DNAT --to-destination 220.178.185.54:10028
iptables -A FORWARD -i eth0 -p tcp --dport 10028 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10024 -j DNAT --to-destination 106.110.107.40:10024
iptables -A FORWARD -i eth0 -p tcp --dport 10024 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10020 -j DNAT --to-destination 222.79.58.9:10020
iptables -A FORWARD -i eth0 -p tcp --dport 10020 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10100 -j DNAT --to-destination 222.79.59.199:10100
iptables -A FORWARD -i eth0 -p tcp --dport 10100 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10100 -j DNAT --to-destination 222.79.59.199:10100
iptables -A FORWARD -i eth0 -p tcp --dport 10100 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10022 -j DNAT --to-destination 121.228.255.121:10022
iptables -A FORWARD -i eth0 -p tcp --dport 10022 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10143 -j DNAT --to-destination 27.156.196.46:10143
iptables -A FORWARD -i eth0 -p tcp --dport 10143 -j ACCEPT

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10031 -j DNAT --to-destination 180.127.165.150:10031
iptables -A FORWARD -i eth0 -p tcp --dport 10031 -j ACCEPT
```

## delete

```bash
#iptables -t nat -v -L PREROUTING -n --line-number
#iptables -t nat -D PREROUTING {rule-number-here}
```
106.110.107.40

183.158.138.74
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 1010 -j DNAT --to-destination 183.158.138.74:10101
60.169.40.81
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10028 -j DNAT --to-destination 60.169.40.81:10028
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10243 -j DNAT --to-destination 27.159.184.79:10243
iptables -A FORWARD -i eth0 -p tcp --dport 10028 -j ACCEPT
27.159.184.79

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10019 -j DNAT --to-destination 106.110.107.40:10019
iptables -A FORWARD -i eth0 -p tcp --dport 10019 -j ACCEPT