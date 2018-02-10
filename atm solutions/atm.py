# allowed papers: 100, 50, 10, 5, and cents
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print('                   *ATM Money withdrawl*')

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
def withdraw(balance, request):

	print("Current balance = " + str(balance))

	result = balance

	if request > balance:

		print("Sorry!Can't give you all this money!!")

	elif request < 0:

		print("More than zero please!")

	else:
		result = balance - request
		while request > 0:

			

			if request >= 100:
				request -= 100
				print("Give 100")
			elif request >= 50:
				request -= 50
				print("Give 50")
			elif request >= 10:
				request -= 10
				print("Give 10")
			elif request >= 5:
				request -= 5			
				print("Give 5")
			else:
				print("Give " + str(request))
				request = 0
	return result

balance = 500
balance = withdraw(balance, 275)
balance = withdraw(balance, 100)
balance = withdraw(balance, 50)
balance = withdraw(balance, 7000)
