from bankAccount import BankAccount


class User:
    accounts = []

    def __init__(
        self, first_name="Name", last_name="lastname", email="example@to.email", age=0
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.bankaccount = BankAccount()
        User.accounts.append(self)

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            account_name.bankaccount.deposit(amount)
        return self
    def make_withdraw(self, account_name, amount):
        if account_name in self.accounts:
            account_name.bankaccount.withdraw(amount)
        return self

    def make_transfer(self, sender, reciver, ammount):
        if sender == reciver:
            print("Cannot make a transfer when the sender is also the reciver  ")
            return self
        elif sender in self.accounts and reciver in self.accounts:
            if sender.bankaccount.balance >= ammount:
                reciver.bankaccount.balance = sender.bankaccount.balance - ammount
                sender.bankaccount.balance = sender.bankaccount.balance - ammount
                print(
                    f"Sucesfully transfered ${ammount} to {reciver.first_name}.\n You now have ${sender.bankaccount.balance}"
                )
                return self
            else:
                print("Insuficent funds ! Ammount too large.")
                return self
        else:
            print("")

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            account_name.bankaccount.display_account_info()
        return self


def main():
    Anxhelo = User("Anxhelo","Bazaj", "anxhelo@email.com", 19)
    Angelo = User("Angelo","last_name", "angelo@email.com", 18)
    Anxhelo.make_deposit(Angelo, 40).make_deposit(Angelo, 40).display_user_balance(Angelo)
    Angelo.make_withdraw(Angelo, 20)

main()
