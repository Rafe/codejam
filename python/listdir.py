import os
path = "/"
files = os.listdir(path)

for file in files:
  if os.path.isfile(path + file):
    type = "file"
  else:
    type = "dir"

  print file + " is a " + type
