class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = ""
        self.__balance = 0.0

        self.set_account_number(account_number)
        self.set_balance(balance)

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Warning: Balance cannot be negative.")

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance


account = BankAccount("1234567890", 5000.00)

print("Account Number:", account.account_number)
print(f"Balance: ₱{account.balance:,.2f}")

account.set_account_number("0987654321")
account.set_balance(7500.50)

print("\nUpdated Account Information")
print("Account Number:", account.account_number)
print(f"Balance: ₱{account.balance:,.2f}")

account.set_balance(-1000)
print("Account Number:", account.account_number)
print(f"Final Balance: ₱{account.balance:,.2f}")
