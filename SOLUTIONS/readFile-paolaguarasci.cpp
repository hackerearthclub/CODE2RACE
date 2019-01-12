/*
This program takes the file path from the command line, reads it and returns the content to the video.
*/


#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
  if (argc != 2)
  {
    cout << "How to use: \n  $ ./rf [file]";
    return -1;
  }
  string filename = argv[1];
  ifstream file(filename);
  string line;
  while (file.eof() == 0)
  {
    getline(file, line);
    cout << line << endl;
  }
  return 0;
}
