def checkDuplicate(string):
  duplicate = {}
  for char in string:
    if char in duplicate:
      return True
    duplicate[char] = True
  return False

def checkDuplicate2(string):
  "checking without extra space"
  for i in range(0,len(string)-1):
    for j in range(i+1,len(string)):
      if string[i] == string[j]:
        return True
  return False

def test(fn):
  print "testing",fn.__name__
  print "aabbcc :",fn("aabbcc")
  print "abc :",fn("abc")
  print "abcc :",fn("abcc")

if __name__ == "__main__":
  test(checkDuplicate)
  test(checkDuplicate2)
