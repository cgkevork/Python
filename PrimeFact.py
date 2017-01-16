

num = 2520
#num = 13195

def Prime(n):
    factors = []
    d = 2
    while n > 1:
        while n % d ==0:
            factors.append(d)
            n = n / d
        d = d + 1

    return factors
fac = Prime(num)
print(fac)
largestprime = max(fac)
