# Getting started 开始

架构

1. flutter 框架和插件 (dart)
2. 引擎 (c++)
3. 嵌入平台(enbedder)


## flutter 框架和插件 (dart)

基础: 包含 UI， 组件(widgets), layout, 动画，手势 和基础模块

插件: json序列化，geo， 摄像头, in-app 支付

## ui theme

1. 使用 material 或者 cupertino 设计语言
2. widget 层， 交互
3. rendering 层， 绘制

## 需要设备

1. 电脑(最好是 mac, 不是也没有关系)
2. flutter sdk (flutter_macos_arm64_3.27.1-stable.zip @2025-Jan-11)
3. 编辑器 (android studio / vscode)
4. 至少一个移动设备，测试用
5. google / apple 开发者账号

## 安装 flutter

flutter.dev 下载，解压, flutter/bin 加入 PATH
然后执行

```bash
flutter help
flutter doctor ## 查看其他东西是否安装就绪
```

## 设置 ide

flutter 官方支持三种 IDE: android studio / Visual Studio Code 和 Emacs, 其他也可以

## hello

# android studio 创建 hello

plugin 安装 flutter

new flutter project -> hello

设备那里 选择 iOS Simulator , RUN

## hot reload