# Convert input to uppercase manually

# Demonstrate loops in Python
i = 0

# while loop
while i < 3:
    print("meow")
    i += 1

# for loop
for i in [0, 1, 2]:
    print("hello, world")

# Most Pythonic way to write this
for i in range(3):  # range function
    print("hello, world")

# More Pythonic
for _ in range(3):
    print("hello, world")

# while True:
#     print("meow")

# Override default newline
before = input("Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(), end="")
print()

# Applying upper to each character is unnecessary in Python
before = input("Before: ")
print("After: ", end="")
print(before.upper())

# More Pythonic
before = input("Before: ")
after = before.upper()
print(f"After: {after}")

# Even more Pythonic
before = input("Before: ")
print(f"After: {before.upper()}")

