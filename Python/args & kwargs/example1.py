def sum_numbers(*args):
    total = sum(args)
    return total

print(sum_numbers(1, 2, 3))

print(sum_numbers(10, 20, 30, 40))

print(sum_numbers(*[5, 15, 25]))