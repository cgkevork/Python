import math
x = 100

n = math.factorial(x)
n = str(n)
lst = list(n)
sum = sum([int(i) for i in lst])
print sum