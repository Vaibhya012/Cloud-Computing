# for i in range(1, 10):
#     pass

# print("Some useful work")

# n = int(input("Enter Num: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("Total Sum",sum)

n = int(input("Enter Num: "))
fac = 1
for i in range(1, n+1):
    fac *= i

print("Total Factorial",fac)