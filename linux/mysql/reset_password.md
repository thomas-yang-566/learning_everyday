## stop

// debian 12.5 / mysql 8.0.x

sytemctl stop mysql

vim /root/temp/mysql-init
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNe1w@Pass';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
UPDATE mysql.user SET plugin='mysql_native_password' WHERE User='root';
ALTER USER 'root'@'localhost' IDENTIFIED BY '';



```mysql
CREATE USER 'kucoin'@localhost IDENTIFIED BY 'fefeZf$ze4';
CREATE DATABASE kucoin;
GRANT ALL PRIVILEGES ON kucoin.* TO 'kucoin'@localhost;
```

