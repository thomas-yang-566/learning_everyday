# 本章内容摘要

1. go代码组织形式
1. 使用 go 命令
1. 使用 go 开发者工具
1. 如何和其它go开发者合作

## 包

文件夹名 / 父名 / github.com 等网络名


### main 包

go install 用
必须包含main函数


## import

内置包,本地和远程包

搜索路径 $GOPATH

```golang
import "package1"

import (
  "package3"
  "package4"
  AliasName "realPackgeName"
  _ "blankPackage"
)

```

### 远程 引用 (remote import)


### init function

package 目录下，每个文件最都可以有，每个都会执行, 执行顺序不定

如果 A 包 引用了 B 包
