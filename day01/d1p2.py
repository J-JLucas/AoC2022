maxVal, first, second, third = 0,0,0,0
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
        if elfSum > first:
            third = second
            second = first
            first = elfSum
        elif elfSum > second:
            third = second
            second = elfSum
        elif elfSum > third:
            third = elfSum
        elfSum = 0              # reinitialize at 0 for next elf
        continue
    elfSum = elfSum + int(i)
        
# close file and print result
f.close()
maxVal = first + second + third
print("The sum calorie count is", maxVal)

