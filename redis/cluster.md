## ubuntu

# add redis-6380 , redis-6381 , redis-6382 dir

## start

```bash
### start redis instance
$cd redis-6380
$nohup redis-server ./redis.conf
$cd redis-6381
$nohup redis-server ./redis.conf
$cd redis-6382
$nohup redis-server ./redis.conf

## create cluster

redis-cli --cluster create 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384  127.0.0.1:6385 --cluster-replicas 1
```



https://redis.io/docs/manual/scaling/

https://www.cnblogs.com/Yunya-Cnblogs/p/14608937.html
