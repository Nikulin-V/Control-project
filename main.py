from tools import *


def search_u(text):
    p = People()
    f = open('SEARCH_U.txt', 'w')
    for person in p.people:
        if text in person.NAME or text in person.PHONE:
            f.write(person.__str__() + '\n')

search_u('Vesnin')