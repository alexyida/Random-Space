array = ["a", "d", "d", "d", "a", "d", "a"]

candidate = array[0]
count = 0

for e in array:
    if e == candidate:
        count += 1
    elif count == 0:
        candidate = e
        count = 1
    else:
        count -= 1
        
print candidate
        