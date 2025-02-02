void main() {
  print("functions");
  print("isNobleGas(3): ${isNobleGas(2)}");
  print("isNobleGas(8): ${isNobleGas(8)}");
}

var _nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon'
};

bool isNobleGas(int atomicNumber) {
  return _nobleGases[atomicNumber] != null; //atomicNumber == 2 || atomicNumber == 10 || atomicNumber == 18;
}