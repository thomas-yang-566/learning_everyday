## install/安装

install java

1. install https://www.tutorials24x7.com/java/how-to-install-java-17-on-mac
2. switch https://www.tutorials24x7.com/java/how-to-switch-java-version-on-mac

结果

```bash
java -version
java version "17.0.12" 2024-07-16 LTS
Java(TM) SE Runtime Environment (build 17.0.12+8-LTS-286)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.12+8-LTS-286, mixed mode, sharing)
```



## 内容

0. 程序入口 public class / public static void main(String[] args){}
1. 基本语法
1. 类名和文件名关系
1. 类型
1. 控制流程
1. 运算符, 运算优先级
1. 类型转换 (casting & type convertion)
2. 包
3. 引用包


## 类型,声明，初始化


### 8 primative types 原始类型



|类型|字节|范围|
|:---|:---|
|boolean|1|true / false|
| byte |1| -128 ~ 127| 
|char|2|字符|
|short| 2| -32k ~ 32k|
|int|4| -2b ~ 2b|
|long|8|-|
|float|4|-|
|double|8|-|


```java

package com.codewithmosh;

import java.util.Date;

public class Main {
	public static void main(String[] args) {
		byte age = 30;
		Date now = new Date();
	}
}

```

### reference types 引用类型, 类

值存储，变量指针

```java

package com.codewithmosh;


imort java.awt.*;

public class MainRef {
	public static void main(String[] args) {
		Point p1 = new Point(1,1);

	}
}


```


## 数组

数组大小固定，如果需要用可变长度，可以用 collection



## 常量

```java

final flaot pi = 3.1415924F;
```