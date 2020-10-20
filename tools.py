import os.path


class Person:
    def __init__(self, ID, NAME, EMAIL, PHONE):
        self.PHONE = PHONE
        self.EMAIL = EMAIL
        self.NAME = NAME
        self.ID = int(ID)

    def __str__(self):
        return f'{self.ID}, {self.NAME}, {self.EMAIL}, {self.PHONE}'


class Gadget:
    def __init__(self, ID, BRAND, TYPE, MODEL):
        self.MODEL = MODEL
        self.TYPE = TYPE
        self.BRAND = BRAND
        self.ID = int(ID)


class People:
    def __init__(self):
        if not os.path.exists('people.txt'):
            print('Файл people.txt не существует')
        else:
            f = open('people.txt')
            self.people = [Person(*record.split(', ')) for record in f.read().split('\n')]

    def __str__(self):
        result = ''
        for person in self.people:
            result += person.__str__() + '\n'
        return result


print(People())
