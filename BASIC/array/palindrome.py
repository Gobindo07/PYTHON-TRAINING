def palindrome(s):
    return s == s[::-1]
s = "hello"
print(palindrome(s))