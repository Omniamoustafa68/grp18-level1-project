print('---python function to check if a string ia a palindrome---')

def palindrome(words):
    after_reverse = words[::-1]
    if after_reverse == words:
        return True
    else:
        return False


v_result = palindrome('radar')
if v_result:
    print('radar is a palindrome')
else:
    print('is not palindrome')
    
