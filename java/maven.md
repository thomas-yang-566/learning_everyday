# maven , maven wrapper 是什么

管理java 的依赖 pom.xml (pom = project object model 项目对象模型) ,支持 java1.7 以上版本

https://www.liaoxuefeng.com/wiki/1252599548343744/1305148057976866

## 下载和安装

```bash
### 目前版本 3.8
$wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz 
$tar zxf apache-maven-3.8.6-bin.tar.gz 
$sudo mv apache-maven-3.8.6 /opt/
$sudo ln -sfn /opt/apache-maven-3.8.6 /opt/apache-maven
### add /opt/apache-maven/bin to $PATH
$vim  ~/.zshrc
$source ~/.zshrc
$mvn -v

```

## 使用

```bash

$mvn -h
$mvn verify
```

## 配置

1. 环境变量 MAVEN_OPTS / MAVEN_ARGS  会在执行 mvn 命令是传给 java
2. $HOME/.m2 配置目录
3. 项目目录下 .mvn 目录
4. maven 3.3.1 之后命令行传参数太难了，因此有了 .mvn/maven.config 文件来配置
5. .mvn/jvm.config


## ide 集成

https://www.jetbrains.com/idea/help/maven.html


## mvnw

mvnw = maven wrapper

通常使用 mvn时会使用系统安装的mvn版本，合作的不同开发会使用不同的mvn， 而在项目根目录增加mvnw 可以统一mvn版本

### 初始化

```bash
$cd project_dir
$mvn wrawpper:wrapper

```

## 参考


1. https://maven.apache.org/
1. https://maven.apache.org/wrapper/
1. https://www.liaoxuefeng.com/wiki/1252599548343744/1305148057976866