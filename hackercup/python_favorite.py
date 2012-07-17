import os
from multiprocessing import Process

def into(title):
  print title
  print "parant process", os.getppid()
  print "process id", os.getpid()

def f(name):
  into("function f")
  print 'hello', name

if __name__ == "__main__":
  into('main')

  p = Process(target = f, args = ('world',))
  p.start()
  p.join()
