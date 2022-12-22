
total = 0
# open data file 
f = open('d3.txt', 'r')

# iterate through file, line by line
for sack in f.readlines():
    # initialize counters
    k = 0
    item = ""
    split = len(sack)//2
    for i in range(split):                       # for first half of string
        if sack[k] in sack[(len(sack)//2):]:    # must be floor div, regular returns float
            item = sack[k]
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


