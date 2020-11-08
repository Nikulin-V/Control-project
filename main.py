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


def new_card(db, line, edit=False):
    if db == 'USER':
        p = People()
        new_person = Person(*line.split(', '))
        if (new_person.PHONE in p.get_phones() or new_person.ID in p.get_ids()) and not edit:
            raise CardInBaseException('user.txt')
        p.add_person(line)
        p.make_file()
    elif db == 'EQUIP':
        e = Equip()
        new_gadget = Gadget(*line.split(', '))
        if new_gadget.BRAND in e.get_brands() and new_gadget.MODEL == \
                e.get_models()[
                    e.get_brands().index(new_gadget.BRAND)] or new_gadget.ID in e.get_ids():
            raise CardInBaseException('equip.txt')
        e.add_equip(line)
        e.make_file()
    elif db == 'WORK':
        w = Works()
        new_work = Work(*line.split(', '))
        if new_work.WORK in w.get_works() or new_work.ID in w.get_ids():
            raise CardInBaseException('user.txt')
        w.add_work(line)
        w.make_file()


def edit_card(db, ID, line):
    if db == 'USER':
        f = open('people.txt')
        data = f.readlines()
        data.pop(People().get_ids().index(ID))
        f.close()
        f = open('people.txt', 'w')
        f.writelines(data)
        f.close()
    elif db == 'EQUIP':
        Equip().gadgets.pop(Equip().get_ids().index(ID))
        f = open('equip.txt')
        data = f.readlines()
        data.pop(Equip().get_ids().index(ID))
        f.close()
        f = open('equip.txt', 'w')
        f.writelines(data)
        f.close()
    elif db == 'WORK':
        Works().works.pop(Works().get_ids().index(ID))
        f = open('works.txt')
        data = f.readlines()
        data.pop(Works().get_ids().index(ID))
        f.close()
        f = open('works.txt', 'w')
        f.writelines(data)
        f.close()
    new_card(db, line, True)


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
    i = Requests().get_ids().index(ID)
    f = open('requests.txt')
    data = f.readlines()
    f.close()
    data = data[:i] + data[i+1:]
    f = open('requests.txt', 'w')
    f.writelines(data)
    f.close()


def request_in_requests(ID):
    for line in open('requests.txt').readlines():
        if line.split()[1] == str(ID):
            return True
    return False


def new_request():
    args = {
        'ID': '',
        'DATE': '',
        'CLIENT_ID': '',
        'EQUIP_ID': '',
        'REASON': '',
        'MASTER_ID': '',
        'WORK_IDS': '',
        'COMPLETE_DATE': '',
        'DELIVERY_DATE': '',
        'COST': ''
    }
    print('Выбирайте поля командой PUSH и вводите значения')
    print('+------------+')
    print('|Начало формы|')
    print('+------------+')
    for key, value in args.items():
        print(f'{key}: {str(value)}')
    print('+-----------+')
    print('|Конец формы|')
    print('+-----------+')
    while not all_filled(args):
        c = input()
        command = c.split()
        if len(command) == 2 and command[0] == 'PUSH' and command[1] in args.keys():
            value = input()
            if command[1] == 'ID':
                if value.isdigit() and int(value) not in Requests().get_ids():
                    args['ID'] = int(value)
                else:
                    raise BadValueException(value)
            elif command[1] in ['DATE', 'COMPLETE_DATE', 'DELIVERY_DATE']:
                x = value.split('-')
                if len(x) == 3 and (x[0] + x[1] + x[2]).isdigit() and len(x[0]) == 4 and \
                        len(x[1]) == 2 and len(x[2]) == 2 and 1 <= int(x[1]) <= 12 and 1 <= \
                        int(x[2]) <= 31:
                    args[command[1]] = value
            elif command[1] == 'CLIENT_ID':
                if value.isdigit() and int(value) in People().get_ids():
                    args['CLIENT_ID'] = int(value)
                else:
                    raise BadValueException(value)
            elif command[1] == 'EQUIP_ID':
                if value.isdigit() and int(value) in Equip().get_ids():
                    args['EQUIP_ID'] = int(value)
                else:
                    raise BadValueException(value)
            elif command[1] == 'REASON':
                args['REASON'] = value
            elif command[1] == 'MASTER_ID':
                if value.isdigit() and int(value) in \
                        People().get_ids() and 1 <= int(value) <= 20:
                    args['MASTER_ID'] = int(value)
                else:
                    raise BadValueException(value)
            elif command[1] == 'WORK_IDS':
                value = value.split()
                check = True
                for v in value:
                    if not v.isdigit() and int(v) in Works().get_ids():
                        check = False
                if check:
                    args['WORK_IDS'] = value
                else:
                    raise BadValueException(' '.join(value))
            else:
                raise UnknownFieldNameException(command[1])
            if args['WORK_IDS']:
                s = 0
                for work_id in args['WORK_IDS']:
                    s += Works().get_prices()[Works().get_ids().index(int(work_id))]
                args['COST'] = s
            print('+------------+')
            print('|Начало формы|')
            print('+------------+')
            for key, value in args.items():
                print(f'{key}: {str(value)}')
            print('+-----------+')
            print('|Конец формы|')
            print('+-----------+')
            if all_filled(args):
                Requests().add_request(f"{', '.join([value for value in args.values()])};")
                break
        else:
            raise UnknownCommandException(c)


def all_filled(args):
    check = True
    for value in args.values():
        if value == '':
            check = False
    return check


def main():
    command = input().split()
    if command[0] == 'HELP':
        if len(command) == 1:
            print_help()
        elif len(command) == 2:
            print_help(command[1])
    elif command[0] == 'NEW':
        if command[1] == 'REQUEST':
            new_request()
        else:
            new_card(command[1], ' '.join(command[2:]))

    elif command[0] == 'LIST' and len(command) == 2:
        list_db(command[1])
    elif command[0] == 'EDIT':
        edit_card(command[2], int(command[1]), command[1] + ', ' + ' '.join(command[3:]))
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
        Requests().make_file()
    elif command[0] == 'EXIT' and len(command) == 1:
        raise ExitException
    else:
        raise UnknownCommandException(f"'{' '.join(command)}'")


if __name__ == '__main__':
    while True:
        # noinspection PyBroadException
        try:
            main()
        except CardInBaseException as file_name:
            print(f'Карточка уже есть в {file_name}')
        except UnknownCommandException as command_line:
            print(f"Неизвестная команда {command_line}")
        except ExitException:
            print('Выход...')
            break
        except UnknownFieldNameException as field_name:
            print(f'Неизвестное поле {field_name}')
        except BadValueException as bad_value:
            print(f'Неверное значение {bad_value}')
        except TypeError as e:
            print(e)
            print('Неизвестная команда')
        except Exception:
            print(Exception.__class__.__name__)
        finally:
            print('----------------------------------------------\n')
new_request()
