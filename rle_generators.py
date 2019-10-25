"""Example using generators for run length encode/decode."""


def rleunits(str1):
    """Generate run length encoded units."""
    current = None
    count = 0

    for letter in str1:
        if letter == current:
            count += 1
        else:
            if current:
                yield str(count)+current
            count = 1
            current = letter


def rldunits(str1):
    """Generate run length decoded units."""
    count = None

    for c in str1:
        if c.isdigit():
            if not count:
                count = c
            else:
                count += c
        else:
            yield(c * int(count))
            count = None


def main():
    """Drive the example."""
    str1 = "AAAABBBBCDDEEFFFFFFFFFFF"

    encoded = ''.join(rleunits(str1))
    print(encoded)

    unencoded = ''.join(rldunits(encoded))
    print(unencoded)


main()
