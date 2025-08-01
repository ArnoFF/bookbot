from stats import get_num_words, get_num_characters, sort_char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    print(f"============ BOOKBOT ============ \n Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    get_num_words(get_book_text(path))
    print("--------- Character Count -------")
    char_dict = get_num_characters(get_book_text(path))
    char_list = sort_char_list(char_dict)
    for character in char_list:
        print(f"{character["char"]}: {character["num"]}")
    

    

main()



