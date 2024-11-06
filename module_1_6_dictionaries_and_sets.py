my_dict = {'Andrey': 1996, 'Max': 1999, 'Alex': 1998, 'Gleb': 2000}
print(my_dict)
print (my_dict ['Max'], my_dict.get('Dima', 2001))
print(my_dict)
my_dict.update({'Nastya': 1998, 'Nikita': 1999})
print(my_dict)
n = my_dict.pop('Nastya')
print(n)
print(my_dict)


my_set = {1, 2, 2, True, 3, 4, 5, 5, 6, 7, 8, 9, False, 'VK'}
print(my_set)
my_set.add(487)
my_set.add(149)
my_set.discard(True)
my_set.remove(2)
print(my_set)