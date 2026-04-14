# Calculate a division and a sum

# NOTE: It is Pythonic to add more lines between functions in Python

x = int(input("x: "))
y = int(input("y: "))

# Truncation no longer an issue
z = x / y
print(z)

# 'format' string
print(f"{z:.50f}")

# Truncation solved, floating-point precision problem remains

# Define a helper function that prompts until user provides an int
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))   # return breaks you out of loop
        except ValueError:
            print("Not an integer")

# Define a the main function to sum two integers
def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x + y)


# Pythonic to call main at end, unlike in C
main()
