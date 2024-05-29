

text_input = input("Please enter a string: ")

dictionary = {'look': ['gaze', 'see', 'glance', 'watch', 'peruse'], 
              'put': ['place', 'set', 'attach', 'keep', 'save', 'set aside', 'effect', 'achieve', 'do', 'build'], 
              'beautiful': ['pretty', 'lovely', 'handsome', 'dazzling', 'splendid', 'magnificent'],
              'slow': ['unhurried', 'gradual', 'leisurely', 'late', 'behind', 'tedious', 'slack'],
              'dangerous': ['perilous', 'hazardous', 'uncertain']}


def delete_e(dictionary, text):
    key_lst = sorted(dictionary.keys())
    for key in key_lst:
        value_lst = dictionary.get(key)
        
        new_lst = []
        for value in value_lst:
            if text not in value:
                new_lst.append(value)
        
        new_lst = sorted(new_lst)
        new_value_key = {key : new_lst}
        dictionary.update(new_value_key)
        
    return dictionary
    

print(delete_e(dictionary, text_input))