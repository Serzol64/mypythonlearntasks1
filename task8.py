def is_palindrome(text):
    valid = text == ''.join(reversed(text))

    if valid: print("Эта строка является палиндромом")
    else: print("Эта строка не устроена из палиндрома;-(")

print(is_palindrome('abba'))