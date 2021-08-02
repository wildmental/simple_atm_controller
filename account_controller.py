from card_reader import CardReader


class AccountController(object):
    card_reader = None

    def __init__(self):
        self.card_reader = CardReader()
        account = self.card_reader.read_card(input("insert card"))

        if account is None:
            raise Exception("Account authentication failed")
        if account.state != 'Available':
            raise Exception("Account is not available")

        self.account = account

    def see_balance(self):
        return self.account.balance

    def deposit(self, deposit_amount):
        self.account.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.account.balance - withdraw_amount > 0:
            self.account.balance -= withdraw_amount
        else:
            raise Exception("Balance insufficient")
