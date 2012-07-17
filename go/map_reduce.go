package main

import (
  "fmt"
  "math/rand"
)

type Object interface {}

func MapReduce(input chan Object,
               mapper func(Object, chan Object),
               reducer func(chan Object) Object,
               pool_size int) Object {

    worker_outputs := make(chan chan Object, pool_size)
    go func() {
      //read input, assign input to mapper(item, output)
      for item := range input {
          worker_output := make(chan Object)
          worker_outputs <- worker_output
          go mapper(item, worker_output)
      }
      close(worker_outputs)
    }()

    reduce_input := make(chan Object)
    go func() {
      //listening worker_outputs as reduce_input
      for worker := range worker_outputs {
          reduce_input <- (<-worker)
      }
      close(reduce_input)
    }()

    return reducer(reduce_input)
}

func CalculatePI(n Object, c chan Object) {
  sum := 0
  for i := 0; i < n.(int); i++ {
    x := rand.Float64()
    y := rand.Float64()
    if (x * x + y * y ) <= 1.0 {
      sum += 1
    }
  }
  c <- sum
  close(c)
}

func CollectPI(in chan Object) Object {
  sum := 0
  for i := range in {
    sum += i.(int)
  }
  return sum
}

func main() {
  input := make(chan Object)
  go func(){
    for i := 0; i < 20000; i++ {
      input <- 20000
    }
    close(input)
  }()
  points_in_circle := MapReduce(input, CalculatePI, CollectPI, 10).(int)
  result := float64(points_in_circle) * 4 / (20000 * 20000 )
  fmt.Println(result)
}
