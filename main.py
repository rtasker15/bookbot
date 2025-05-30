from stats import count_words
from stats import count_characters

def get_book_text():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)


def main():
    raw_text = get_book_text()
    count_characters(raw_text)
    count_words(raw_text)


main()