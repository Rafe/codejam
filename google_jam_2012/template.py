import sys

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
  params = line.split()

  #algorithem
  #result = func(params)
  result = 4

  print "Case #%d: %s" % (case, result)

read_input(sys.argv[1])
