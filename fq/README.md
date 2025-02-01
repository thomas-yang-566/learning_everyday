# 科学上网

## 0. 准备



1. 你家有别的 有网卡的电脑吗？
2. 路由器什么牌子，型号？
3. 是路由器拨号还是光猫拨号
4. 是否有宽带的用户名密码？
5. 一条网线/ 8根线都要通的
6. 一个无线路由器(后期调整为 AP模式，作为wifi 连接用，不拨号)

## r2s/R4S固件下载和烧录

下载地址

1. https://github.com.cnpmjs.org/DHDAXCW/NanoPi-R4S-2021

烧录(写入) 软件

https://www.balena.io/etcher/


## 网口

NanoPi-R4S拥有一个全球唯一的Mac地址，默认分配给Cpu内置的以太网卡(rtl8211e)，接口名为eth0，该以太网口在PCB上的标注为LAN2，在外壳标注为WAN，在FriendlyWrt系统下默认已分配给WAN口。


## 主路由模式

https://www.right.com.cn/forum/thread-4104155-1-1.html
