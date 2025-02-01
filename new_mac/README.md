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
## 确认 php 版本
$php version
$redis-cli
## 输入 info server
```

### php 配置

```bash
## 安装 redis 扩展
$pecl install redis
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



### 杂项

```bash
$

## composer
$mkdir ~/temp
$cd ~/temp
## 安装 composer
$php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
$sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
## 安装好之后验证一下
$composer version
```

## phpmyadmin

```bash
$mkdir -p ~/web/default
$cd ~/web/default/
# 建立 phpinfo
# <?php phpinfo();
$vim index.php
$wget https://files.phpmyadmin.net/phpMyAdmin/5.1.1/phpMyAdmin-5.1.1-all-languages.tar.gz
$tar zxf phpMyAdmin-5.1.1-all-languages.tar.gz
## 改名，然后访问 http://localhost/pma
$mv phpMyAdmin-5.1.1-all-languages pma

```
