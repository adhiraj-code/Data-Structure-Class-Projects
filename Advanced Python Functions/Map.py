def my_func(a, b):
    return a + ':' + b

data = map(my_func, ('dog', 'cat', 'cherry'), ('barks', 'meow', 'blossom'))
print(list(data))