package main

import (
  "fmt"
)

type Fetcher interface {
  // Fetch returns the body of URL and
  // a slice of URLs found on that page.
  Fetch(url string) (body string, urls []string, err error)
}

// Crawl uses fetcher to recursively crawl
// pages starting with url, to a maximum of depth.
func Crawl(url string, depth int, fetcher Fetcher, c chan string) {
  // TODO: Fetch URLs in parallel.
  // TODO: Don't fetch the same URL twice.
  // This implementation doesn't do either:
  if depth <= 0 {
    return
  }
  body, urls, err := fetcher.Fetch(url)
  if err != nil {
    fmt.Println(err)
    c <- "error"
    return
  } else{
    c <- "found:" + url +" "+ body
  }
  for _, u := range urls {
    go Crawl(u, depth-1, fetcher, c)
  }
  return
}

func Handler(c chan string){
  //history := make(map[string]bool)
  select {
  case s := <-c:
    fmt.Println(s)

  }
}

func main() {
  c := make(chan string)
  go Crawl("http://golang.org/", 4, fetcher, c)
  Handler(c)
}


// fakeFetcher is Fetcher that returns canned results.
type fakeFetcher map[string]*fakeResult

type fakeResult struct {
  body string
  urls     []string
}

func (f *fakeFetcher) Fetch(url string) (string, []string, error) {
  if res, ok := (*f)[url]; ok {
    return res.body, res.urls, nil
  }
  return "", nil, fmt.Errorf("not found: %s", url)
}

// fetcher is a populated fakeFetcher.
var fetcher = &fakeFetcher{
  "http://golang.org/": &fakeResult{
    "The Go Programming Language",
    []string{
      "http://golang.org/pkg/",
      "http://golang.org/cmd/",
    },
  },
  "http://golang.org/pkg/": &fakeResult{
    "Packages",
    []string{
      "http://golang.org/",
      "http://golang.org/cmd/",
      "http://golang.org/pkg/fmt/",
      "http://golang.org/pkg/os/",
    },
  },
  "http://golang.org/pkg/fmt/": &fakeResult{
    "Package fmt",
    []string{
      "http://golang.org/",
      "http://golang.org/pkg/",
    },
  },
  "http://golang.org/pkg/os/": &fakeResult{
    "Package os",
    []string{
      "http://golang.org/",
      "http://golang.org/pkg/",
    },
  },
}
