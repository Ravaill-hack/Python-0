
import sys


def count_things(raw_text: str):
    """
    Calcule les sommes
    """
    nb_upper: int = 0
    nb_lower: int = 0
    nb_ponct: int = 0
    nb_space: int = 0
    nb_digit: int = 0
    ponctuation_str = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for c in raw_text:
        if c.isupper():
            nb_upper += 1
        if c.islower():
            nb_lower += 1
        if c.isdigit():
            nb_digit += 1
        if c == " " or c == "\n":
            nb_space += 1
        if c in ponctuation_str:
            nb_ponct += 1
    return (nb_upper, nb_lower, nb_ponct, nb_space, nb_digit)


def print_sums(raw_text: str):
    """
    Affiche les sommes
    """
    nb_letters: int = len(raw_text)

    results = count_things(raw_text)
    nb_upper = results[0]
    nb_lower = results[1]
    nb_ponct = results[2]
    nb_space = results[3]
    nb_digit = results[4]

    print(f"The text contains {nb_letters} characters:")
    print(f"{nb_upper} upper letters")
    print(f"{nb_lower} lower letters")
    print(f"{nb_ponct} punctuation marks")
    print(f"{nb_space} spaces")
    print(f"{nb_digit} digits")


def main():
    """
    Execution du programme.
    """
    try:
        args = sys.argv
        assert len(args) <= 2
        if (len(args) == 1):
            print("What is the text to count?")
            print("Hello World!")
            print_sums("Hello World!\n")
        else:
            print_sums(args[1])

    except (AssertionError):
        print("AssertionError : there must be one and only one input")


if __name__ == "__main__":
    main()
