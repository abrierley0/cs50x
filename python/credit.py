# Identifies a credit card number

MASTERCARD = 16
AMEX = 15
VISA_13 = 13
VISA_16 = 16

def main():
    # Get a credit card number from the user
    number = input("Number: ")

    if check_mastercard(number) == True:
        if checksum(number, MASTERCARD) == True:
            print("MASTERCARD.")
        else:
            print("INVALID.")

    check_amex(number)

    check_visa(number)


def checksum(num, length):
    """Apply Luhn's algorithm"""
    length = int(length)
    num = int(num)
    off_sum = 0
    on_sum = 0
    for i in range(int(length / 2.0)):
        off_digit = 2 * int((num / 10) % 10)
        off_sum = off_sum + (int(off_digit / 10)) + (int(off_digit % 10))
        on_sum = on_sum + int(num % 10)
        num = num / 100
        #print(off_digit)
    #print(int(off_sum))
    check = int((int(off_sum) + int(on_sum)) % 10)
    if check == 0:
        return True
    else:
        return False




def check_mastercard(num):
    """16-digit, begins 51-55"""
    if len(num) == 16:
        #print("Mastercard has correct length.")
        return True


def check_amex(num):
    """15-digit, begins 34 or 37"""


def check_visa(num):
    """13 and 16-digit, begin with 4"""


if __name__ == "__main__":
    main()