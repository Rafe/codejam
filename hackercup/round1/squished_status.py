#1 dynamic calculate

def decode_status(m , status):
  result = []
  for n in range(len(status)):
    s = 0
    #chop last 1,2,3 digits, if > m add cases
    for i in range(3):
      if i > n:
        break
      t = status[n-i:n+1]
      code = int(t)
      if code <= m and code > 0 and t[0] != "0":
        if n == i:
          s += 1
        if n > i:
          s += result[n-i-1]
    if s == 0: #decode failed
      return 0
    result.append(s)
    #print result

  return result[-1]

file = open("squished_status.txt")

lines = int(file.readline())

for case in range(lines):
  params = file.readline().strip("\n").split()
  m = int(params[0])
  if len(params) == 2 : 
    status = params[1].strip("\n")
  else:
    status = file.readline().strip("\n")
  #print m,status
  n = decode_status(m, status) % 4207849484
  print "Case #{0}: {1}".format(case + 1,n)
