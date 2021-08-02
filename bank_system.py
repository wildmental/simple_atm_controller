class Account(object):
    owner = None
    balance = 0
    state = None
    states = ['Available', 'Suspended']


class BankSystem(object):
    bank_name = None
    open_time = None
    close_time = None
    main_server = None

    def get_account(self, pin, password):
        return self._validate_account(pin=pin, password=password)

    def _validate_account(self, *args, **kwargs):
        account = self.main_server.get_account_by_pin(kwargs['pin'])
        authentication = account.authenticate(kwargs['password'])
        if authentication:
            return Account()
        else:
            return None
