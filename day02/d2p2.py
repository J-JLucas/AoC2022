# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3
# X = must lose = 0
# Y = must draw = 3
# Z = must win = 6

score, result = 0, 0
p1,p2 = "", ""

# open data file
f = open('d2Input.txt', 'r')

# iterate through file, line by line
for i in f.readlines():
    p2 = i[0]
    p1 = i[2]
    # determine result
    if p2 == "A":
        if p1 == "X":
            result = 3
        elif p1 == "Y":
            result = 4
        else:
            result = 8
    if p2 == "B":
        if p1 == "X":
            result = 1
        elif p1 == "Y":
            result = 5
        else:
            result = 9
    if p2 == "C":
        if p1 == "X":
            result = 2
        elif p1 == "Y":
            result = 6
        else:
            result = 7
    score = score + result
# close file and print result
f.close()
print("Final score =", score)
