## Retained / 保留

每个 topic 保留一个。

配置

```ini
; /etc/emqx/emqx.conf
mqtt.retain_available = true | false
```

## shared subscription / 分组

一条消息只一个 subscriber 处理。

topic 1
分组: abc 组 一起监听 主题 1
$share/abc/1

不分组

$queue/1


https://docs.emqx.io/en/broker/v4.3/advanced/shared-subscriptions.html

## 延迟 delay publish

## Proxy Subscription

## Bridge 桥接

## Topic Rewrite 消息重写

主题换一换 (基本用不到)
```ini
module.rewrite = off|on

module.rewrite.rule.1 = y/+/z/# ^y/(.+)/z/(.+)$ y/z/$2
module.rewrite.rule.2 = x/# ^x/y/(.+)$ z/y/x/$1
module.rewrite.rule.3 = x/y/+ ^x/y/(\d+)$ z/y/$1
```

## $SYS 系统消息

https://docs.emqx.io/en/broker/v4.3/advanced/system-topic.html


client online and offline events

```ini
## 客户端
${clientid}/connected
${clientid}/disconnected

## 统计
$SYS/brokers/${node}/stats/
```

## 黑名单
https://docs.emqx.io/en/broker/v4.3/advanced/blacklist.html

## hook & webhook , web 钩子


https://docs.emqx.io/en/broker/v4.3/advanced/webhook.html

## 分布式集群

先不深入

https://docs.emqx.io/en/broker/v4.3/advanced/cluster.html


## Metric 指标

先不管

## rate limit , 限速

先不管










1
