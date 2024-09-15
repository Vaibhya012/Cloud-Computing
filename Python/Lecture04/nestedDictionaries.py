stud = {
    "name" : "Vaishu Patil",
    "score" : {
        "phy" : 80,
        "chem" : 85.5,
        "math" : 84
    }
}

# print(stud["score"]["math"])
# print(stud.keys())
# print(stud.values())
# print(stud.items())
new_dict = {"age" : 22, "city" : "Sambhajinagar"}

stud.update(new_dict)
print(stud)