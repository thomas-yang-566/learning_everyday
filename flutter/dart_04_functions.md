## functions 函数

`https://dart.dev/language/functions`

dart 是面对对象语言，因此函数也是对象，有类型: Function, 这意味着函数可以作为参数传递，也可以作为返回值，页可以赋给变量

```dart
bool isNoble(int atomicNumber) {
  return _nobleGases[atomicNumber] != null;
}

// 如果方法体只有一句，可
bool isNoble(int atomicNumber) => _nobleGases[atomicNumber] != null;
```

## params 参数

required positional parameters
named parameters
optional positional parameters

```dart
String say(String from, String msg, [String? device]) {
  var result = '$from says $msg';
  if (device != null) {
    result = '$result with a $device';
  }
  return result;
}
```

## main 函数

一个文件/项目 必须有一个main函数作为入口,可以传入参数

```dart
void main(List<String> args) {
  print(args);
}
```

执行 dart main.dart feature1

## 匿名函数

```dart
void main() {
  List<int> l = [1,2,4,8, 16];

  l.forEach(printElement);

  l.forEach((element) { // 匿名函数
    print("forEach|element: $element");
  });
}

```

## 变量有效范围

```dart
bool topLevel = true;

void main() {
  var insideMain = true;

  void myFunction() {
    var insideFunction = true;

    void nestedFunction() {
      var insideNestedFunction = true;

      assert(topLevel);
      assert(insideMain);
      assert(insideFunction);
      assert(insideNestedFunction);
    }
  }
}
```

## return value 返回值

所有函数都有返回值，如果没有return语句，函数会返回null

## 生成器 generators

```dart

```

## external functions

函数体在另外地方实现

