import math

def get_approximate_size(width ,height, words_count):
  return math.floor(math.sqrt((width * height) / words_count ))

def flow(width,height,size,words):
  row = height / size
  line = width / size
  current_line = 0
  current_row = 1
  i = 0
  while i < len(words):
    if(current_line != 0):
      current_line += 1 # add space
    current_line += len(words[i])
    if(current_line > line):
      current_line = 0
      current_row += 1
      if(current_row > row):
        return False
    else:
      i += 1

  return True

def max_size(width,height,words):
  words_count = 0
  for word in words:
    words_count += len(word) + 1

  font = int(get_approximate_size(width,height,words_count))

  for size in range(font,0,-1):
    if flow(width,height,size,words):
      return size

max_size.case = 0

file = open('billboards.txt')
file.readline()

case = 1
for line in file:
  param = line.split()
  print "Case #{0}: {1}".format(case,max_size(int(param[0]),int(param[1]),param[2:]))
  case += 1

#max_size(20,6,['hacker','cup'])
#max_size(100,20,['hacker','cup','2013'])
#max_size(10,20,['MUST','BE','ABLE','TO','HACK'])
#max_size(55,25,['can','you','hack'])
#max_size(100,20,['hack','your','way','to','the','cup'])
