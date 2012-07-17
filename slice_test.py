

def trim(text):
    text = text[:100]

def trim2(text):
    if len(text) > 100:
        text = text[:100]


for i in range(1,10000000):
    if i % 10 == 7:
        text = 'a' * 105
    else:
        text = 'a' * 50
    trim2(text)
