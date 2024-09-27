#function definition
def calcSum(a, b): #parameters
    sum = a + b
    print(sum)

#function call
calcSum(5, 7) #arguments
calcSum(5, 8)
calcSum(5, 9)

def printHello():
    print("Hello World")

printHello()
printHello()


def calcAvg(a, b, c):
    sum = a+b+c
    avg = sum/3
    return avg

avg = calcAvg(2,5,9)
print(avg)