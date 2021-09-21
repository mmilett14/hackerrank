def superReducedString(s):
    i = 0
    
    while i+1 < len(s):
        left = i
        right = i+1
        
        if s[left] == s[right]:
            s = s[0:left] + s[right+1:len(s)]
                
            i = 0
        
        elif s[left] != s[right]:
            i += 1
            
    
    if len(s) > 0:
        return s
    
    else:
        return 'Empty String'
