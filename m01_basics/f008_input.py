name = input("Enter your name: ")  # prompt is optional, by deafult ''

print(name, type(name))
print("My name is", name, sep=":")  # :

# method 1
out = "My name is" + ":" + name
print(out)

print(f"My name is:{name}")
