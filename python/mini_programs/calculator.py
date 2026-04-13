# Calculate a division

x = int(input("x: "))
y = int(input("y: "))

# Truncation no longer an issue
z = x / y
print(z)

# 'format' string
print(f"{z:.50f}")

# Truncation solved, floating-point precision problem remains

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))   # return breaks you out of loop
        except ValueError:
            print("Not an integer")


def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x + y)


main()

# Pythonic to add more lines between functions in Python
