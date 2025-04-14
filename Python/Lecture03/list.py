marks = [95,85,76,94,74.5,87]

print(marks)
print(marks[0])
print(marks[2])
print("lenth of List", len(marks))
# marks[4] = "Vaishnavi"
print(marks)
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

marks.append(90)
marks.sort()
marks.sort(reverse=True)
marks.reverse()
marks.insert(2, 80)
marks.remove(90)
marks.pop(2)
print(marks)

