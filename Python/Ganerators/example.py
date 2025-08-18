def even_num_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def even_num_list(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

#Using Generator
gen = even_num_generator(10)
print(next(gen))
print(next(gen))
print(next(gen))

#Using Regular Function
my_list = even_num_list(10)
print(my_list)