import 'dart:io';

void main() {
  print("enter string");
  String str = stdin.readLineSync(encoding: Encoding.UTF_8);
  int i, j = 0;
  int ascii = 1;
  for (i = 0; i < str.length; i++) {
    j = int.parse(str[i]);
    ascii = ascii * j;
  }
  print("product of ascii values=" + ascii);
}
