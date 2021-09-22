def alternate(s):
    
    letter_count = {}
    
    for i in range(0, len(s)):
        
        if s[i] not in letter_count:
            letter_count[s[i]] = 1
        
        else:
            letter_count[s[i]] += 1
            
          
    for letter in letter_count:
        
        if letter_count[letter] == 1:
            s = s.replace(letter, '')

    left = 0
    
    while left < len(s)-1:
        
        right = left+1
        
        if s[left] == s[right]:
            s = s.replace(s[left], '')
            
            left = 0
            
        else:
            left += 1
            
    return len(s)
