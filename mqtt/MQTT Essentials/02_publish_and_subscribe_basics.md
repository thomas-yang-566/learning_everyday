## pub/sub

publisher -> broker -> subscribe

## 解耦

1. 时空上 publisher 和 subscriber 不需要知道对方
1. 时间上， publisher 的消息 subscriber 可以晚点处理
1. 非同步执行，不会阻塞进程

## 扩展性 scalability

## 消息过滤

`不需要关心， mqtt 用第一种`

1. Subject-based filtering / 基于主题
1. Content-based filtering / 基于内容
1. Type-based filtering / 基于类型/事件过滤

## 消息
内容

1. 主题/ topic
2. 内容 payload / 字符串
3. 服务等级 / QoS level (0 ~ 2)
4. retainFlag
5. dupFlag

## 和传统消息队列的不同

传统消息队列可能有下面的特性

1. 未消费的消息会被存储，直到消费掉。
1. 消息只会被消费一次。
1. 队列/主题必须先创建

#
