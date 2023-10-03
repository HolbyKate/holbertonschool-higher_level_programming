#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    list_new = my_list.copy()
    if idx < 0 or idx > length - 1:
        return(list_new)
    list_new[idx] = element
    return (list_new)
