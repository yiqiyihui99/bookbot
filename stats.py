def get_num_words(text):
    num_words = len(text.split())
    
    return f"Found {num_words} total words"


def get_num_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        chars[char] = chars.get(char, 0) + 1
        
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(chars):
    c_list = []
    for i in chars:
        c_list.append({"char": i, "num": chars[i]})
    c_list.sort(reverse=True, key=sort_on)
    return c_list
