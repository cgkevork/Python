import math 

x= 2000000
sum = 0 

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return n>1;

for num in range(x):
	if is_prime(num):
		print num
		sum += num 

print sum