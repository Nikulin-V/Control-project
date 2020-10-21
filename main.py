from tools import *


def search_u(text):
    p = People()
    f = open('SEARCH_U.txt', 'w')
    for person in p.people:
        if text in person.NAME or text in person.PHONE:
            f.write(person.__str__() + '\n')


def search_e(text):
    e = Equip()
    f = open('SEARCH_E.txt', 'w')
    for gadget in e.gadgets:
        if text in gadget.MODEL:
            f.write(gadget.__str__() + '\n')


def search_w(text):
    w = Works()
    f = open('SEARCH_W.txt', 'w')
    for work in w.works:
        if text in work.WORK and not work.WORK.isdigit() or text in str(work.PRICE):
            f.write(work.__str__() + '\n')


def new_card(db):
    if db == 'USER':
        p = People()
        line = input('Введите карточку: ')
        new_person = Person(*line.split())
        if new_person.PHONE in p.get_phones() or new_person.ID in p.get_ids():
            raise CardInBaseException('user.txt')
        p.add_person(new_person)
    elif db == 'EQUIP':
        e = Equip()
        line = input('Введите карточку: ')
        new_gadget = Gadget(*line.split())
        if new_gadget.BRAND in e.get_brands() and new_gadget.MODEL == \
                e.get_models()[
                    e.get_brands().index(new_gadget.BRAND)] or new_gadget.ID in e.get_ids():
            raise CardInBaseException('equip.txt')
        e.add_equip(new_gadget)
    elif db == 'WORK':
        w = Works()
        line = input('Введите карточку: ')
        new_work = Work(*line.split())
        if new_work.WORK in w.get_works() or new_work.ID in w.get_ids():
            raise CardInBaseException('user.txt')
        w.add_work(new_work)


def edit_card(db, ID):
    if db == 'USER':
        People().people.pop(People().get_ids().index(ID))
    elif db == 'EQUIP':
        Equip().gadgets.pop(Equip().get_ids().index(ID))
    elif db == 'WORK':
        Works().works.pop(Works().get_ids().index(ID))
    new_card(db)


def print_card(db, ID):
    if db == 'USER':
        print(People().people[People().get_ids().index(ID)])
    elif db == 'EQUIP':
        print(Equip().gadgets[Equip().get_ids().index(ID)])
    elif db == 'WORK':
        print(Works().works[Works().get_ids().index(ID)])


def list_db(db):
    if db == 'USER':
        print(People())
    elif db == 'EQUIP':
        print(Equip())
    elif db == 'WORK':
        print(Works())
