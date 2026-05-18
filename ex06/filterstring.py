
from ft_filter import ft_filter
import sys

def is_even(num):
    """
    Fonction test qui renvoie True si un nombre est pair et False sinon.
    """
    return num % 2 == 0


def main():
    """
    Execution du programme.
    """
    try:
        args = sys.argv
        assert len(args) == 3
        assert type(args[1]) == str
        assert args[2].isdigit()
        splited = args[1].split()
        filtered = list(ft_filter(lambda word: len(word) > int(args[2]), splited))
        print(filtered)

    except (AssertionError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
