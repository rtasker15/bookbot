def count_words(raw_text):
    raw_words = raw_text
    word_list = raw_words.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")

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
            print({key:count})
                
                    

