package main

import (
  "testing"
)

func TestCalculate_PI(t *testing.T ) {
  result := make(chan Object)
  go CalculatePI(2000, result)
  sum := <-result
  PI := float64(sum.(int)) * 4 / 2000
  if PI > 3.5 {
    t.Error("Calculation Error!!")
  }
}

func buildChannel(in chan Object, a int, b int) {
  for i := 0; i < b; i++ {
    in <- a
  }
  close(in)
}

func TestCollectPI(t * testing.T){
  result := make(chan Object)
  go buildChannel(result, 10, 10)
  sum := CollectPI(result).(int)
  if sum != 100 {
    t.Error("Calculation Error!!")
  }
}
