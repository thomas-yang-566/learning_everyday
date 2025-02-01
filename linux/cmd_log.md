```bash
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10028 -j DNAT --to-destination 60.169.42.228:10028
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

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10031 -j DNAT --to-destination 106.110.107.225:10031
iptables -A FORWARD -i eth0 -p tcp --dport 9007 -j ACCEPT
```

## delete

```bash
#iptables -t nat -v -L PREROUTING -n --line-number
#iptables -t nat -D PREROUTING {rule-number-here}

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10201 -j DNAT --to-destination 106.110.107.225:10031
iptables -A FORWARD -i eth0 -p tcp --dport 9210 -j ACCEPT
```
106.110.107.40

183.158.138.74
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 1010 -j DNAT --to-destination 60.169.42.168:10101
60.169.40.81
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10028 -j DNAT --to-destination 60.169.42.8:10028
## 220.161.243.185
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10243 -j DNAT --to-destination 220.161.243.185:10243
iptables -A FORWARD -i eth0 -p tcp --dport 10028 -j ACCEPT
27.159.184.79

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10019 -j DNAT --to-destination 114.235.209.236:10119

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10019 -j DNAT --to-destination 49.88.10.9:10003
iptables -A FORWARD -i eth0 -p tcp --dport 10003 -j ACCEPT

## 180.127.165.187
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 10019 -j DNAT --to-destination 180.127.165.187:9001
iptables -A FORWARD -i eth0 -p tcp --dport 9001 -j ACCEPT


mkdir ~/ip-update
cd ~/ip-update
wget 94.103.4.41/main-amd64-20240306232658
vim 

#pm2 restart server --cron-restart="5 * * * *"

curl -v https://h5.ptudd.com:2087

nohup gost -L ss://aes-256-gcm:w0rd2019@:10233 2>&1 10233.log &


nohup gost -L tcp://:9210/171.14.149.204:9210 > 9210.log 2>&1 &