## keywords 关键字

59个
```text
abstract , as , assert, async await
base, break
case, catch, class , const, continue, covariant
default, deferred, do, dynamic
else, enum, export, extends, extension, external
factory, false, final, finally, for, Function
get
hide
if, implements, import, in, interface, is
late, library
mixin, new, null
of, on, operator
part
required, rethrow, return
sealed, set, show, static, super, switch, sync
this, throw, true, try, type typedef
var void, 
when, with, while
yield
```

## 变量和常量

`https://dart.dev/language/variables`
type safe
变量 var 自动推断, late 消除 runtime errors/ lazy init

常量: final 只能赋值一次。 const 常量

```dart
// var 编译器推断类型
var name1 = 'Bob';

// 指定类型
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

`运算符 https://dart.dev/language/operators`


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
11. assignment 赋值 = *= /= += -=(...)


```dart
// dart operators.dart
// ## 数学运算/ arithmetic operators
// + 加 - 减 * 乘 / 除 % 去模(modulo) ~/(除法取整)
asser(2 + 3 == 5);
```

## 注释
单行和多行, [] 包含内容会指向被引用对象
```dart
// TODO 这是单行
/*
 这也是, 多行
*/
```

## metadata 元数据

`metadata https://dart.dev/language/metadata`

以 @开头的注解, 编译时常量或者常量构造器(constant constructor) 

1. Deprecated (已弃用),意味着它仍然可用，但不推荐使用，通常是因为有更好的替代方案。将来版本中可能移除
1. Override(重写),通过重写，子类可以提供与父类不同的实现 (通常给 ide 的代码提示，避免拼写错误)
1. progma(编译指令),它通常用于控制编译器的行为，例如优化、警告或特定平台的行为。
```dart
class Television {
  /// Use [turnOn] to turn the power on instead.
  @Deprecated('Use turnOn instead')
  void activate() {
    turnOn();
  }

  /// Turns the TV's power on.
  void turnOn() {
    // do something
  }
  // ···
}
```

也可以自定义 注解

```dart
class Todo {
  final String who;
  final String what;

  const Todo(this.who, this.what);
}

// 指向上面的类的常量构造器
@Todo('Dash', 'Implement this function')
void doSomething() {
  print('Do something');
}
```

## libraries & import 引用和库

`https://dart.dev/language/libraries`

import 'URI';
```dart
// 三种形式
import 'dart:math'; // core libraries 核心库
import 'package:test/test.dart'; // external package 外部包
import 'path/to/other_file.dart'; // 引用文件
import 'path/to/helper.dart' as lib; // 如果 helper.dart里类名和其他引用的有冲突,引用文件

// 部分引用
// Import only foo. 
import 'package:lib1/lib1.dart' show foo;

// Import all names EXCEPT foo.
import 'package:lib2/lib2.dart' hide foo;
// lazy import
import 'package:greetings/hello.dart' deferred as hello;

```

如何创建自己的库 `https://dart.dev/tools/pub/create-packages`
