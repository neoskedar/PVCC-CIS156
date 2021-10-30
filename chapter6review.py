
def absolute(n):
    return abs(n)

numbers = (4, 5, 6, -2, 4, -12)
x = (map(absolute, (4, 5, 6)))
print(list(x))