


user_input = input("Please enter a string: ")

def create_sorted_dictionary(text):
    text_lst = text.split()
    keys = []
    for word in text_lst:
        if word.isalpha() and word not in keys:
            keys.append(word)
            
    keys = sorted(keys)
    
    dictionary = {}
    for key in keys:
        num_lst = []
        for i in range(len(text_lst)):
            if text_lst[i].isnumeric() and text_lst[i] not in num_lst and key == text_lst[i - 1]:
                num_lst.append(int(text_lst[i]))
        
        min_element = min(num_lst)
        max_element = max(num_lst)
        pair_tuple = (min_element, max_element)
        new_dictionary = {key : pair_tuple}
        dictionary.update(new_dictionary)
    
    return dictionary
    

print(create_sorted_dictionary(user_input))
