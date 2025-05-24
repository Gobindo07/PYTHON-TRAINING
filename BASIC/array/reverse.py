def rever(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev
s = "hello"
print(rever(s))