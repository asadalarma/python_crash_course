# Mutiple types of print

var = "abc"
variable1 ="asdf"

# print using f string

print("Hello "f"{var}")
print(f"{var}")
print(f"Hello {var}")

# print using comma
print("Hello",var,variable1)

# print using format
print("If there was a birth every 7 seconds, there would be: {} births".format(var))

# print using %
print('I have %s %s' %(var,variable1))

# print using concatenation

print('I have '+ var + variable1)
