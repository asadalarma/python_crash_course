# Working with strings

print("Hello Graffe")

#when you want to print quotation mark use backslash
print("Hello \" Graffe")

# using variable
phrase = "Hello \" Graffe"
print(phrase)

# concat
phrase2 = "Hello \" Graffe"
print(phrase2 + " very cool")

# string to lower
phrase2 = "Graffe Academy"
print(phrase2.lower())

# string to upper
phrase2 = "graffe academy"
print(phrase2.upper())

# check string is upper case or not
phrase2 = "graffe academy"
print(phrase2.isupper())

# convert to upper and then check string is upper case or not
phrase2 = "graffe academy"
print(phrase2.upper().isupper())

# length of a string
phrase2 = "graffe academy"
print(len(phrase2))


# indexes of a string
phrase2 = "giraffe academy"
print(phrase2[0])

# give the index of a string
phrase2 = "Giraffe Academy"
print(phrase2.index("G"))

# give the index of a string
phrase2 = "Giraffe Academy"
print(phrase2.index("a"))

# give the index of a string
phrase2 = "Giraffe Academy"
print(phrase2.index("Acad"))

# replace the string
phrase2 = "Giraffe Academy"
print(phrase2.replace("Giraffe","Elephant"))