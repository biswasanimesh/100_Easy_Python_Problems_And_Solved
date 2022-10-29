def is_group_number (group_data, n):
    for value in group_data:
        if n == value:
            return True

    return False

print(is_group_number([1,2,3,4,5,6,7,45,99], 99))             ## Last digit is the matching or non matching digit here.