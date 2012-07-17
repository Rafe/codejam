best = []
worst = []

def prefer(A,B):
  if A[0] < B[0]:
    if A[1] <= B[1]:
      return 1
  elif A[0] > B[0]:
    if A[1] >= B[1]:
      return -1
  elif A[0] == B[0]: 
    if A[1] < B[1]:
      return 1
    elif B[1] < A[1]:
      return -1

  return 0

def update_best(product):
  for i in range(len(best)):
    p = prefer(product,best[i])
    if p == 1:
      best[i] = product
    if p != 0:
      return
  best.append(product)

def update_worst(product):
  for i in range(len(worst)):
    p = prefer(product,worst[i])
    if p == -1:
      worst[i] = product
    if p != 0:
      return
  worst.append(product)

print best
print worst
