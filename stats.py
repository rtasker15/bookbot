
def count_words(raw_text):
    raw_words = raw_text
    word_list = raw_words.split()
    word_count = len(word_list)
    return word_count

def count_characters(raw_text):
    raw_words = raw_text.lower()
    character_dict = {}
    for key in raw_words:
        if key not in character_dict.keys():
            count = 0
            for character in raw_words:
                if character == key:
                    count +=1
                else:
                    pass
            character_dict.update({key:count})
    return character_dict

def sorted_dict(raw_dict):
    unsorted_dict = raw_dict
    sorting_list = []
    for char, count in unsorted_dict.items():
        sorting_list.append({"char": char, "num": count})
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list

def sort_on(dict):
    return dict["num"]





                
                    

