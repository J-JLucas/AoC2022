# indentifies a marker (string of 14 unique chars)
# in a buffer and returns index of the last element (+1)
# of the marker string

f = open("d6.txt", "r")

#read file and fill buffer "pipeline"
line = f.readline()
found = False
i = 0

while line[i] != "" and not found:
    # build substring of next 14 characters
    substring = ""  
    for k in range(i, i+14):
        substring = substring + line[k]
    testSet = set(substring)

    # if sets are unique, if length equal, chars all unique
    if len(substring) == len(testSet):
        found = True
        print("marker ends at", i+14, "char")
    i+= 1  # next iteration
f.close()


