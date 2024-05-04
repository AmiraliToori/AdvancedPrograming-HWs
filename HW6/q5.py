

text = input("Please enter a text: ")

text_lst = text.split()

length_list = []
for word in text_lst:
    if len(word) not in length_list:
        length_list.append(len(word))

length_list = sorted(length_list)


def create_dictionary(size, text_lst):
    lst = []
    for word in text_lst:
        if size == len(word) and word not in lst:
                lst.append(word)
    return lst
                
values_lst = []
for size in length_list:
    values_lst.append(create_dictionary(size, text_lst))

print(dict(zip(length_list, values_lst)))