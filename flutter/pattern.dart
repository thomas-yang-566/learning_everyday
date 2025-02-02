void main() {

  var num = 5;

  switch(num) {
    case 1:
      print("num is 1");
    case 2:
    case 3:
      print("num is 3");
    case 4:
      print("num is 4");
    case 5 || 6 || 7:
      print("multi case, 5, 6,7");
      default:
        print("none of above.");
  }


  var numList = [1,2,4];
  var [a,b,c] = numList;
  print("a is: $a, b is: $b, c is: $c");
}