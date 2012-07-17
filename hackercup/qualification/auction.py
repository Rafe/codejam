def lcm(a,b):
  return a * b / gcd(a,b)

def gcd(a,b):
  while b != 0:
    a,b = b,a%b 
  return a

class Products:
  def __init__(self,N,P1,W1,M,K,A,B,C,D):
    self.N = N
    self.M = M
    self.K = K
    self.P = P1 
    self.W = W1 
    self.A = A % M 
    self.B = B % M
    self.C = C % K
    self.D = D % K

  def get_price_cycle(self):
    if self.A == 0:
      return 1

    if self.A == 1:
      if self.B + 1 == 0:
        return 1
      d = gcd(self.M,self.B + 1)
      return self.M / d

    self.prices = []
    self.pindex = 0

    while self.pindex < self.M:
      self.P = ((self.A * self.P + self.B) % self.M) + 1
      if len(self.prices) > 0 and self.prices[0] == self.P:
        break
      self.prices.append(self.P)
      self.pindex += 1
    return self.pindex

  def get_weight_cycle(self):
    if self.C == 0:
      return 1

    if self.C == 1:
      d = gcd(self.K,self.D + 1)
      return self.K / d

    self.weight = []
    self.windex = 0

    while self.windex < self.K:
      self.W = ((self.C * self.K + self.D) % self.M) + 1
      if len(self.weight) > 0 and self.weight[0] == self.W:
        break
      self.weight.append(self.W)
      self.windex += 1
    return self.windex

  #Pi = ((A*Pi-1 + B) mod M) + 1 (for all i = 2..N)
  def generate_prices(self):
    self.prices = []
    self.pindex = 0

    if self.A == 1:
      d = self.B  
      if d == 0:
        return self.M
      if d == self.M - 1:
        return 1
      if d == self.M - 2:
        return self.M

    while self.pindex < self.M:
      self.P = ((self.A * self.P + self.B) % self.M) + 1
      if len(self.prices) > 0 and self.prices[0] == self.P:
        break
      self.prices.append(self.P)
      self.pindex += 1
    return self.pindex

  #Wi = ((C*Wi-1 + D) mod K) + 1 (for all i = 2..N)
  def generate_weight(self):
    self.weight = []
    self.windex = 0
    while self.windex < self.K:
      self.W = ((self.C * self.W + self.D) % self.K) + 1
      if len(self.weight) > 0 and self.weight[0] == self.W:
        break
      self.weight.append(self.W)
      self.windex += 1
    print self.windex

  def prefer(self,A,B):
    #cmp(price_a,price_b)
    if A[0] < B[0]:
      if A[1] <= B[1]:
        return 1
      else: return 0
    if B[0] < A[0]:
      if B[1] <= A[1]:
        return -1
      else: return 0
    if A[0] == B[0]:
      if A[1] < B[1]:
        return 1
      elif B[1] < A[1]:
        return -1

    return 0

#N, P1, W1, M, K, A, B, C and D
def get_terribles_and_bargins(N, P1, W1, M, K, A, B, C, D):
  products = Products(N,P1,W1,M,K,A,B,C,D)
  pc = products.get_price_cycle()
  wc = products.get_weight_cycle()
  #print pc,wc
  cycle = lcm(pc,wc)
  #print cycle
  a = N / cycle 
  a += 1
  return (a,a)



if __name__ == "__main__":
  file = open("auction.txt")
  file.readline()
  case = 1
  for line in file:
    p = [int(x) for x in line.split()]
    result = get_terribles_and_bargins(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
    print "Case #{0}: {1} {2}".format(case,result[0],result[1])
    case += 1

#prefer:
#A.price < B.price and A.weight <= B.weight 
#or A.price == B.price and A.weight < B.weight
#[1, 2, 3, 4, 5]
#[4, 7, 3, 6, 2]
#A1 : >2, =3 >4 =5 : bargin
#A2 : <1, =3, =4, =5 : terrible
#A3 : =1, =2, >4, =5 : bargin
#A4 : <1, =2, <3, =5 : terrible 
#A5 : =1, =2, =3, =4, =5: bargin & terrible
# 3:3
