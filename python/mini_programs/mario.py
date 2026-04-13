# Prints mario-like stairs

from cs50 import get_int

# Pythonic to deliberately induce an infinite loop
while True:
    n = get_int("Height: ")
    if n > 0:
        break

for i in range(n):
    print("#")

for i in range(n):
    print("?", end="")
print()

print("?" * n)

# Print mario bricks
for i in range(n):
    for j in range(n):
        print("#", end="")
    print()

print()

for i in range(n):
    print("#" * n)

