package main

import(
  "testing"
  //"fmt"
)

func TestCrawl(t *testing.T){
  fetcher := &fakeFetcher{
    "http://golang.org/" : &fakeResult{
      "The go programming language",
      []string{
        "http://test",
        "http://testw",
      },
    },
  }
  c := make(chan string)
  go Crawl("http://golang.org", 4, fetcher, c)
  Handler(c)
}
