def get_book_text():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)


def main():
    get_book_text()
    count_words()


def count_words():
    raw_words = get_book_text()
    word_list = raw_words.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")

main()