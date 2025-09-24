
### Produce [1, 10, 100, 1000, 10000, 100000]
lst1 = [10**i for i in range(0,6)]
print(lst1)

### produce [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
lst2 = [i*(i+1) for i in range(0, 10)]
print(lst2)

### Produce [‘a’, ‘b’, ‘c’, ... , ‘z’]
# chr(i) produces letter, ord('') produces ascii code
lst3 = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(lst3)