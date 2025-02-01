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


## maven 5 minutes 五分钟maven

```bash
$mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
$cd my-app
## 查看目录结构
$tree .
## 编译包
$mvn package
## 运行一下
$java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
## 输出 Hello World!
```

1. https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html


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


## goals

1. validate 验证项目是否正确且完整(validate the project is correct and all necessary information is available)
1. compile 编译项目代码
1. test 测试
1. package 打包 ,将编译好的的代码打包成可分发状态
1. integration-test 集成测试
1. verify 检查项目是否合法(valid) 并符合质量标准
1. install 安装到本地的 repo里，作为其他本地项目的依赖
1. deploy 部署
1. clean 清除中间产生的临时文件，比如一下jar文件
1. site 产生 site 文档
1. dependency:get 下载依赖

## phases

## mvn -h

```bash

mvn -h

usage: mvn [options] [<goal(s)>] [<phase(s)>]

Options:
 -am,--also-make                        If project list is specified, also
                                        build projects required by the
                                        list
 -amd,--also-make-dependents            If project list is specified, also
                                        build projects that depend on
                                        projects on the list
 -B,--batch-mode                        Run in non-interactive (batch)
                                        mode (disables output color)
 -b,--builder <arg>                     The id of the build strategy to
                                        use
 -C,--strict-checksums                  Fail the build if checksums don't
                                        match
 -c,--lax-checksums                     Warn if checksums don't match
    --color <arg>                       Defines the color mode of the
                                        output. Supported are 'auto',
                                        'always', 'never'.
 -cpu,--check-plugin-updates            Ineffective, only kept for
                                        backward compatibility
 -D,--define <arg>                      Define a system property
 -e,--errors                            Produce execution error messages
 -emp,--encrypt-master-password <arg>   Encrypt master security password
 -ep,--encrypt-password <arg>           Encrypt server password
 -f,--file <arg>                        Force the use of an alternate POM
                                        file (or directory with pom.xml)
 -fae,--fail-at-end                     Only fail the build afterwards;
                                        allow all non-impacted builds to
                                        continue
 -ff,--fail-fast                        Stop at first failure in
                                        reactorized builds
 -fn,--fail-never                       NEVER fail the build, regardless
                                        of project result
 -gs,--global-settings <arg>            Alternate path for the global
                                        settings file
 -gt,--global-toolchains <arg>          Alternate path for the global
                                        toolchains file
 -h,--help                              Display help information
 -l,--log-file <arg>                    Log file where all build output
                                        will go (disables output color)
 -llr,--legacy-local-repository         Use Maven 2 Legacy Local
                                        Repository behaviour, ie no use of
                                        _remote.repositories. Can also be
                                        activated by using
                                        -Dmaven.legacyLocalRepo=true
 -N,--non-recursive                     Do not recurse into sub-projects
 -npr,--no-plugin-registry              Ineffective, only kept for
                                        backward compatibility
 -npu,--no-plugin-updates               Ineffective, only kept for
                                        backward compatibility
 -nsu,--no-snapshot-updates             Suppress SNAPSHOT updates
 -ntp,--no-transfer-progress            Do not display transfer progress
                                        when downloading or uploading
 -o,--offline                           Work offline
 -P,--activate-profiles <arg>           Comma-delimited list of profiles
                                        to activate
 -pl,--projects <arg>                   Comma-delimited list of specified
                                        reactor projects to build instead
                                        of all projects. A project can be
                                        specified by [groupId]:artifactId
                                        or by its relative path
 -q,--quiet                             Quiet output - only show errors
 -rf,--resume-from <arg>                Resume reactor from specified
                                        project
 -s,--settings <arg>                    Alternate path for the user
                                        settings file
 -t,--toolchains <arg>                  Alternate path for the user
                                        toolchains file
 -T,--threads <arg>                     Thread count, for instance 2.0C
                                        where C is core multiplied
 -U,--update-snapshots                  Forces a check for missing
                                        releases and updated snapshots on
                                        remote repositories
 -up,--update-plugins                   Ineffective, only kept for
                                        backward compatibility
 -v,--version                           Display version information
 -V,--show-version                      Display version information
                                        WITHOUT stopping build
 -X,--debug                             Produce execution debug output
 ```

## 参考


1. https://maven.apache.org/
1. https://maven.apache.org/wrapper/
1. https://www.liaoxuefeng.com/wiki/1252599548343744/1305148057976866