a = input("Enter a Number: ")
print(f"Table of {a} : ")

try:
    for i in range(1, 11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Important lines")
print("Code End.")