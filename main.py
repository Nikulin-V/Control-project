from tools import *

r = Requests()
print(r.get_equip_ids())
r.add_request('157, 2017-11-22, 13, 176, Ne pokazyvaet nichego, 5, *, 15, 13, 17, *, 2017-11-29, '
              '2017-11-30, 2300;')
print(r)
r.make_file()
