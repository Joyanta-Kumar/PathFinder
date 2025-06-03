a = ["f", "g", "h"]

print(a.__contains__("f"))

b = a.copy()

removeItem = "g"
left = b[0:b.index(removeItem)]
right = b[b.index(removeItem)+1:]
b = left + right

print(a)
print(b)