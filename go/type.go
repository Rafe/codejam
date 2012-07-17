package main

import (
  "fmt"
)

type Person struct {
  FirstName string
  LastName string
}

func (p *Person) FullName() string {
  return p.FirstName + " "+ p.LastName
}

func fake_main() {
  person := &Person{"John", "Smith"}
  fmt.Println(person.FullName())
}
