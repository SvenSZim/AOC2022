"""
A program to convert the content of the txt into usable data
for the main program
"""
rawdata: str
with open('data.txt', 'r') as data:
    rawdata = data.read()


def convert_data_for_puzzle_one() -> str:
    """
    functions as outsorcing of reading in the one string of characters
    of the input data

    Returns:
        str: first row in data
    """
    return rawdata.splitlines()[0]


def main() -> None:
    """
    Function for testing purposes
    """
    print(convert_data_for_puzzle_one())


if __name__ == '__main__':
    main()
