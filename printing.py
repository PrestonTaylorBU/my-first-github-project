# Preventing new line from print
print("On a line;", end="")
print(" On the same line")

# Printing using format strings
name = "Preston"
age = 22
subject = "Computer Science"
print(f"Name = {name}, Age = {22}, Subject = {subject}, Age Doubled = {age*2}")

# Printing using format func
print("Name = {}, Age = {}, Subject = {}, Age Doubled = {}".format(name, age, subject, age*2))