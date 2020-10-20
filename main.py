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
