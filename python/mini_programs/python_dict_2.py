#  Search one big dictionary

# One big dictionary, rather than a list of dictionaries: no name or number keys
people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-618-495-1000",
    "John": "+1-6949-468-2750",
}

name = input("Name: ")

# Check name in dict, if yes, return corresponding number
if name in people:
    number = people[name]
    print(f"Found {number}.")
else:
    print("Not found.")


