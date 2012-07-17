package main

import "fmt"

func counter(id int, channel chan int, closer bool) {
  x:= 0
  for i := 0; i < 100000000; i++ {
    // send count data to channel
    //fmt.Println("Thread", id, "send", i)
    x += i
  }
  channel <- x
  if closer { close(channel ) }
}

func a_main() {
  channel := make(chan int, 10)
  go counter(1, channel, false)
  go counter(2, channel, true)

  x := 0
  // receiving data from channel
  for i := range channel {
    //fmt.Println("receiving")
    x += i
  }

  fmt.Println(x)
}
