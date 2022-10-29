def concatenate_list (list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list(['me', 5, 'globals']))