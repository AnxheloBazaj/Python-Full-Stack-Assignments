class BankAccount:

    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount= 0):
        if amount >= 1:
            self.balance += amount
            print(f"Deposit ammount: ${amount}")
            return self

    def withdraw(self, amount=0):
        
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            print(f" Withdrawl ammount: ${amount}\n Current balance: ${self.balance}")
            return self
        else:
            print( "Insufficient funds: Charging a $5 fee")
            if self.balance <= 0:
                print(f'Balance: ${self.balance}! $5 will be kept from your next deposit')
                return self
            else:
                self.balance -= 5
                return self

    def display_account_info(self):
        print(f"You now have : ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance >0:
            self.balance += self.int_rate * self.balance
            return self
        else:
            print("Insufficient funds!")
            return self
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True






