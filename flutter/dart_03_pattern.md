## 模式

`https://dart.dev/language/patterns`

什么是 pattern



## matching/匹配

```dart
switch (number) {
  case 1:
    print("one");
    case [2, 3, 4]:
      print("two to four");
}
```


## destructuring/分解

```dart
var numList = [1,2,4];
var [a,b,c] = numList;
print("a is: $a, b is: $b, c is: $c");
```