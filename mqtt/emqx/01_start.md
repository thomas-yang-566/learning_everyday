## 安装和配置

### debian

```bash
$sudo apt update && sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
$curl -fsSL https://repos.emqx.io/gpg.pub | sudo apt-key add -
$sudo apt-key fingerprint 3E640D53
$sudo add-apt-repository "deb [arch=amd64] https://repos.emqx.io/emqx-ce/deb/debian/ ./$(lsb_release -cs) stable"
$sudo apt update
$sudo apt install emqx
$sudo systemctl start emqx
$sudo systemctl enable emqx
```

### macos

```bash
$brew tap emqx/emqx
$brew install emqx
```


## 配置

### 基础

`debian`
1. /etc/emqx/emqx.conf 主配置文件
1. /etc/emqx/acl.conf 默认访问控制文件
1. /etc/emqx/plugins/*.conf 插件配置

基本格式

```ini
mqtt.max_packet_size = 1MB
```


### Listener 监听进程

|name|port|desc|
|:---|:---|:---|
|tcp listener|1883|MQTT/TCP protocol port|
|tcp listener|11883|MQTT/TCP Protocol internal port, only used for local client connection|
|ssl listener|8883|MQTT/SSL protocol port|
|websocket listener|8083|MQTT/WS protocol port|
|secure websocket listener|8084|MQTT/WSS protocol port|



redis

## 参考
https://docs.emqx.io/en/broker/v4.3/getting-started/install.html
