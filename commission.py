class Value:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name
        print(f'Calling class: {owner}\nAttribute name: {name}\n')

    def __get__(self, instance, owner):
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Must be positive!')
        instance.__dict__[self.private_name] = value * (1 - instance.commission)


class Account:
    amount = Value()

    def __init__(self, commission, amount=0):
        self.commission = commission
        if amount:
            self._amount = amount
        else:
            self._amount = 0

    def top_up(self, amount):
        if amount <= 0:
            raise ValueError
        self._amount += amount * (1 - self.commission)
