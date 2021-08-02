from card_reader import CardReader
from machine_controller import CashBin


class AccountController(object):
    card_reader = None

    # TODO : place hold for future integration
    cash_bin = None

    def __init__(self):
        self.card_reader = CardReader()
        self.cash_bin = CashBin()
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

    def deposit_request(self, deposit_amount):
        # TODO : place hold for future integration
        pass

    def withdraw(self, withdraw_amount):
        if self.account.balance - withdraw_amount > 0:
            self.account.balance -= withdraw_amount
        else:
            raise Exception("Balance insufficient")

    def withdraw_request(self, withdraw_amount):
        # TODO : place hold for future integration
        pass
