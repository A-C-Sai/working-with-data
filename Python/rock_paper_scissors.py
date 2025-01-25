import random

# from computer point of view r p s
output_matrix = [		
					[-1,0,1],
					[1,-1,0],
					[0,1,-1]
				]


choices = {'r':0,'p':1,'s':2}


def menu_option():
	print('1. Play')
	print('2. Exit')

def game():

	while (True):
		menu_option()

		option = input("Would you like to play (1) or exit (2): ")
		computer_choice = choices.get(random.choice(list(choices.keys())))

		match (option):

			case '1':
				user_choice = choices.get(input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()) 
				
				if user_choice == None:
					print('Please enter a vaild choice')
				else:
					result = 'You Won' if output_matrix[computer_choice][user_choice] == 0 else 'You Lost' if output_matrix[computer_choice][user_choice] == 1 else 'Draw'
					print(result)
			case '2':
				print("Thank you for playing")
				break

			case _:
				print("Please check your input and try again")


game()


	
