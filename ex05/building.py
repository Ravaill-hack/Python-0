
import sys

# def check_args(args: str[]):


def count_something(raw_text: str, low_bound: int, high_bound: int):


def print_sums(raw_text: str):
    """
    Calcule et affiche les sommes
    """
    nb_letters: int = len(raw_text)
    nb_upper: int = 0
    nb_lower: int = 0
    nb_ponct: int = 0
    nb_space: int = 0
    nb_digit: int = 0

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
    args = sys.argv[1:]
    print(args[0])
    print_sums(args[0])


if __name__ == "__main__":
    main()
