2. 本章主要简述epoll的基础理论知识。方便理解libevent。

2.1 流 i/o 操作/堵塞

1. read时候没有数据
2. write时候已经写满了


解决方法

1. select (代收)
2. epoll


https://github.com/aceld/libevent/blob/master/21-%E6%B5%81-io.md