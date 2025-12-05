def count_words(file_contents):
    num_words = 0
    words = file_contents.split()

    num_words = len(words)

    return num_words

def count_characters(file_contents):
    character_count = {}

    for c in file_contents:
        c_lower = c.lower()
        
        if c_lower in character_count:
            character_count[c_lower] += 1
        else:
            character_count[c_lower] = 1

    return character_count

def sort_on (d):

    return d["num"]

def sort_data(char_count_dict):
    temp = []

    for c in char_count_dict:
        temp.append({
            "char":c,
            "num":char_count_dict[c],
        })

    temp.sort(reverse=True, key=sort_on)

    return temp


