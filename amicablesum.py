#not working right, misses numbers
lst = []
    
def factor(n):
    return [x for x in range(1, n) if n %x == 0]
    
for i in range(1,10000):
    a = sum(factor(i))
    b = sum(factor(a))
    if a == b:
        lst.append(i)
    else:
        continue
print lst

print sum(lst)