from stats import count_words
from stats import count_characters
from stats import sorted_dict

import sys

def get_book_text():
    path_to_file = sys.argv[1] 
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    raw_text = get_book_text()
    count_characters(raw_text)
    word_count = count_words(raw_text)
    x = sorted_dict(count_characters(raw_text))
    print_report(raw_text, x)

def print_report(raw_text, x):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}\n----------- Word Count ----------")
    print(f"Found {count_words(raw_text)} total words")
    print("--------- Character Count -------")
    for dict in x:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()