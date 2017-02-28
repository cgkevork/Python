def roll():
	import random
	die = random.randrange(1,6)
	return die
	
print(" Lets play a game of dice!")
while True:
	a= raw_input("would you like to roll? yes/no > ")
	if a=="yes":
		print roll()
		continue
	elif a=="no":
		break
	else:
		print("Enter either yes/no")