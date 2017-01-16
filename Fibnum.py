

xp=2
x=3
sum =0

while x < 4000000:
    xn=x
    x=x+xp
    xp=xn

    if (x % 2 ==0):
        sum = sum + x
        print('even sum',sum)
 

    
a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a+b  # the real formula for Fibonacci sequence
print total
