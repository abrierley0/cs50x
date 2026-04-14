# Searches a list of contacts

names = ["Carter", "David", "John"]

name = input("Name: ")

# PYTHON CAN HAVE ELSE CLAUSE IN A FOR LOOP
#__________________________________________________
for n in names:
    if name == n:
        print("Found.")
        break

else:
    print("Not found.")
#___________________________________________________


# More Pythonic way
# No need to loop through list
#_____________________________________________________
if name in names:   # LINEAR SEARCH
    print("Found.")
else:
    print("Not found.")
#_____________________________________________________