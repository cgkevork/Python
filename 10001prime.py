def primes(n):
    primes = []
    attempt = 3
    while len(primes) < (n-1):
        for i in range(len(primes)):
            if attempt % primes[i] == 0:
                attempt += 2
                break
        else:
            primes.append(attempt)
            print (primes)
    return (primes)

primes(10001)

