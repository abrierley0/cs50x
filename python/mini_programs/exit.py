import sys

# Check for two command-line arguments
if len(sys.argv) != 2:
    print("Missing command-line argument.")
    sys.exit()

# Print the second command-line argument
print(f"hello, {sys.argv[1]}")
sys.exit(0)