# Prints a half-pyramid of height 1-8 inclusive

def main():
    # Prompt user for height
    height = get_int("Height: ")

    # Print half-pyramid
    stairs(height)


def get_int(prompt):
    """ Prompts user for an integer until input is valid"""
    while True: # Keep running loop unless broken
        try:
            num = int(input(prompt))
            if 1 <= num <= 8:
                return num
            print("Height must be between 1 and 8")
        except:
            print("Please enter a valid integer.")


def stairs(int):
    """Prints a half-pyramid of size height"""
    for i in range(int):
        spaces = int - (i + 1)
        hashes = i + 1
        print(" " * spaces + "#" * hashes)


if __name__ == "__main__":
    """ Prevents the file running automatically on import"""
    main()