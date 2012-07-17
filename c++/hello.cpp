#include <iostream>
#include "hello.h"

void Hello::hello() {
  std::cout << "hello world" << std::endl;
};

int main() {

  Hello h;

  h.hello();

  return 0;
}
