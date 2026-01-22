from stats import get_num_words, get_book_text, get_char, sort_characters
import sys

def main():
    if(len(sys.argv) > 1):
        book_text = get_book_text(sys.argv[1])
        num_words = get_num_words(book_text)
        char_counts = get_char(book_text)

        #Prints
        # Sort the characters
        sorted_chars = sort_characters(char_counts)

        # Print the report
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        # Print each character and its count
        for char_dict in sorted_chars:
            print(f"{char_dict['char']}: {char_dict['num']}")

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   
main()
