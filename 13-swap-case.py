def swap_case(str):
    
    new_str = ''
    
    for s in range(0, len(str)):
        if str[s].isalpha():
            
            if str[s].isupper():
                new_str += str[s].lower()

            elif str[s].islower():
                new_str += str[s].upper()

        else:
            new_str += str[s]
            
    return new_str