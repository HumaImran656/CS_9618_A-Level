def validate_password(password):
    lcase_char = 0
    ucase_char = 0
    num_char = 0
    n = 1
    return_flag = True
    while n <= len(password) and return_flag:
        next_char = password[n - 1]
        if next_char >='a' and next_char <= 'z':
            lcase_char += 1
        elif next_char>='A' and next_char <= 'Z':
            ucase_char += 1
        elif next_char >= '0' and next_char <= '9':
            num_char += 1
        else:
            return_flag = False
        n += 1
    return return_flag and lcase_char >= 1 and ucase_char >= 1 and num_char >= 1

passw = str(input("Enter your password"))
answer = validate_password(passw)
print (answer)

