# a beginners guide to linux firewall (2021)

## key terms (关键概念)

1. bash unix shell
2. NetFilter (linux内核的网络框架)
3. iptables (user-space utility program)
4. ufw un-complicated tool to managing NetFilter
5. VirtualMachine


## difference of ufw, iptables

1. iptables is flexible and complex firewall tool.
2. ufw is base on iptables, simplify

## install

```bash
$sudo apt install ufw
$ufw --help

Commands:
  enable
  disable
  default ARG
  logging LEVEL
  allow ARGS
  deny ARGS
  reject ARGS
  limit ARGS
  delete RULE|NUM
  insert NUM RULE
  prepend RULE // 前置规则 预先考虑，预谋
  route RULE
  route delete RULE|NUM
  route insert NUM RULE
  reload : reload firewall
  reset reset firewall,删除所有的规则
  status show firewall status / and rules
  status numbered ## show firewall status as numbered list of rules
  version
  
application profile command
   app list
   app info PROFILE
   app update PROFILE
   app default ARG
```

## basic commands

```bash
#ufw enable // 启用
#ufw allow 8080/tcp
#ufw status numbered
#ufw delete number
```

## port forwarding

##
```bash
ufw allow proto tcp from any to 172.104.61.139 port 80
ufw allow proto tcp from any to 172.104.61.139 port 443
```
*nat
:PREROUTING ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8081 -j REDIRECT --to-port 8080
-A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 172.104.61.139:80
-A PREROUTING -p tcp --dport 443 -j DNAT --to-destination 172.104.61.139:443
-A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 172.104.61.139
COMMIT

-A OUTPUT -p tcp --match multiport ! --dports 12345,1080 -j DNAT --to-destination 127.0.0.1:12345
-A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 172.104.61.139:80

-A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 172.104.61.139:80
-A PREROUTING -p tcp --dport 443 -j DNAT --to-destination 172.104.61.139:443

*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -i eth0 -d 2xx.2xx.1xx.0 -p tcp --dport 80 -j DNAT --to-destination 1xx.1xx.2xx.0:8080
# setup routing
-A POSTROUTING -s 1xx.1xx.2xx.0/24 ! -d 1xx.1xx.2xx.0/24 -j MASQUERADE
COMMIT

cdnmaster: 139.162.52.92 (linode)
cdn1: 172.104.61.139:80 (linode)

*nat
:PREROUTING ACCEPT [0:0]
# forward 202.54.1.1  port 80 to 192.168.1.100:80
# forward 202.54.1.1  port 443 to 192.168.1.100:443
-A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:80
-A PREROUTING -i eth0 -d 202.54.1.1   -p tcp --dport 443 -j  DNAT --to-destination 192.168.1.100:443
# setup routing
-A POSTROUTING -s 192.168.1.0/24 ! -d 192.168.1.0/24 -j MASQUERADE
COMMIT

configure arguments: --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-AoTv4W/nginx-1.22.1=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=stderr --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_secure_link_module --with-http_sub_module --with-mail_ssl_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-stream_realip_module --with-http_geoip_module=dynamic --with-http_image_filter_module=dynamic --with-http_perl_module=dynamic --with-http_xslt_module=dynamic --with-mail=dynamic
--with-stream=dynamic --with-stream_geoip_module=dynamic