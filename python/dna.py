# Identifies a person from their raw DNA

import csv
import sys


def main():

    # User must input a database file with DNA records, and a text file with raw DNA, as CL arguments
    if len(sys.argv) != 3:
        print("Requires two command-line arguments.")
        sys.exit()

    # Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # Read raw DNA text file into a variable
    with open(sys.argv[2]) as file:
        person = file.read()

    # Find the longest contiguous appearance of each DNA sequence
    longest_runs = []
    sequences = len(reader.fieldnames) - 1
    for i in range(sequences):
        longest_run = longest_match(person, reader.fieldnames[i+1])
        longest_runs.append(longest_run)

    # Check if frequencies match any records
    for i in range(len(rows)):
        if longest_runs == [int(rows[i][j]) for j in reader.fieldnames[1:]]:
            print(rows[i]['name'])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
