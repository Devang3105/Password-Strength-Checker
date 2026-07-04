def check_password(password):
    score = 0
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    suggestions = []
    
    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"
    
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should contain at least 8 characters.")
        
    for ch in password:
        
        if ch.isupper():
            has_upper=True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_characters:
            has_special = True
            
    if has_upper:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")
    
    if has_lower:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")
        
    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one number/digit.")
        
    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character.")
        
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
        
    return {
        "Score" : score,
        "Strength" : strength,
        "Suggestions" : suggestions
    }
    