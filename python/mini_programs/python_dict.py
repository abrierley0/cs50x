# Searches a list of contacts and returns a phone number

# Global list of dictionaries
people = [ 
    {"name": "Carter", "number": "+1-617-495-1000"},    # Each entry like a data struct in C
    {"name": "David", "number": "+1-618-495-1000"},
    {"name": "John", "number": "+1-6949-468-2750"},
]

name = input("Name: ")


# Search list of names and return corresponding number
for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}.")
        break
else:
    print("Not found.")


# More Pythonic
for person in people:
    if person["name"] == name:
        print(f"Found {person['number']}.")  # Put anything in {}, but use ''
        break 
else:
    print("Not found.")