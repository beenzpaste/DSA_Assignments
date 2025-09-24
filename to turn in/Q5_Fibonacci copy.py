### Fibonacci Function that yields generator
def fibs(n):
    pos = [1, 1]
    yield pos[0]
    yield pos[1]
    while len(pos)<n:
        pos.append(pos[-1] + pos[-2])
        yield pos[len(pos)-1]




### Test code
for curr in fibs(8):
    print(curr) # prints curr at every loop