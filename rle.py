"""Demonstrate runlength endocing/decoding."""
import re


def main():
    """Drive the example."""
    encooded = "14A3B2C1D2A"
    decoded = ""

    # first attempt at decoding
    list1 = re.findall(r'\d+\D', encooded)
    for l in list1:
        count, char = int(l[0:-1]), l[-1]
        decoded += ''.join(count * char)
    print(decoded)

    # one-liner using regex for decoding!
    print(''.join([int(l[0:-1]) * l[-1] for l
                   in re.findall(r'\d+\D', encooded)]))

    # one liner using regex for encoding
    print(''.join([str(len(match[1])+1) + match[0] for match
                   in re.findall(r"(.)(\1*)", decoded)]))


if __name__ == "__main__":
    main()
