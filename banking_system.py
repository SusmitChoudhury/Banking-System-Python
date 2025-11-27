class SC_Bank:
    def __init__(self, acn, name, balance):
        self.acn = acn
        self.name = name
        self.balance = balance

    def debit(self, amount):
        if self.balance - amount < 500:
            print("⚠️ Transaction failed for", self.name)
            print("Minimum balance ₹500 required to maintain account.")
        else:
            self.balance -= amount
            print("Hello", self.name, "Rs:", amount, "was debited from 8*2* Bank account")
            print("Total balance is:", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Hello", self.name, "Rs:", amount, "was credited to 8*2* Bank account")
        print("Total balance is:", self.get_balance())

    def get_balance(self):
        return self.balance


#Account creation
acc1 = SC_Bank(8228, "Susmit", 1000)
print("\nWelcome to SC Bank, Mr. Susmit ")
print("Account Number:", acc1.acn)
print("Current balance: ₹", acc1.get_balance())

#Interactive transaction system
while True:
    print("\nChoose an option:")
    print("C - Credit money")
    print("D - Debit money")
    print("B - Check balance")
    print("E - Exit")
    
    choice = input("Enter your choice (C/D/B/E): ").upper()

    if choice == 'C':
        amt = float(input("Enter amount to credit: ₹"))
        acc1.credit(amt)

    elif choice == 'D':
        amt = float(input("Enter amount to debit: ₹"))
        acc1.debit(amt)

    elif choice == 'B':
        print("Current Balance: ₹", acc1.get_balance())

    elif choice == 'E':
        print("Thank you for banking with SC Bank")
        break

    else:
        print("Invalid option! Please enter C, D, B, or E.")