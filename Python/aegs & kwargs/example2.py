def show_profile(**kwargs):
    print(f"Name : {kwargs.get('name')}")
    print(f"Age : {kwargs.get('age')}")
    print(f"City : {kwargs.get('city')}")

show_profile(name="Vaibhav", age=23, city="Pune")

show_profile(**{'name': 'Atharv', 'age': 20, 'city': 'Sambhajinagar'})