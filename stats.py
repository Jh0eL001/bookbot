def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(book):
    num_words = len(book.split())
    return num_words


def get_char(book_text):
    book_text = book_text.lower()
    char_dict = {}
    
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict


def sort_characters(char_count_dict):
    # Create a list of dictionaries with 'char' and 'num' keys
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    # Sort by count in descending order using a helper function
    def sort_on(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
