def w_count(input_string):
    if type(input_string) != str:
        return "Input is not string"
    else:
        arr = input_string.split()
        return len(arr)