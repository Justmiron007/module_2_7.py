def print_params(a=1, b='red', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [25, 'red', [5, 6]]
values_dict = {'a': 2, 'b': 'green', 'c': [1, 2]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [100, 'blue']
print_params(*values_list_2, 42)