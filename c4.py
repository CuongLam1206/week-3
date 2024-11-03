def is_valid_email(email):
    if '@' in email and '.' in email:
        at_index = email.index('@')
        dot_index = email.index('.')
        
        if at_index < dot_index and dot_index > at_index + 1:
            return True
    return False

email_input = input("Nhập vào địa chỉ email: ")
if is_valid_email(email_input):
    print("Valid")
else:
    print("Invalid")
