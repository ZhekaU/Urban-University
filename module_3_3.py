def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    


print_params()  # Вызов без аргументы
print_params(55)  # Вызов с одним аргументом
print_params(55, 'Новая строка')  # Вызов с двумя аргументом
print_params(55, 'Новая строка', False)  # Вызов с тремя аргументом
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 'Новосибирск', 1.5]
values_dict = {'a': 500, 'b': 'Моя строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [14,'Сатурн']
print_params(*values_list_2, 42)