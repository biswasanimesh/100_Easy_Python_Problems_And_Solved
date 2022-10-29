def sub_string (str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    sub_str = str[:flen]

    result = ""
    for i in range (n):
        result = result + sub_str
    return result
print(sub_string("abcd", 2))