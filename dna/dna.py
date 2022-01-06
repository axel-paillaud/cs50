import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py [datafile][sequence]")


    # TODO: Read database file into a variable
    data = []
    fdata = open(sys.argv[1], 'r')
    reader = csv.DictReader(fdata)
    for row in reader:
        for valeur in row.values():
            if valeur.isdigit() == True:
                valeur = int(valeur)
        data.append(row)

    for row in data:
        for valeur in row.values():
            tmp = 0
            if valeur.isdigit() == True:
                print(valeur)
                tmp = valeur + tmp
                print(tmp)



    # TODO: Read DNA sequence file into a variable
    fSTR = open(sys.argv[2], 'r')
    STR = fSTR.read()


    # TODO: Find longest match of each STR in DNA sequence
    AGATC = "AGATC"
    TTTTTTCT = "TTTTTTCT"
    AATG = "AATG"
    TCTAG = "TCTAG"
    GATA = "GATA"
    TATC = "TATC"
    GAAA = "GAAA"
    TCTG = "TCTG"

    dataSTR = []

    long_AGATC = longest_match(STR, AGATC)
    dataSTR.append(long_AGATC)

    long_TTTTTTCT = longest_match(STR, TTTTTTCT)
    dataSTR.append(long_TTTTTTCT)

    long_AATG = longest_match(STR, AATG)
    dataSTR.append(long_AATG)

    long_TCTAG = longest_match(STR, TCTAG)
    dataSTR.append(long_TCTAG)

    long_GATA = longest_match(STR, GATA)
    dataSTR.append(long_GATA)

    long_TATC = longest_match(STR, TATC)
    dataSTR.append(long_TATC)

    long_GAAA = longest_match(STR, GAAA)
    dataSTR.append(long_GAAA)

    long_TCTG = longest_match(STR, TCTG)
    dataSTR.append(long_TCTG)


    # TODO: Check database for matching profiles

    return


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
