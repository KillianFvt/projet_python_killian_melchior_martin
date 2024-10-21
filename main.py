from classes.account import AccountType
from classes.user import User

def main():

    user = User(input('Enter your name: '))
    print('Welcome to the bank, ' + user.get_name())
    print('Please create your first account')

    user.create_account()
    print('Account created successfully')

    exit_selected = False
    account_selected = None
    while not exit_selected:
        if account_selected is None:
            print('Select an account:')
            for i, account in enumerate(user.get_accounts()):
                print(f'{i + 1}: {account.get_account_type()}')
            print('0: Exit')
            account_num = input('Enter the number of the account you would like to access: ')

            if account_num == '0':
                exit_selected = True
                break
            elif not account_num.isdigit() or int(account_num) > len(user.get_accounts()):
                print('Invalid account number')
                continue
            else:
                account_selected = user.get_accounts()[int(account_num) - 1]
                pin = input('Enter your pin: ')

                if not account_selected.check_pin(pin):
                    print('Incorrect pin')
                    account_selected = None
                    continue

                print(f'You have selected {account_selected.get_account_type()}')

        else:
            print('What would you like to do?')
            print('1: Deposit')
            print('2: Withdraw')
            print('3: Transfer')
            print('4: Wait a month and add interest')
            print('5: View transactions')
            print('6: View balance')
            print('7: Select another account')
            print('8: Create a new account')
            print('0: Exit')
            selected_action = input('Enter the number of the action you would like to take: ')

            if selected_action == '1':
                amount = float(input('Enter the amount you would like to deposit: '))
                try:
                    account_selected.deposit(amount)
                except ValueError as e:
                    print(e)
                    continue
                else:
                    print(f'You have deposited {amount}')
                    print(f'You have {account_selected.get_balance()} remaining')

            elif selected_action == '2':
                amount = float(input('Enter the amount you would like to withdraw: '))
                try:
                    account_selected.withdraw(amount)
                except ValueError as e:
                    print(e)
                    continue
                else:
                    print(f'You have withdrawn {amount}')
                    print(f'You have {account_selected.get_balance()} remaining')

            elif selected_action == '3':
                amount = float(input('Enter the amount you would like to transfer: '))
                while amount > account_selected.get_balance():
                    amount = float(input('Insufficient funds. Please enter a valid amount: '))

                print('Select an account to transfer to:')
                for i, account in enumerate(user.get_accounts()):
                    print(f'{i + 1}: {account.get_account_type()}')
                account_num = input('Enter the number of the account you would like to transfer to: ')
                if not account_num.isdigit() or int(account_num) > len(user.get_accounts()):
                    print('Invalid account number')
                    continue
                else:
                    account = user.get_accounts()[int(account_num) - 1]
                    try:
                        account_selected.transfer(amount, account)
                    except ValueError as e:
                        print(e)
                        continue
                    else:
                        print(f'You have transferred {amount} to {account.get_account_type()}')

            elif selected_action == '4':
                account_selected.add_interest()
                print('You waited a month and now have ' + str(account_selected.get_balance()))

            elif selected_action == '5':
                print('Transactions:')
                for transaction in account_selected.transactions:
                    print(transaction)

            elif selected_action == '6':
                print('Balance: ' + str(account_selected.get_balance()))

            elif selected_action == '7':
                account_selected = None

            elif selected_action == '8':
                account_selected = None
                user.create_account()
                print('Account created successfully')

            elif selected_action == '0':
                exit_selected = True
                break
            else:
                print('Invalid action')

        print('----------------------------------------')

    print('See you later!')


if __name__ == '__main__':
    main()