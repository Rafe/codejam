import sys

def num_of_hackercup(line):
  target = {'h':0,'a':0,'c':0,'k':0,'e':0,'r':0,'u':0,'p':0}
  for c in line:
    if target.has_key(c.lower()):
      target[c.lower()] += 1

  target['c'] /= 2

  cap = sys.maxint
  for x in target.itervalues():
    if cap > x:
      cap = x
  return cap

if __name__ == "__main__":
  file = open("alphabet_soup.txt")
  file.readline()

  target=['h','a','c','k','e','r','c','u','p']

  case = 1
  for line in file:

    s = num_of_hackercup(line)
    
    print "Case #{0}: {1}".format(case,s)
    case += 1
