#Piksi Generate and Check Prime numbers

#determine amount of numbers to calculate
a = int(raw_input("Enter the amount of Fibonacci terms required: "))

#calculate the Fib sequence out as far as items specified 
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

#function to check if numbers are prime
def is_prime(x):
    return all(x % i for i in xrange(2, x))

#call Fib function returning a list of numbers
Fib = list(fib(a))
#print Fib


#check each number for specified condition

for item in Fib:
	
	if item % 3 == 0 and item % 5 == 0:
		print "FizzBuzz"
	elif item % 3 == 0:
		print "Buzz" 
	elif item % 5 == 0:
		print "Fizz"
	elif is_prime(item):
		print "BuzzFizz" 
	else:
		print item


