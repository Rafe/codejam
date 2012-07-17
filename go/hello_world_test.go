package main

import (
  "testing"
  "fmt"
)

func TestAdd(test *testing.T) {
  var in, out = 9, 3
  if x := add(in, out); x != 12 {
    test.Errorf("Sqrt(%v) = %v, want %v", in, x, out)
  }
}

func ExampleFoo() {
  fmt.Printf("hello")
  // Output:
  //hello
}
