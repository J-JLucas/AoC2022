# A = X = Rock = 1
# B = Y = Paper = 2
# C = Z = Scissors = 3
# loss = 0, draw = 3, win = 6

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
            result = 4
        elif p1 == "Y":
            result = 8
        else:
            result = 3
    if p2 == "B":
        if p1 == "X":
            result = 1
        elif p1 == "Y":
            result = 5
        else:
            result = 9
    if p2 == "C":
        if p1 == "X":
            result = 7
        elif p1 == "Y":
            result = 2
        else:
            result = 6
    score = score + result
# close file and print result
f.close()
print("Final score =", score)
