package main

import (
  "fmt"
  "math"
)

type Abser interface {
  Abs() float64
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
  if f < 0 {
    return float64(-f)
  }
  return float64(f)
}

type Vertex struct {
  X, Y float64
}

func (v *Vertex) Abs() float64 {
  return math.Sqrt(v.X*v.X + v.Y*v.Y)
}


func add(a, b int) int{
  return a + b
}

func swap(a, b string) (string, string){
  return b, a
}

type Point struct{
  x int
  y int
}

func mmain(){
  fmt.Println("Hello world!! %f", math.Pi)
  fmt.Println(add(1, 2))

  var sum int = 0
  for sum < 1000 {
    sum += 10
  }
  fmt.Println(sum)

  s := []int{1,2,3,4,5}

  fmt.Println(s)

  var a Abser
  f := MyFloat(-math.Sqrt2)
  v := Vertex{3, 4}

  a = f  // a MyFloat implements Abser
  a = &v // a *Vertex implements Abser
  //a = v  // a Vertex, does NOT
         // implement Abser

  fmt.Println(a.Abs())

  op := makeAdd()
  fmt.Println(op(1,2))
}

type operator func(x,y int) int

func makeAdd() operator{
  return func(x,y int) int{
    return x + y
  }
}
