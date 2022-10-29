str = '802'

try:
    i = float(str)
    print("Numeric")
except (ValueError, TypeError):
    print("Not Numeric")
print()