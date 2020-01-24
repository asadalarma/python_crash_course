# working with list manipulation
numbers = [1,23,45,6,7,8,34,67,90,23]
friends = ["kevin","Richerdson","Jim","oscar","tom","ridar"]


# Append function adds item in the end 

friends.append("Creed")
print(friends)


# Insert in particular position

friends.insert(1,"Jelly")
print(friends)


# Remove item in the list

friends.remove("Creed")
print(friends)


# Remove all elements in the list

friends.index("Jim")
print(friends)

# sort the list in ascending order
friends.sort()
print(friends)

# use of extend function in list 

friends.extend(numbers)
print(friends)


# Pop function delete last item in the list

friends.pop()
print(friends)

# count the elements in the list

print(friends.count("Jim"))





# Reverse function reverse the numbers
numbers.reverse()
print(numbers)


# copy function
numbers2 =numbers.copy()
print(numbers2)

friends2 = friends.copy()
print(friends2)


# Remove all elements in the list

friends.clear()
print(friends)
