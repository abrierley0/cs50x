# Counts the minimum number of coins required for customer's change

from cs50 import get_float


def main():
    # Get user's amount of change
    while True:
        try:
            change = get_float("Change: ")
            if change > 0:
                break
            print("Enter positive change.")
        except:
            print("Please enter a valid float")

    # Convert to pennies
    change = int(change * 100)

    # Count quarters
    quarter_count, remaining = count_quarters(change)

    # Count dimes
    dime_count, remaining = count_dimes(remaining)

    # Count nickels
    nickel_count, remaining = count_nickels(remaining)

    # Count pennies
    penny_count = count_pennies(remaining)

    # Return coin count
    count = quarter_count + dime_count + nickel_count + penny_count

    print(count)


def count_quarters(float):
    count = float // 25
    remaining = float - (count * 25)
    return count, remaining


def count_dimes(float):
    count = float // 10
    remaining = float - (count * 10)
    return count, remaining


def count_nickels(float):
    count = float // 5
    remaining = float - (count * 5)
    return count, remaining


def count_pennies(float):
    count = int(float // 1)
    return count


if __name__ == "__main__":
    main()