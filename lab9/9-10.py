class BankAccount:
    def __init__(self, name, account_num, balance=0):
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance

    def __str__(self):
        return '{}님의 계좌 {}의 잔고는 {}원입니다.'.format(
            self.__name, self.__account_num, self.__balance)

    def get_name():
        return self.__name

    def get_account_num():
        return self.__account_num

    def get_balance():
        return self.__balance

    def deposit(self, money):
        self.__balance += money
        return print('{}원이 입금되었습니다. 잔고는 {}입니다.'.format(money,
                                                 self.__balance))

    def withdraw(self, money):
        if self.__balance - money < 0:
            return print('계좌 잔고는 {}원으로 인출 요구 금액 {}원보다 작습니다.'.format(
                self.__balance, money))

        else:
            self.__balance -= money


account1 = BankAccount('홍길동', '1234-0001')
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)
