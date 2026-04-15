# Checks the validity of any credit card number and identifies its type

MASTERCARD = 16
AMEX = 15
VISA_13 = 13
VISA_16 = 16

def main():
    # Get a credit card number from the user
    number = input("Number: ")

    # Check Mastercard then check sum
    if check_mastercard(number) == True:
        if checksum(number, MASTERCARD) == True:
            print("MASTERCARD.")
        else:
            print("INVALID.")
            return

    # Check Amex then check sum
    elif check_amex(number) == True:
        if checksum(number, AMEX) == True:
            print("AMEX.")
        else:
            print("INVALID.")
            return

    # Check Visa then check sum
    elif check_visa(number) == True:
        if checksum(number, VISA_13) == True:
            print("VISA.")
        elif checksum(number, VISA_16) == True:
            print("VISA.")
        else:
            print("INVALID.")
            return
    else:
        print("INVALID.")
        return


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
    """16-digit, begins 51-55"""
    if (len(num) == 16) and (int(num[0]) == 5) and (1 <= int(num[1]) <= 5):
        return True


def check_amex(num):
    """15-digit, begins 34 or 37"""
    if (len(num) == 15) and (int(num[0]) == 3) and (int(num[1]) == 4 or int(num[1]) == 7):
        return True


def check_visa(num):
    """13 and 16-digit, begin with 4"""
    if (len(num) == 13 or len(num) == 16) and (int(num[0]) == 4):
        return True



if __name__ == "__main__":
    main()