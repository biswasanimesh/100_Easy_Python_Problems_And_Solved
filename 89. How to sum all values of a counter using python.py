import collections

num = [2, 5, 6, 9, 52, 3, 6, 54, 2, 3]

print(sum(collections.Counter(num).values()))