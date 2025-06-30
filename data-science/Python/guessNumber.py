import random

def guessNumber():
	random_number = random.randint(1,10)

	while (True):

		try:
			user_input = int(input("Guess a number between 1 and 10: "))
		except ValueError:
			print('Please ensure to only give integers as inputs')
		else:
			if user_input == random_number:
				print("Yay, congrats. You have guessed the number {} correctly!!".format(user_input))
				break
			elif user_input < random_number:
				print("Sorry, guess again. Too low")
			elif user_input > random_number:
				print("Sorry, guess again. Too high")


guessNumber()