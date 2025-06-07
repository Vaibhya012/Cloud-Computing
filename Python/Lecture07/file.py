f = open("demo.txt", "r")

data = f.read()
# data = f.read(10)
print(data)
print(type(data))
f.close()