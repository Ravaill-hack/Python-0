
import sys

NESTED_MORSE={" ": "/ ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        ",": "--..-- ",
        ".": ".-.-.- ",
        "?": "..--.. ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. "
}


def main():

    result: str = ""
    try:
        args = sys.argv
        assert len(args) == 2
        raw_str = args[1].upper()
        for c in raw_str:
            result += (NESTED_MORSE[c])
        print (result)

    except (AssertionError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()