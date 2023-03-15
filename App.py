class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is {self.balance}."

    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited {amount}. Your new balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Sorry, you do not have enough funds in your account."
        self.balance -= amount
        return f"You have withdrawn {amount}. Your new balance is {self.balance}."


if __name__ == "__main__":
    atm = ATM()
    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(atm.check_balance())
        elif choice == 2:
            amount = int(input("Enter the amount you want to deposit: "))
            print(atm.deposit(amount))
        elif choice == 3:
            amount = int(input("Enter the amount you want to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

