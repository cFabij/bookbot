from stats import count_words, count_chars, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        
    return contents


def print_format(filepath, word_count, content_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in content_dict:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_text(filepath)
    num_words = count_words(book_content)
    num_chars_dict = count_chars(book_content)
    sorted_dict = sort_char_dict(num_chars_dict)
#    print(f"{num_words} words found in the document")
#    print(num_chars_dict)
#    print(sorted_dict)
    print_format(filepath, num_words, sorted_dict)


main()
