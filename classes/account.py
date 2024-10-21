from __future__ import annotations
from enum import Enum
from typing import List, Any

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    CREDIT = 3

class Account:
    _type: AccountType = None
    _balance: float = 0.0
    _interest_rate: float = 0.0
    _pin: str = None
    transactions: list[str] = []
    _owner: 'User' = None

    def __init__(self, owner: 'User', account_type: 'AccountType', balance: float, interest_rate: float, pin: str):
        self._owner = owner
        self._type = account_type
        self._balance = balance
        self._interest_rate = interest_rate
        self._pin = pin

    def __str__(self):
        return f'{self._type.name}: {self._balance}'

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError('Deposit amount must be positive')
        elif amount == 0:
            pass
        else:
            self._balance += amount
            self.transactions.append("Deposit: " + str(amount))

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError('Withdraw amount must be positive')
        elif amount == 0:
            pass
        elif amount > self._balance:
            raise ValueError('Insufficient funds')
        else:
            self._balance -= amount
            self.transactions.append("Withdraw: " + str(amount))

    def transfer(self, amount: float, account: 'Account'):
        if amount < 0:
            raise ValueError('Transfer amount must be positive')
        elif amount == 0:
            pass
        else:
            self.withdraw(amount)
            account.deposit(amount)
            self.transactions.append("Transfer: " + str(amount) + " to " + account._type.name)
            account.transactions.append("Transfer: " + str(amount) + " from " + self._type.name)

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        self.transactions.append("Interest: " + str(interest))

    def check_pin(self, pin: str) -> bool:
        return self._pin == pin

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self.transactions

    def get_interest_rate(self):
        return self._interest_rate

    def get_account_type(self):
        return self._type.name
