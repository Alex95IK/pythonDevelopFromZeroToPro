class BankAccount:
    def __init__(self, client_id, client_first_name, client_last_name, balance=0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, add_balance):
        self.balance = self.balance + add_balance

    def withdraw(self, withdraw_balance):
        self.balance = self.balance - withdraw_balance
