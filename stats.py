def get_num_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")


def get_num_characters(text):
    text_lower_case = text.lower()
    characters = {}
    for letter in text_lower_case:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters
    
