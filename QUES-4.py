def is_palindrome(s: str) -> bool:
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    return normalized_str == normalized_str[::-1]

s1 = "A man, a plan, a canal: Panama"
print("Input:", s1)
print("Output:", is_palindrome(s1))  

s2 = "race a car"
print("Input:", s2)
print("Output:", is_palindrome(s2))