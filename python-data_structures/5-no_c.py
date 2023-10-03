def no_c(my_string):
    new_string = ""
    if my_string is None:
        return
    for char in my_string:
        if char != "c" and char != "C":
            new_string += char
    return new_string
