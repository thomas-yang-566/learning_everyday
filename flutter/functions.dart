void main() {
  print("functions");
  print("isNobleGas(3): ${isNobleGas(2)}");
  print("isNobleGas(8): ${isNobleGas(8)}");

  List<int> l = [1,2,4,8, 16];

  l.forEach(printElement);

  l.forEach((element) { // 匿名函数
    print("forEach|element: $element");
  });
}

var _nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon'
};

isNobleGas(int atomicNumber) {
  return _nobleGases[atomicNumber] != null; //atomicNumber == 2 || atomicNumber == 10 || atomicNumber == 18;
}

void printElement(int element) {
  print("element: $element");
}