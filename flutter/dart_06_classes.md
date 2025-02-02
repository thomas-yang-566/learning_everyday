##

dart 基于类(class) 和 mixin(混入)机制, 除了 null 之外所有的类都是 Object 的子/孙类

## 类

`https://dart.dev/language/classes`


```dart
class Point {
  double? x; // 可空(nullable)
  double? y;// 可空(nullable)
  double z = 0; // 有默认值
}
```

## 隐含定义接口 implicit interfaces

```dart
// A person. The implicit interface contains greet().
class Person {
  // In the interface, but visible only in this library.
  final String _name;

  // Not in the interface, since this is a constructor.
  Person(this._name);

  // In the interface.
  String greet(String who) => 'Hello, $who. I am $_name.';
}

// An implementation of the Person interface.
class Impostor implements Person {
  String get _name => '';

  String greet(String who) => 'Hi $who. Do you know who I am?';
}

String greetBob(Person person) => person.greet('Bob');


void main() {
  print(greetBob(Person('Kathy')));
  print(greetBob(Impostor()));
}
```

## 静态方法和常量

```dart
class Queue {
  static const initialCapacity = 16; // 静态常量
  // ···

  static double distance() { // 静态函数
    return 0.1;
  }
}

void main() {
  assert(Queue.initialCapacity == 16);
}

```