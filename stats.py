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
    
def sort_char_list(character_list):
    new_char_list = []
    for key in character_list:
        dict_entry = {"char": key, "num": character_list[key]}
        new_char_list.append(dict_entry)
    new_char_list.sort()
    print(new_char_list)
