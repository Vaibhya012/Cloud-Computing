import time

def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"'{func.__name__}' ran in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def long_running_function(n):
    total = 0
    for  i in range(n):
        total += 1
    return total

long_running_function(1000000000)