from __future__ import annotations
from typing import List, Any
from classes.account import AccountType, Account

class User:
    _name = None
    _accounts: list['Account'] = []

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f'User: {self._name}'

    def create_account(self) -> 'Account':

        account_type_num = input(
            'What type of account would you like to create?\n(1) Checking\n(2) Savings\n(3) Credit\n')
        while account_type_num not in ['1', '2', '3']:
            account_type_num = input(
                'Invalid account type. Please select an account type from the list below:\n(1) Checking\n(2) Savings\n(3) Credit\n')

        account_type = AccountType(int(account_type_num))

        balance = float(input('How much would you like to deposit?\n'))
        while balance <= 0:
            balance = float(input('Invalid balance. Please enter a positive amount\n'))

        interest_rate = float(input('What is the interest rate?\n'))
        while interest_rate <= 0:
            interest_rate = float(input('Invalid interest rate. Please enter a positive amount\n'))

        pin = input('Please enter a 4 digit pin\n')
        while len(pin) != 4 or not pin.isdigit():
            pin = input('Invalid pin. Please enter a 4 digit pin\n')

        for account in self._accounts:
            if account.get_account_type() == account_type:
                raise ValueError('Account already exists')

        account = Account(self, account_type, balance, interest_rate, pin)
        self._accounts.append(account)
        return account

    def get_account(self, account_type: 'Account') -> 'Account' | None:
        if account_type is None:
            raise ValueError('Account type must be specified')

        for account in self._accounts:
            if account.get_account_type() == account_type:
                return account
        return None

    def get_accounts(self) -> List['Account']:
        return self._accounts

    def get_name(self) -> str:
        return self._name