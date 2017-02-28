def specialPythagoreanTriplet(s):
	for a in xrange(1,s):
		for b in xrange(a,s,1):
			c = s - a - b;
			if a**2 + b**2 == c**2:
				print (a,b,c)
				print (a*b*c)
								
specialPythagoreanTriplet(1000)

