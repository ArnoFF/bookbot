def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")

def main():
    path = "books/frankenstein.txt"
    count_words(get_book_text(path))

main()



