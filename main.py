from datetime import *

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


def new_card(db, line):
    if db == 'USER':
        p = People()
        new_person = Person(*line.split())
        if new_person.PHONE in p.get_phones() or new_person.ID in p.get_ids():
            raise CardInBaseException('user.txt')
        p.add_person(new_person)
    elif db == 'EQUIP':
        e = Equip()
        new_gadget = Gadget(*line.split())
        if new_gadget.BRAND in e.get_brands() and new_gadget.MODEL == \
                e.get_models()[
                    e.get_brands().index(new_gadget.BRAND)] or new_gadget.ID in e.get_ids():
            raise CardInBaseException('equip.txt')
        e.add_equip(new_gadget)
    elif db == 'WORK':
        w = Works()
        new_work = Work(*line.split())
        if new_work.WORK in w.get_works() or new_work.ID in w.get_ids():
            raise CardInBaseException('user.txt')
        w.add_work(new_work)


def edit_card(db, ID, line):
    if db == 'USER':
        People().people.pop(People().get_ids().index(ID))
    elif db == 'EQUIP':
        Equip().gadgets.pop(Equip().get_ids().index(ID))
    elif db == 'WORK':
        Works().works.pop(Works().get_ids().index(ID))
    new_card(db, line)


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


def create_report():
    f = open('reports.txt', 'w')
    lines = []
    now = datetime.now()
    for request in Requests().requests:
        if datetime(*list(map(int, request.COMPLETE_DATE.split('-')))) <= now < datetime(
                *list(map(int, request.DELIVERY_DATE.split('-')))):
            email = People().get_emails()[People().get_ids().index(request.CLIENT_ID)]
            brand = Equip().get_brands()[Equip().get_ids().index(request.EQUIP_ID)]
            model = Equip().get_models()[Equip().get_ids().index(request.EQUIP_ID)]
            lines.append(f'{email}, {brand}, {model}, {request.COMPLETE_DATE};\n')
    f.write('\n'.join([line for line in lines]))
    f.close()


def create_inwork(master_name):
    f = open('inwork.txt', 'w')
    now = datetime.now()
    for request in Requests().requests:
        if People().get_names()[People().get_ids().index(request.MASTER_ID)] == master_name and \
                datetime(*list(map(int, request.COMPLETE_DATE.split('-')))) < now:
            brand = Equip().get_brands()[Equip().get_ids().index(request.EQUIP_ID)]
            model = Equip().get_models()[Equip().get_ids().index(request.EQUIP_ID)]
            f.write(f'{request.DATE}, {request.ID}, {brand}, {model}, {request.REASON};\n')
    f.close()


def print_help(command=''):
    f = open('help.txt', encoding='utf-8')
    data = f.readlines()
    if not command:
        for line in data:
            print(line.strip('\n'))
    elif command.startswith('HELP'):
        print(''.join(data[:2]))
    elif command.startswith('NEW'):
        print(data[2])
        print(''.join(data[9:12]))
    else:
        for line in data:
            if line.startswith(command):
                print(line.split('\n'))
                break


def del_request(ID):
    Requests().requests.pop(Requests().get_ids().index(ID))


def new_request():
    pass


def main():
    command = input().split()
    if command[0] == 'HELP':
        if len(command) == 1:
            print_help()
        elif len(command) == 2:
            print_help(command[1])
    elif command[0] == 'NEW':
        if len(command) == 3:
            new_card(command[1], command[2])
        elif command[1] == 'REQUEST':
            new_request()
    elif command[0] == 'LIST' and len(command) == 2:
        list_db(command[1])
    elif command[0] == 'EDIT' and len(command) == 4:
        edit_card(int(command[2]), command[1], command[3])
    elif command[0] == 'PRINT' and len(command) == 3:
        print_card(command[2], int(command[1]))
    elif command[0] == 'FIND_U' and len(command) == 2:
        search_u(command[1])
    elif command[0] == 'FIND_E' and len(command) == 2:
        search_u(command[1])
    elif command[0] == 'FIND_W' and len(command) == 2:
        search_u(command[1])
    elif command[0] == 'DEL' and len(command) == 2:
        del_request(int(command[1]))
    elif command[0] == 'EXIT' and len(command) == 1:
        raise ExitException
    else:
        raise UnknownCommandException(f"'{' '.join(command)}'")


if __name__ == '__main__':
    while True:
        try:
            main()
        except CardInBaseException as file_name:
            print(f'Карточка уже есть в {file_name}')
        except UnknownCommandException as command_line:
            print(f"Неизвестная команда {command_line}")
        except ExitException:
            print('Выход...')
            break
        except TypeError:
            print('Неизвестная команда')
        except Exception:
            print(Exception.__class__.__name__)
        finally:
            print('----------------------------------------------\n')