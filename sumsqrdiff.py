

r = range(1, 101)  
a = sum(r)  
print (a * a - sum(i*i for i in r))

for i in range(1,101):
    sum = 0;
    squares=0;
   
    
    squares = squares + i**2
    sum = sum+i

sum2=sum**2
diff = sum2 - squares

print('square ', squares)
print('sum square ', sum2)




