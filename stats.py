def number_of_words(text):
    split_text = text.split()
    return len(split_text)

def count_each_character(text):
    lower_text = text.lower()
    count_dict = {}
    for t in lower_text:
        if t in count_dict:
            count_dict[t] += 1
        else:
            count_dict[t] = 1
    return count_dict

def sort_on(items):
    return items["num"]

def create_sorted_list(text_dictionary):
    sorted_list = []
    for character in text_dictionary:
        new_dict = {}
        new_dict["char"] = character
        new_dict["num"] = text_dictionary[character]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list