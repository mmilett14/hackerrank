def camelcase(s):
    
    word_counter = 1
    
    for i in range(0, len(s)):
        if s[i].isupper():
            word_counter += 1
    
    return word_counter
