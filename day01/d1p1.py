maxVal = 0
elfSum = 0

# open data file
f = open('day1p1.txt', 'r')

#while not eof
while True:
    # iterate through file
    i = f.readline()
    if i == "":
        break                   # EOF
    if i == "\n":
        if elfSum > maxVal:
            maxVal = elfSum
        elfSum = 0              # reinitialize at 0 for next elf
        continue
    elfSum = elfSum + int(i)
        
# close file and print result
f.close()
print("The largest sum calorie count is", maxVal)

