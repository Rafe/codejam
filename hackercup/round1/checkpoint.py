import sys
import math
from collections import defaultdict

def init_possible_steps():
  p = []
  r = 10000000
  w = 10000000
  h = 10000000
  possible_steps = defaultdict(int)
  possible_steps[1] = 1
  for i in range(w):
    p.append(1)

  flag = False
  for i in range(h):
    if flag == True: break
    for j in range(i,w):
      if i == j:
        p[j] *= 2
        if p[j] > r: 
          flag = True
          break
      else:
        p[j] += p[j - 1]
        if p[j] > r: continue
      if possible_steps[p[j]] == 0:
        possible_steps[p[j]] = i + j + 2
      else:
        possible_steps[p[j]] = min(possible_steps[p[j]], i + j + 2)
  #print possible_steps
  return possible_steps

def checkpoint(possible_paths,possible_steps):
  min_steps = 0
  i = 0
  while i <= possible_paths / 2 or i == 0:
    i += 1
    if possible_paths % i != 0:
      continue
    p = possible_paths / i
    if p in possible_steps and i in possible_steps:
      #print i,p
      s = possible_steps[i] + possible_steps[p]
      if min_steps == 0:
        min_steps = s
      else:
        min_steps = min(s,min_steps)

  return min_steps

  #1 calculate array with paths, min steps
  #2 dissemble paths with all possible combination, get min steps
  #divide paths and get combination

file = open("checkpoint.txt")

lines = file.readline()

case = 0
possible_steps = init_possible_steps()

for line in file:
  case += 1
  possible_paths = int(line)
  min_steps = checkpoint(possible_paths,possible_steps)
  print "Case #{0}: {1}".format(case,min_steps)
