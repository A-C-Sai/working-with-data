import random


def computerGuess(start,end):
	# guess = random.randint(start,end)
	guess = (start+end)//2

	while (True):

		guess_status = input("Is {} too high (H), too low (L), or correct (C)?? ({},{}) ".format(guess,start,end))

		if (guess_status.lower() == 'c'):
			print('Yay! The computer guessed your number, {}, correctly!'.format(guess))
			return
		elif (guess_status.lower() == 'l'):
			computerGuess(guess+1,end)
			return
		elif (guess_status.lower() == 'h'):
			computerGuess(start,guess-1)
			return


computerGuess(1,1000)
