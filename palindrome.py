def palin(input_string):
    if type(input_string) != str:
        return "Input is not string"
    
    else:
        return input_string == input_string[::-1]