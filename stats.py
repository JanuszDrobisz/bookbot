def word_list_count(text):
    word_list = text.split()
    return len(word_list)

def count_chars(text):
    char_count_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(num_dict):
    sorted_list = []
    for char in num_dict:
        sorted_list.append({"char": char, "num": num_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list