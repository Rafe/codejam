import math

def recover_sequence(n,seq):
  l = [x for x in range(1,n + 1)]
  r = recover_merge(l,seq)
  #print r
  ans = [0 for x in range(n)]
  for x in range(n):
    ans[r[x]-1] = x + 1  
  #print ans
  return checksum(ans)

def recover_merge(l,seq):

  if len(l) <= 1:
    return l

  mid = int(math.floor(len(l) / 2))

  first = recover_merge(l[:mid],seq)
  last = recover_merge(l[mid:],seq) 

  return recover(first,last,seq)

def recover(first,last,seq):
  r = []
  while len(first) > 0 and len(last) > 0 and len(seq) > 0:
    s = int(seq.pop(0))
    if(s) == 1:
      r.append(first.pop(0))
    if(s) == 2:
      r.append(last.pop(0))
  return r + first + last

def checksum(arr):
  result = 1
  for i in range(len(arr)):
    result = (31 * result + arr[i]) % 1000003

  return result

file = open("recover_the_sequence.txt")

lines = int(file.readline())

for case in range(lines):
  n = int(file.readline())
  seq = [x for x in file.readline().strip("\n")]
  ans = recover_sequence(n,seq)
  print "Case #{0}: {1}".format(case + 1,ans)
