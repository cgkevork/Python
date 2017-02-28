def roll():
	import random
	die = random.randrange(1,6)
	return die
	
print(" Lets play a game of Guess the Random number between 1 - 6!")
die = roll()
while True:
	a= raw_input("Whats your guess > ")
	if int(a)==die:
		print "You guessed it!"		
		break
	elif a != die:
		print "please guess again"
	else:
		print("Enter a number between 1- 6")