# Bank Management System with Interest

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0, annual_interest_rate=0.05):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.annual_interest_rate = annual_interest_rate  # Default interest rate is 5%

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: ${self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        # Allows overdraft (negative balance)
        if amount <= 0:
            return "Withdrawal amount must be positive."
        self.balance -= amount
        return f"Withdrawal successful. New balance: ${self.balance:.2f}"

    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}"

    def apply_interest(self):
        interest = self.balance * self.annual_interest_rate
        self.balance += interest
        return f"Interest applied. New balance: ${self.balance:.2f}"

# Example usage
if __name__ == "__main__":
    # Create a new bank account with a starting balance and interest rate
    account = BankAccount("123456", "John Doe", 100.0, 0.05)

    print(account.check_balance())  # Check initial balance

    # Deposit money
    print(account.deposit(50.0))  # Deposit $50

    # Withdraw money (allows negative balance)
    print(account.withdraw(200.0))  # Withdraw $200

    # Apply interest
    print(account.apply_interest())

    # Check final balance
    print(account.check_balance())
