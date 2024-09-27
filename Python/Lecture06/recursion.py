# n = int(input("Enter your No. "))

# #Recursive Function
# def show(n):
#     if(n==0):  #Base case
#         return
#     print(n)
#     show(n-1)
#     print(n+1)  #stack down

# show(n)

# n = int(input("Enter your No. "))

# def fact(x):
#     if(x==0 or x==1):
#         return 1
#     else:
#         return fact(x-1)*x
    
# fact = fact(n)
# print(fact)



# PRACTICE Q1

# n = int(input("Enter your No. "))

# def calcSum(x):
#     if(x == 0):
#         return 0
#     return calcSum(x-1) + x

# sum = calcSum(n)
# print(sum)

# PRACTICE Q2

nums = [5,6,5,4,2,8,6,2]

def printList (list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    printList(list, idx+1)

printList(nums)