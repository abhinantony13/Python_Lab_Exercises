# Bank account system using OOP
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Enter an amount greater than zero.")
        else:
            self.balance += amount
            print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter an amount greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance:.2f}")

name = input("Account holder name: ")
account = BankAccount(name)

while True:
    print("\\n1. Deposit  2. Withdraw  3. Balance  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        account.deposit(float(input("Amount to deposit: ")))
    elif choice == "2":
        account.withdraw(float(input("Amount to withdraw: ")))
    elif choice == "3":
        account.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
