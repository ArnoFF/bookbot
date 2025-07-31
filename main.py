from stats import get_num_words, get_num_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    get_num_words(get_book_text(path))
    characters = get_num_characters(get_book_text(path))
    for key in characters:
        print(f"'{key}': {characters[key]}")

main()



