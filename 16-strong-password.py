def minimumNumber(n, password):
    
    pass_counts = {'lower_count': 0,
    'upper_count': 0,
    'number_count': 0,
    'char_count': 0}
    
    rem_requirement = 0
   
    for i in range(0, len(password)):
        if password[i].islower():
            pass_counts['lower_count'] += 1
        
        elif password[i].isupper():
            pass_counts['upper_count'] += 1
            
        elif password[i].isnumeric():
            pass_counts['number_count'] += 1
        
        else:
            pass_counts['char_count'] += 1
        
    

    for count in pass_counts:
        if pass_counts[count] == 0:
            rem_requirement += 1
    
    length_diff = (6 - rem_requirement) - len(password)
            
    if length_diff > 0:
        rem_requirement += length_diff
            
    return rem_requirement
