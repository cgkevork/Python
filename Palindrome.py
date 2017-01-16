max = 0
for x in xrange(100,1000):
    for y in xrange(100,1000):
        if str(x*y) == str(y*x)[::-1]:
            print (x*y)
            if (x*y) > max:
                max = x* y

            print('max',max)
