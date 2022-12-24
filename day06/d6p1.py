# indentifies a marker (string of 4 unique chars)
# in a buffer and returns index of the last element (+1)
# of the marker string

f = open("d6.txt", "r")

#read file and fill buffer "pipeline"
line = f.readline()
found = False
pos1 = line[0]
pos2 = line[1]
pos3 = line[2]
pos4 = line[3]
i = 3 
print(pos1, pos2, pos3, pos4)

# initial case, determine if all unique
if pos1 != pos2 and pos1 != pos3 and pos1 != pos4:
    if pos2 != pos3 and pos2 != pos4:
        if pos3 != pos4:
            print("marker ends at 4th char")
            found = True

# increment 1 by 1
if not found:
    while line[i] != "" and not found:
        i += 1
        pos1 = pos2
        pos2 = pos3
        pos3 = pos4
        pos4 = line[i]
        print(pos1, pos2, pos3, pos4)

        if pos1 != pos2 and pos1 != pos3 and pos1 != pos4:
            if pos2 != pos3 and pos2 != pos4:
                if pos3 != pos4:
                    print("marker ends at", i+1, "char")
                    found = True
                    break
f.close()


