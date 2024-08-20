def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params(3, 'пайтон', False)
print_params(2,'Урбан')
print_params(a = 4)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [21, 'Земля', False]
values_dict = {'a': 52, 'b': 'Луна','c': True}
print_params(*values_list)
print_params(**values_dict) # получилось только отдельно распаковать

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)