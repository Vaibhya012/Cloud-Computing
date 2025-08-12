try:
    result = 10/0   #This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by Zero")
else:
    print("Division successful: ", result)
finally:
    print("Execution finished")