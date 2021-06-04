# 新 mac 设置

1. brew
1. atom
1. golang
1. mysql + redis
1. php@7.4 + nginx
1. phpmyadmin

`## 开头为注释`

## brew

```bash
## 安装
$/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
## https://mirrors.cloud.tencent.com/help/homebrew.html

```



## golang AND atom AND etc


```bash
$brew install --cask chromium
$brew install go wget curl
$go version
$brew install --cask atom
```

## mysql + redis + nginx + php@7.4-fpm

```bash
$brew install mysql redis nginx php@7.4
$brew install redis

## 列出所有服务
$brew services
$brew services start redis
$brew services start mysql

```

### php 配置

```bash
$vim /usr/local/etc/php/7.4/php-fpm.d/www.conf
// listen = 127.0.0.1:9074
// user = myName (用户名)
// group = staff
```

```bash
$cd /usr/local/nginx/
$vim nginx
## user myName staff
## vhosts/*.conf

```



###

## phpmyadmin

```
$wget https://files.phpmyadmin.net/phpMyAdmin/5.1.1/phpMyAdmin-5.1.1-all-languages.tar.gz

```
