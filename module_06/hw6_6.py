def encode_password(password):
    
    result = []
    for i in password:
        result.append(hex(ord(i.encode())))
        
    return result