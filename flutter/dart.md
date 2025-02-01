## 安装

https://dart.dev/get-dart

如果安装了 flutter，那么就已经有了

```bash
$dart --help
A command-line utility for Dart development.

Usage: dart <command|dart-file> [arguments]

Global options:
-v, --verbose               Show additional command output.
    --version               Print the Dart SDK version.
    --enable-analytics      Enable analytics.
    --disable-analytics     Disable analytics.
    --suppress-analytics    Disallow analytics for this `dart *` run without changing the analytics configuration.
-h, --help                  Print this usage information.

Available commands:
  analyze    Analyze Dart code in a directory.
  compile    Compile Dart to various formats.
  create     Create a new Dart project.
  devtools   Open DevTools (optionally connecting to an existing application).
  doc        Generate API documentation for Dart projects.
  fix        Apply automated fixes to Dart source code.
  format     Idiomatically format Dart source code.
  info       Show diagnostic information about the installed tooling.
  pub        Work with packages.
  run        Run a Dart program.
  test       Run tests for a project.

Run "dart help <command>" for more information about a command.
See https://dart.dev/tools/dart-tool for detailed documentation.
```



## hello world

```dart
## main.dart
void main() {
    print('hello dart');
}
```

```bash
## 运行
$dart main.dart

## 编译
$dart compile exe main.dart -o bin/hello
$./bin/hello
```

## 变量

`https://dart.dev/language/variables`
type safe 
var 自动推断, late 消除 runtime errors/ lazy init

```dart
var name1 = 'Bob';
String name2 = 'Bob_too';

int? age = 12; // nullable 
```

late/ 2 lazy

```dart
// This is the program's only call to readThermometer().
// 如果没有用到 temerature, readThermometer 就不会被调用
late String temperature = readThermometer(); // Lazily initialized.
```

## 运算

https://dart.dev/language/operators

1. unary postfix(单目后运算符) ++/ --
2. unary prefix(弹幕前运算符)
3. 乘法 * / % ~/
4. 加法 + -
5. 位移 << / >> , >>>
6. 位运算 和(&) , XOR (^), OR(|)
7. 关系运算符 == != > < >= <=
8. 类型 as is , is!
9. 逻辑运算符 并且&&,或 || , if-null ??
10. 三元运算符 expr1 ? expr2 : expr3
11. 

```dart

```

## 控制流

if / for / while / switch / case / break / continue assert

assert 是开发中使用， 如果 assert 里的变量是 false，则会停止执行 / production 模式中会被忽略(不用移除)

```dart
assert(urlString.startsWith('https'),
    'URL ($urlString) should start with "https".');
```

if / for / while
```dart

if (year > 2001) {
    print('21 century');
} else {
    print('not yet');
}

for (final object in flybyObjects) {
    print('object');
}

for (int month = 1; month <= 12; month++) {
    print(month);
}

while ( year < 2016) {
    year += 1;
}

try {
    breadMoreLlamas();
} on OutOfLlamasException {
    buyMoreLlamas();
} on OtherExpcetion {
    // do other thing.
} catch(e) {
    // finally
    print('Something really unknown: $e');
}

```

## functions 方法

```dart
int fibonacci(int n) {
    if (n == 0 || n == 1) {
        return n;
    }
    
    return fibonacci(n-1) + fibonacci(n-2);
}
```

## 注释

```dart
// TODO 这
/*
 这也是
*/
```

## import 引入

```dart

import 'dart:math'; // core libraries 核心库
import 'package:test/test.dart'; // external package 外部包
import 'path/to/other_file.dart'; // 引用文件
```

## classes 类

```dart
class SpaceCraft {
    String name;
    DateTime? launchDate;
    int? get launchYear => launchDate?.year;
    
    SpaceCraft(this.name, this.launchDate) {
    }
    
    SpaceCraft.unlaunched(String name): this(name, null);
}
```