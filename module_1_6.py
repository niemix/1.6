my_dict = {'Eva': 1999, 'Sonya': 2009}
print(my_dict)
print(my_dict.get('Eva'))
print(my_dict.get('Natasha'))
print(my_dict.get('Natasha', 'Такого ключа нет'))
my_dict['Alex'] = 1988
my_dict['mom'] = 1976
del my_dict['Alex']
print(my_dict)

my_set = {6, 9, 6, 8, 9, 1, 1, 's', 's', 'f', 'f', 'cat', 'dog', 'cat'}
print(my_set)
my_set.add(5)
my_set.add('hare')
my_set.remove(1)
print(my_set)