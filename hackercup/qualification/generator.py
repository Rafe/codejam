def lcm(a,b):
  return a * b / gcd(a,b)

def gcd(a,b):
  while b != 0:
    a,b = b,a%b 
  return a

def g(N, P1, M, A, B):
  past = set()
  last = P1
  A = A % M
  B = B % M
  i = 0

  print A,B
  result = [P1]
  past.add(P1)
  while i < N-1:
    last = 1 + ((A * last + B) % M )
    i += 1
    if last in past: 
      print result[:10]
      break
    else:
      past.add(last)
    result.append(last)

  return len(result)

def gg(N):
  result = []
  i = 0
  while i < N:
    result.append(i)
    i += 1


#1558749102 1 10000000 10000000 10000000 30000001 780000000 660000001 389999998
#print g(1558749102,1,10000000,30000001,780000000)
#print g(1558749102,10000000,10000000,660000001,389999998)
#gg(1000000000000000)
#848937385843 8 7 17 19 0 5 6 2
print g(848937385843,8,17,0,5)
