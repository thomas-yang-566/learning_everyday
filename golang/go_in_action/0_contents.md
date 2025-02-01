# 目录

1. 介绍
1. 通常介绍
1. 包的概念，以及包的组织
1. 内建数据类型接受
1. 类型系统/类 (type system)
1. 深入 go scheduler, concurrency 和 channel
1. 深化上一章
1. 标准库(log, json, io)
1. 测试和基准性能测试/ testing and benchmark


## 安装

https://golang.org/dl/ 任君选择

1. 直接下载对应包, 解压，将 bin/  放到 $PATH 里
1. 下载对应 pkg / deb/ rpm 安装
1. snapcraft.io/go / 适合于linux

## 命令

```bash
$go help
Go is a tool for managing Go source code.

Usage:

	go <command> [arguments]

The commands are:

	bug         start a bug report ## 报告bug，基本用不到
	build       compile packages and dependencies ## 将源码编译成执行二进制码
	clean       remove object files and cached files ## 删除编译产生的中间文件
	doc         show documentation for package or symbol ## 显示文档 / go.dev
	env         print Go environment information ## 打印默认环境变量
	fix         update packages to use new APIs ## 不知道怎么用
	fmt         gofmt (reformat) package sources ## 自动格式化代码 = gofmt / fmt = format /
	generate    generate Go files by processing source ## 不会用
	get         add dependencies to current module and install them ## 下载go包
	install     compile and install packages and dependencies ## 安装 go包
	list        list packages or modules ##
	mod         module maintenance ## 模块管理
	run         compile and run Go program ## 直接执行
	test        test packages ## 测试
	tool        run specified go tool ## 工具
	version     print Go version ## 显示版本
	vet         report likely mistakes in packages

Use "go help <command>" for more information about a command.

Additional help topics:

	buildconstraint build constraints
	buildmode       build modes
	c               calling between Go and C
	cache           build and test caching
	environment     environment variables
	filetype        file types
	go.mod          the go.mod file
	gopath          GOPATH environment variable
	gopath-get      legacy GOPATH go get
	goproxy         module proxy protocol
	importpath      import path syntax
	modules         modules, module versions, and more
	module-get      module-aware go get
	module-auth     module authentication using go.sum
	packages        package lists and patterns
	private         configuration for downloading non-public code
	testflag        testing flags
	testfunc        testing functions
	vcs             controlling version control with GOVCS

Use "go help <topic>" for more information about that topic.
```
