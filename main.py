class Account():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, deposit):
        self.amount += deposit
        print(
            f"You've just deposit {deposit} BDT\nYour current balance is {self.amount} BDT")

    def withdraw(self, withdraw):
        if withdraw > self.amount:
            print("You don't have enough funds to withdraw")
        elif withdraw <= self.amount:
            self.amount -= withdraw
            print(
                f"You've just withdrawn {withdraw} BDT\nYour current balance is {self.amount} BDT")
        else:
            print("Invalid Input")

    def show(self):
        print(f"Hello {self.name}, Your current Balance is {self.amount}")


# user functionalities
user_name = input("Enter your name: ")
funds = float(input("Enter the funds you currently have: "))

account_1 = Account(user_name, funds)

option = 0

while option != 4:

    option = int(
        input("\n\n1. Deposit\n2. Withdraw\n3. See Balance\n4. Quit\nEnter Your Choice: "))

    if option == 1:
        deposit = float(input("Enter the amount you want to deposit: "))
        account_1.deposit(deposit)
    elif option == 2:
        withdraw = float(input("Enter the amount you want to withdraw: "))
        account_1.withdraw(withdraw)
    elif option == 3:
        account_1.show()
else:
    quit()
