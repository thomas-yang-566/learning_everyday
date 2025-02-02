## 类型

`https://dart.dev/language/built-in-types`

所有类型都是嘞，所有变量都指向对象引用(object reference)

1. Numbers(int, double)
2. Strings(String)
3. Booleans(bool)
4. Functions( Function)
5. List
6. Maps
7. Runes
8. Symbol
9. The value null( Null)


## Numbers 数字

int 整数, double 浮点, num 数字

abs(), ceil, floor, round, max, min

```dart
void main() {
  var i = 1;
  int j = 2;
  print("int i + j : ${i + j}");
  var d = 3.1;
  var ceiling = d.ceil();
  print("ceil d: ${d.ceil()}");
}
```

## 字符串

utf-16 序列, 可以单引号也可以双引号. ${表达式}

## Boolean

## symbol

实质上是 常量

## Records

`https://dart.dev/language/records`

匿名，不可变，聚集类型

```dart
var record = ('first', a: 2, b: true, 'last');

print(record.$1); // Prints 'first'
print(record.a); // Prints 2
print(record.b); // Prints true
print(record.$2); // Prints 'last'

(num, Object) pair = (42, 'a');
var first = pair.$1; // Static type `num`, runtime type `int`.
var second = pair.$2; // Static type `Object`, runtime type `String`.

// 多返回, Returns multiple values in a record:
(String name, int age) userInfo(Map<String, dynamic> json) {
return (json['name'] as String, json['age'] as int);
}

final json = <String, dynamic>{
'name': 'Dash',
'age': 10,
'color': 'blue',
};

// Destructures using a record pattern with positional fields:
var (name, age) = userInfo(json);

/* Equivalent to:
  var info = userInfo(json);
  var name = info.$1;
  var age  = info.$2;
*/

```

## collection 集合

`https://dart.dev/language/collections`

list, set 和 map

list / 有 add 方法 和 removeLast
```dart
var list = [1,2,3];
var vehicles = [
  'Car',
  'Boat',
  'Plane',
];
```

set

```dart
var elements = <String>{};
// Set<String> names = {};
elements.add("one");
```

## generics 通用类型

```dart
abstract class Cache<T> {
  T getByKey(String key);
  void setByKey(String key, T value);
}
```

## typedef

```dart
typedef IntList = List<int>;
IntList il = [1, 2, 3];

typedef Compare<T> = int Function(T a, T b);

// ----------- //
int sort(int a, int b) => a - b;

void main() {
  assert(sort is Compare<int>); // True!
}
```

## dart type system, 类型体系

dart 使用静态类型检查和运行时类型检查。可以早期发现类型相关的错误。