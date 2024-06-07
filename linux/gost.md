## gost 代理

help
```bash
$gost -h
Usage of gost:
  -C string
    	configure file 配置文件
  -D	enable debug log  debug日志文件
  -F value
    	forward address, can make a forward chain ## 转发
  -I string
    	Interface to bind 绑定网卡
  -L value
    	listen address, can listen on multiple ports (required) //  监听(必填)
  -M int
    	Specify out connection mark 链接标识
  -V	print version
  -obfs4-distBias
    	Enable obfs4 using ScrambleSuit style table generation
```

## 简单代理 http ,sock5


```bash
## http proxy 
## server 1, 172.104.61.139
$gost -L http://:8081

## server2/machine 2
$curl https://httpbin.org/ip
$curl -x "http://cdn1.4cdn.xyz:8081" https://httpbin.org/ip
$curl -x "cdn1.4cdn.xyz:8081" https://httpbin.org/ip

###### ------- ============ ----------
## server1
$gost -L socks5://:8082
## 也可以同时开多个监听 gost -L http://:8081  -L socks5://:8082
## server2:
curl -x "socks5://cdn1.4cdn.xyz:8082" https://httpbin.org/ip
```

```bash```

## 转发

client -> server1 -> server2
```bash
## server2: bwg.4cdn.xyz
$gost -L socks5://:8081

## server1 cdn1.4cdn.xyz
$gost -L socks5://:8090 -F socks5://bwg.4cdn.xyz:8081

## client
$curl -x "socks5://cdn1.4cdn.xyz:8090" https://httpbin.org/ip
$curl -x "socks5://localhost:1080" https://httpbin.org/ip

```


```bash

$gost -L :8000 -F ss://AEAD_CHACHA20_POLY1305:jack1234@:8338
## -L 监听端口
## -F 
## ss: shadowsocks, 
```

## ss 代理

```bash
## 密码为 w0rd2019, 端口 8001
$gost -L ss://aes-256-gcm:w0rd2019@:8001
```


gost -L :8080 -F relay://username:password@:12345?nodelay=false


## wss
```bash
gost -L http://:8080 -F "wss://:8443?keepalive=true&ttl=15s"
gost -L relay+wss://jack:w0rd2019@:8443
gost -L relay://username:password@:12345
```
### 协议


### 参考

1. https://oxylabs.io/blog/curl-with-proxy