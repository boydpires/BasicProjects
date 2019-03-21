import random
import os

mainWhile = 1

os.system('cls')
print("\t\t\t--------------------------------------------------------------------------------")
print("\n\t\t\t\t\t\t\tChallenge me human 1.0 \n".upper())
print("\t\t\t--------------------------------------------------------------------------------")

while mainWhile == 1:
	random_num = random.randint(1,10)

	while True:
		my_guess = int(input("\nWhat's your guess? ")) 
		if my_guess == random_num:
			print("You're right!".upper())
			break
		elif my_guess < random_num:
			print("low man")
		else:
			print("that's high")

	while True:
		endGame = input("\nDo you wanna continue playing? y/n ")
		if (endGame == 'n') or (endGame == 'N'):
			mainWhile = 0
			break
		elif (endGame == 'y') or (endGame == 'Y'):
			os.system('cls')
			print("\t\t\t--------------------------------------------------------------------------------")
			print("\n\t\t\t\t\t\t\tChallenge me human 1.0 \n".upper())
			print("\t\t\t--------------------------------------------------------------------------------")
			print("\n\nAlright here's another one")
			break
		else:
			print("Input could'nt be recognised \nPlease type in y/Y to continue or n/N to quit ")

os.system('cls')

print("\t\t\t--------------------------------------------------------------------------------")
print("\n\t\t\t\t\t\t\tChallenge me human 1.0 \n".upper())
print("\t\t\t--------------------------------------------------------------------------------")

print("\n\tThanks for playing!\n".upper())

ratings = int(input("Please rate this game in the scale of 5/"))	

if ratings == 0:
	print("\nHope we can fix this")
elif ratings < 3:
	print("\nHope we can improve in the next update")
elif ratings < 5:
	print("\nWe're glad you liked it")
elif ratings == 5:
	print("\nHope this made your day")
else:
	print("\nMan ssly? more than 5?")

print("\n\n\t*** Created by: Boyden ***\n\n")		 	


