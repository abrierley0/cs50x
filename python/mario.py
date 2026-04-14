# Prints mario stairs

def main():

    # Prompt user for pyramid height
    height = get_int("Height: ")

    # Print pyramid of size height
    stairs(height)


# Gets a valid integer
def get_int(prompt):
    while True: # Keep running loop unless broken
        try:
            num = int(input(prompt))
            if 1 <= num <= 8:
                return num
            print("Height must be between 1 and 8")
        except:
            print("Please enter a valid integer.")

# Prints pyramid of size height
def stairs(int):
    for i in range(int):
        print(" " * (int - (i + 1)), end="")
        print("#" * (i + 1))


main()