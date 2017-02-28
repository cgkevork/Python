
import time

start = time.time()
        
def Coll(n, i = 1):
    
    while n >1:
        i +=1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
    return i
	
max = [0,0]
for n in range(1000000):
    if max[0] < Coll(n):
        max[0] = Coll(n)
        max[1] = n
    


elapsed = (time.time() - start)       
print "found %s at length %s in %s seconds" % (max[1],max[0],elapsed)