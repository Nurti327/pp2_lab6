def is_palindrome(s: str) -> bool:
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Hello"))