def decorator(func):
    def wrapper():
        print("Write mail")
        func()
        print("recevided a mail")
    return wrapper

@decorator
def hello():
    print("sending mail....")

hello()