def letter_count_dict(s):
    
    letter_count = {}
    
    for i in range(0, len(s)):
        
        if s[i] not in letter_count:
            letter_count[s[i]] = 1
        
        else:
            letter_count[s[i]] += 1
    
    return letter_count


def letter_count_replace(s, letter_count):
           
    for letter in letter_count:
        
        if letter_count[letter] == 1:
            s = s.replace(letter, '')
            
    return s
            

def same_letter_replace(s):
    
    left = 0
    
    while left < len(s)-1:
        
        right = left+1
        
        if s[left] == s[right]:
            s = s.replace(s[left], '')
            
            left = 0
            
        else:
            left += 1
            
    return s


def letter_count_list(letter_count):
    
    letter_list = []

    for letter in letter_count:
        letter_list.append(letter)

    return letter_list
    

def alternate(s):
    
    letter_count = letter_count_dict(s)
    
    s = letter_count_replace(s, letter_count)

    s = same_letter_replace(s)
    
    letter_count = letter_count_dict(s)
    
    letter_list = letter_count_list(letter_count)
    
    if len(letter_list) == 2:
        return len(s)
    
    else:
        for i in range(0, len(letter_list)-2):
            s = s.replace(letter_list[i], '')
        
        return len(s)
