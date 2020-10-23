import os.path


class Person:
    def __init__(self, ID, NAME, EMAIL, PHONE):
        self.PHONE = PHONE
        self.EMAIL = EMAIL
        self.NAME = NAME
        self.ID = int(ID)

    def __str__(self):
        return f'{self.ID}, {self.NAME}, {self.EMAIL}, {self.PHONE};'


class Gadget:
    def __init__(self, ID, BRAND, TYPE, MODEL):
        self.ID = int(ID)
        self.BRAND = BRAND
        self.TYPE = TYPE
        self.MODEL = MODEL

    def __str__(self):
        return f'{self.ID}, {self.BRAND}, {self.TYPE}, {self.MODEL};'


class Work:
    def __init__(self, ID, WORK, PRICE):
        self.ID = int(ID)
        self.WORK = WORK
        self.PRICE = int(PRICE)

    def __str__(self):
        return f'{self.ID}, {self.WORK}, {self.PRICE};'


class Request:
    def __init__(self, ID, DATE, CLIENT_ID, EQUIP_ID, REASON, MASTER_ID, WORK_IDS, COMPLETE_DATE,
                 DELIVERY_DATE, COST):
        self.ID = int(ID)
        self.DATE = DATE
        self.CLIENT_ID = int(CLIENT_ID)
        self.EQUIP_ID = int(EQUIP_ID)
        self.REASON = REASON
        self.MASTER_ID = int(MASTER_ID)
        self.WORK_IDS = list(map(int, WORK_IDS))
        self.COMPLETE_DATE = COMPLETE_DATE
        self.DELIVERY_DATE = DELIVERY_DATE
        self.COST = int(COST)

    def __str__(self):
        return f'{self.ID}, {self.DATE}, {self.CLIENT_ID}, {self.EQUIP_ID}, {self.REASON}, ' \
               f'{self.MASTER_ID}, *, {", ".join(list(map(str, self.WORK_IDS)))}, *, ' \
               f'{self.COMPLETE_DATE}, {self.DELIVERY_DATE}, {self.COST}; '


class People:
    def __init__(self):
        if not os.path.exists('people.txt'):
            print('Файл people.txt не существует')
        else:
            f = open('people.txt')
            self.people = [Person(*record.split(', ')) for record in
                           f.read().replace(';', '').split('\n') if record]

    def __str__(self):
        result = ''
        for person in self.people:
            result += person.__str__() + '\n'
        return result

    def add_person(self, person):
        self.people.append(Person(*person[:-1].split(', ')))

    def make_file(self):
        f = open('people.txt', 'w')
        f.write(self.__str__())

    def get_ids(self):
        return [person.ID for person in self.people]

    def get_names(self):
        return [person.NAME for person in self.people]

    def get_emails(self):
        return [person.EMAIL for person in self.people]

    def get_phones(self):
        return [person.PHONE for person in self.people]


class Equip:
    def __init__(self):
        if not os.path.exists('equip.txt'):
            print('Файл equip.txt не существует')
        else:
            f = open('equip.txt')
            self.gadgets = [Gadget(*record.split(', ')) for record in
                            f.read().replace(';', '').split('\n') if record]

    def __str__(self):
        result = ''
        for gadget in self.gadgets:
            result += gadget.__str__() + '\n'
        return result

    def add_equip(self, equip):
        self.gadgets.append(Gadget(*equip[:-1].split(', ')))

    def make_file(self):
        f = open('equip.txt', 'w')
        f.write(self.__str__())

    def get_ids(self):
        return [gadget.ID for gadget in self.gadgets]

    def get_brands(self):
        return [gadget.BRAND for gadget in self.gadgets]

    def get_types(self):
        return [gadget.TYPE for gadget in self.gadgets]

    def get_models(self):
        return [gadget.MODEL for gadget in self.gadgets]


class Works:
    def __init__(self):
        if not os.path.exists('works.txt'):
            print('Файл works.txt не существует')
        else:
            f = open('works.txt')
            self.works = [Work(*record.split(', ')) for record in
                          f.read().replace(';', '').split('\n') if record]

    def __str__(self):
        result = ''
        for work in self.works:
            result += work.__str__() + '\n'
        return result

    def add_work(self, work):
        self.works.append(Work(*work[:-1].split(', ')))

    def make_file(self):
        f = open('works.txt', 'w')
        f.write(self.__str__())

    def get_ids(self):
        return [work.ID for work in self.works]

    def get_works(self):
        return [work.WORK for work in self.works]

    def get_prices(self):
        return [work.PRICE for work in self.works]


class Requests:
    def __init__(self):
        if not os.path.exists('requests.txt'):
            print('Файл requests.txt не существует')
        else:
            f = open('requests.txt')
            self.requests = []
            for record in f.read().replace(';', '').split('\n'):
                if record:
                    a, b, c = map(lambda x: x.split(', '), record.split(', *, '))
                    self.requests.append(Request(*(a + [b] + c)))

    def __str__(self):
        result = ''
        for request in self.requests:
            result += request.__str__() + '\n'
        return result

    def add_request(self, request):
        a, b, c = map(lambda x: x.split(', '), request[:-1].split(', *, '))
        self.requests.append(Request(*(a + [b] + c)))

    def make_file(self):
        f = open('requests.txt', 'w')
        f.write(self.__str__())

    def get_ids(self):
        return [request.ID for request in self.requests]

    def get_dates(self):
        return [request.DATE for request in self.requests]

    def get_client_ids(self):
        return [request.CLIENT_ID for request in self.requests]

    def get_equip_ids(self):
        return [request.EQUIP_ID for request in self.requests]

    def get_reasons(self):
        return [request.REASON for request in self.requests]

    def get_master_ids(self):
        return [request.MASTER_ID for request in self.requests]

    def get_works_ids(self):
        return [request.WORK_IDS for request in self.requests]

    def get_complete_dates(self):
        return [request.COMPLETE_DATE for request in self.requests]

    def get_delivery_dates(self):
        return [request.DELIVERY_DATE for request in self.requests]

    def get_costs(self):
        return [request.COST for request in self.requests]


class CardInBaseException(Exception):
    pass


class UnknownCommandException(Exception):
    pass


class ExitException(Exception):
    pass


class BadCommandException(Exception):
    pass

class UnknownFieldNameException(Exception):
    pass

class BadValueException(Exception):
    pass