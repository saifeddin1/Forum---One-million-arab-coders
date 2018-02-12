
# allowed papers: 100, 50, 10, 5, and cents
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")

print('                   *ATM Money withdrawl*\n')

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")

class ATM():
	def __init__(self, balance, bank_name):
		self.withdrawls_list = []
		self.balance = balance
		self.bank_name = bank_name

	def proccess(self, request):
		self.withdrawls_list.append(request)	
		self.balance -= request
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
					
	def withdraw(self, request):
		print("Welcome to "+ self.bank_name)
		print("Current balance = " + str(self.balance))
		print("====" * 10)	
		
		if request > self.balance:
			print("Sorry!Can't give you all this money!!")
		elif request < 0:
			print("More than zero please!")
		else:	
			ATM.proccess(self, request)			
		
		print("====" * 10)
		return self.balance

	def show_withdrawls(self):
	   	 for withdrawl in self.withdrawls_list:
   		     print(withdrawl)

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(175)
atm1.withdraw(800)
atm1.show_withdrawls()

atm2.withdraw(100)
atm2.withdraw(2000)
atm2.show_withdrawls()
