my_dict = {'Sasha' : 1991 , 'Masha' : 1987}
print(my_dict)
print(my_dict .get('Sasha'))
print(my_dict .get('Ivan'))
my_dict .update({'Ivan' : 1998 , 'Slava' : 1987 })
del_ = my_dict .pop('Masha')
print(del_)
print(my_dict)
#
my_set = {1, 2, 3, 1, 2, 3, 'Саша', 'Маша', 'Саша', 'Маша'}
print(my_set)
my_set .add(5)
my_set .add(False)
my_set .discard(1)
print(my_set)
