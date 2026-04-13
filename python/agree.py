# Asks if user agrees

# Demonstrates methods
s = input("Do you agree? ").lower()

# Make user input uniform
# s = s.lower()

# Check user input
# if s == "Y" or s == "y":
#     print("Agreed.")
# elif s == "N" or s == "n":
#     print("Not agreed.")

# Check for errors in user input using array
# if s in ["y", "yes", "Y", "Yes", "YeS", "YEs"]:
#     print("Agreed")
# elif s in ["n", "no"]:
#     print("Not agreed")

if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")


