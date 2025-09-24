### Sum of Squares
def sqrSum1(n):
    if (n >= 0):
        sum = 0
        # iterates for all numbers smaller than n
        for i in range(1,n):
            sum += i*i
        return sum
    else:
        return 0 # for non-positive input n's


### One Line of Code
def sqrSum2(n):
    return sum([i*i for i in range (1, n)])


### Sum of Squares for Odd Ints
def posSqrSum1 (n):
    if (n >= 0):
        sum = 0
        for i in range(1,n,2):
            sum += i*i
        return sum
    else: return 0


### One Line of Code for posSqrSum
def posSqrSum2(n):
    return sum([i*i for i in range (1,n,2)])







### Test code
# First Function
print(sqrSum1(5)) # 16+9+4+1 = 30

# Second Function
print(sqrSum2(5)) # 16+9+4+1 = 30

# Third Function
print(posSqrSum1(7)) # 25+9+1 = 35
print(posSqrSum1(9)) # 49+25+9+1 = 84

# Fourth Function
print(posSqrSum2(7)) # 25+9+1 = 35
print(posSqrSum2(9)) # 49+25+9+1 = 84
