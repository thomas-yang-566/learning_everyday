## 
wget https://521github.com/fatedier/frp/releases/download/v0.54.0/frp_0.54.0_linux_amd64.tar.gz
## frps service

vim /lib/systemd/system/frps.service

```text
[Unit]
Description=Frp Server Service
After=network.target
[Service]
Type=simple
User=nobody
Restart=on-failure
RestartSec=5s
ExecStart=/usr/local/frp_0.54.0_linux_amd64/frps -c /usr/local/frp_0.54.0_linux_amd64/frps.toml
[Install]
WantedBy=multi-user.target


```

vim /usr/local/frp_0.54.0_linux_amd64/frps.toml

```text
bindPort = 7090
auth.method = "token"
auth.token = "fejk$12A"
```

## frpc service

vim /lib/systemd/system/frpc.service

```text

[Unit]
Description=Frp Server Service
After=network.target
[Service]
Type=simple
User=nobody
Restart=on-failure
RestartSec=5s
ExecStart=/usr/local/frp_0.54.0_linux_amd64/frpc -c /usr/local/frp_0.54.0_linux_amd64/frpc.toml
[Install]
WantedBy=multi-user.target
```

## config

vim /usr/local/frp_0.54.0_linux_amd64/frpc.toml

```text
serverAddr = "94.103.4.41"
serverPort = 7090
auth.method = "token"
auth.token = "fejk$12A"

[[proxies]]
name = "wuhu1-tcp"
type = "tcp"
localIP = "127.0.0.1"
localPort = 10028
remotePort = 10028
```