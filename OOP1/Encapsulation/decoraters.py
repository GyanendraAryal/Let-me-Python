# Getter by decorator-unlike getter Method
class Bank:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
        # Setter

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount


b = Bank()
b.balance = 500
print(b.balance)
