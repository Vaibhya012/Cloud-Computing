# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# n = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(i*n)
#     i += 1

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx <= len(num) -1:
#     print(num[idx])
#     idx += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
n = int(input("Enter num: "))
i = 0
while i <= len(nums) -1:
    if(nums[i] == n):
        print("Match Number: ", n)
        break
    else:
        print("Matching...")     
    i += 1

