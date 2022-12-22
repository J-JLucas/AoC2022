
total = 0
# open data file 
f = open('d3.txt', 'r')

# iterate through file, 3 lines at a time
while True:
    #read 3 lines, abort if one == EOF
    x = f.readline()
    if x == "":
        break
    y = f.readline()
    if y == "":
        break
    z = f.readline()
    if z == "":
        break

    # determine shortest string
    if len(x) < len(y):
        if len(x) < len(z):
            # x is shortest string
            shortest = x
            a = y
            b = z
        else:
            # z is shortest string
            shortest = z
            a = x
            b = y
    elif len(y) < len(z):
        # y is shortest string
        shortest = y
        a = x
        b = z
    else:
        # z is shortest string
        shortest = z
        a = x
        b = y
    # initialize counters
    k = 0
    item = ""
    for i in range(len(shortest)):                  
        if shortest[k] in a and shortest[k] in b:
            item = shortest[k]
            # chars have different enum values if lower or upper
            if item.isupper():
                item = ord(item)-38
            else:
                item = ord(item)-96
            total = total + item
            break 
        else:
            k+=1 # increment counter and check next item
print("The sum total priority value is" ,total)
f.close()


