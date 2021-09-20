# 发布和订阅

## 消息内容

|-|描述|举例|
|:--|:--|:--|
|topicName|标题|myhome/livingRoom/temp|
|Qos|服务等级|0|
|retianFlag|是否保留|true|
|Payload|消息内容|{"code": 500,"type": 3}|
|packet Id|只有Qos大于0的包才有|客户端或者broker来维护|
|dup flag|重复发送标签|-|


## 订阅

subscribe / unsubscribe
