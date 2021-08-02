from bank_system import BankSystem
bank = BankSystem()


class Card(object):
    pin = None
    owner = None
    bank_name = None
    state = None
    states = ['Available', 'Authentication Failed']

    def get_account(self, password):
        bank.get_account(self.pin, password)


class CardReader(object):
    state = None
    states = ['idle', 'wait', 'reading', 'ejecting', 'need maintenance', 'in maintenance']
    card = None

    def __init__(self, *args, **kwargs):
        self.state = self.states[1]

    def read_card(self, card):
        self.card = card
        account = card.get_account(input("please input account password"))
        if account:
            self.card.state = self.card.states[0]
            return account
        else:
            self.card.state = self.card.states[1]
            return None

    def wait(self):
        self.state = self.states[1]

    def idle(self):
        self.state = self.states[0]

    def eject_card(self):
        self.card = None
        self.state = self.states[1]

