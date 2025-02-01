## stop

// debian 12.5 / mysql 8.0.x

sytemctl stop mysql

vim /root/temp/mysql-init
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNe1w@Pd22';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
UPDATE mysql.user SET plugin='mysql_native_password' WHERE User='root';
ALTER USER 'root'@'localhost' IDENTIFIED BY '';



```mysql
CREATE USER 'kucoin'@localhost IDENTIFIED BY 'fefeZf$ze4';
select user FROM mysql.user;
CREATE DATABASE kucoin;
GRANT ALL PRIVILEGES ON kucoin.* TO 'kucoin'@localhost;

CREATE USER 'douyou'@localhost IDENTIFIED  by 'fffeZf$ze4';
GRANT ALL PRIVILEGES ON douyou.* TO 'douyou'@localhost;
```

MyNe1w@Pd22

```mysql
CREATE USER nginx_ui@localhost IDENTIFIED BY 'fezf$aaQsa';
CREATE DATABASE nginx_ui;
GRANT ALL PRIVILEGES ON nginx_ui.* to 'nginx_ui'@localhost;
GRANT ALL PRIVILEGES ON nginx_ui.* TO 'nginx_ui'@'%' WITH GRANT OPTION;
```
