from sys import argv

# Check for two command-line arguments
if len(argv) == 2:  # Command 'python' is ignored
    print(f"hello, {argv[1]}")
else:
    print("hello, world")