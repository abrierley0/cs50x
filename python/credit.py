# Checks credit card number

# Length of Mastercard numbers
MASTERCARD = 16

# Length of AMEX numbers
AMEX = 15

def main():
    # Get a credit card number from the user
    number = input("Number: ")

    # Checks length and first few numbers then applies Luhn's algorithm
    if check_mastercard(number) and checksum(number, MASTERCARD):
        print("MASTERCARD.")

    # ''
    elif check_amex(number) and checksum(number, AMEX):
        print("AMEX.")

    # ''
    elif check_visa(number) and checksum(number, 13):
        print("VISA.")

    # ''
    elif check_visa(number) and checksum(number, 16):
        print("VISA.")

    else:
        print("INVALID")


def checksum(num, length):
    """Apply Luhn's algorithm"""
    length = int(length)
    num = int(num)
    off_sum = 0
    on_sum = 0

    for i in range(length // 2):    # NOTE: floor/integer division
        # Double second from last digit
        off_digit = 2 * int((num // 10) % 10)
        off_sum += (off_digit // 10) + (off_digit % 10)

        # Last digit
        on_sum += num % 10

        # Remove last two digits
        num = num // 100

    # Extra on-digit for odd-numbered cards
    if length % 2 == 1:
        on_sum += num % 10

    total = on_sum + off_sum
    return total % 10 == 0


def check_mastercard(num):
    """Checks if number matches Mastercard - i.e. 16-digit and begins 51-55"""
    if (len(num) == 16) and (int(num[0]) == 5) and (1 <= int(num[1]) <= 5):
        return True
    return False


def check_amex(num):
    """Checks if number matches Amex- i.e. 15-digit and begins 34 or 37"""
    if (len(num) == 15) and (int(num[0]) == 3) and (int(num[1]) == 4 or int(num[1]) == 7):
        return True
    return False


def check_visa(num):
    """Checks if number matches Visa - i.e. 13- or 16-digit and begins with 4"""
    if (len(num) == 13 or len(num) == 16) and (int(num[0]) == 4):
        return True
    return False



if __name__ == "__main__":
    main()