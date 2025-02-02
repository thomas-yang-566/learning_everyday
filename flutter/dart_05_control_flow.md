## loops 循环
`https://dart.dev/language/loops`

for

while / do while
break, continue

```dart
var message = StringBuffer('Dart is fun');
for (var i = 0; i < 5; i++) {
  if (i == 2) {
    continue; // 相等时，后面不会执行，下一个循环
  }
  
  if (i == 3) { // 到这里为止，循环终止
      break;
  }
  message.write('!');
}

// 没有 i, 不需要序号的时候
for (final candidate in candidates) {
  candidate.interview();
}


// 执行前验证是否为true
while (!isDone()) {
    doSomething();
}


// 先执行一次，验证条件为true 再执行，直到为false
do {
  doSomething();
} while (!ended());

```

## switch /case

```dart
switch (command) {
  case 'OPEN':
    executeOpen();
    continue newCase; // Continues executing at the newCase label.

  case 'DENIED': // Empty case falls through.
  case 'CLOSED':
    executeClosed(); // Runs for both DENIED and CLOSED,

  newCase:
  case 'PENDING':
    executeNowClosed(); // Runs for both OPEN and PENDING.
}
```

## 错误处理

