def count_words(content):
    words = content.split()
    num_words = len(words)
    return num_words


def count_chars(content):
    char_count = {}
    
    for char in content.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count


def sort_on(dict):
    return dict["num"]


def sort_char_dict(char_dict):
    dict_list = []
    for k,v in char_dict.items():
        dict_list.append({"char" : k, "num" : v})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
