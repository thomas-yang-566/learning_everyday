
void main() {
  var i = 1;
  int j = 2;
  print("int i + j : ${i + j}");
  var d = 3.1;
  var ceiling = d.ceil();
  print("ceil d: ${d.ceil()}");
  print('single ceil d: ${d.ceil()}');

  var list = [1,2,3,4];
  print("list length: ${list.length}");
  // list.forEach( (item) => {
  //   print("item list@ is: ${item}");
  // });
  list.add(6);
  // list.add("1f");
  print("list: ${list}");

  var li = <int>[];
  li.add(1);
  li.add(2);
  li.add(3);
  li.add(5);
  li.add(8);

  printints(li);

}

void printints(List<int> a) => print(a);