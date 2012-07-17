import sys
import string

def read_input(file_name):
  file = open(file_name)

  case = 0
  for line in file.readlines():
    if case == 0:
      case += 1
      continue
    process(case, line)
    case += 1

def process(case, line):
  params = map(lambda s: int(s), line.split()[1:])

  result = safty(params)

  print "Case #%d:" % case,
  for i in result:
    print i,
  print ""

def safty(scores):
  X = sum(scores)
  sorted = [x for x in scores].sort()
  n = len(scores)
  if n == 2:
    fraction = (scores[1] - scores[0] + X) / float(2 * X)
    return [fraction * 100, (1 - fraction) * 100]
  else:
    l = 2 * X
    for i in range(0, len(sorted)):
      for j in range(0,)


read_input(sys.argv[1])
