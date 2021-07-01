# 认证

内置认证 Mnesia / username/ clientid 认证

开关

```conf
## /etc/emqx/emqx.conf
## 设置为 false
allow_anonymous = false
```

## 扩展认证方式

1. ldap
1. mysql / postgreSQL / mongodb
1. redis


## redis

config
/etc/emqx/plugins/emqx_auth_redis.conf

```conf
auth.redis.pool = 8
auth.redis.database = 0
auth.redis.password =
```
