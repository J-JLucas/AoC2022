# This script reads two pairs of ranges from a file
# and determines if the two ranges overlap
# prints count of total overlaps

def read_int(a, i):
    '''
    returns a substring terminated by delimiters '-' or ',' or '\n' 
    inputs: string a, int i
    outputs: string substring, int i at value of current point in array
    '''
    substring = ""
    while a[i] != "-" and a[i] != "," and a[i] != "\n":
        substring = substring + a[i]
        i+= 1
    return substring,i

def main():
    f = open("d4.txt", "r")
    total = 0
    # for each line parse start and end point of both ranges
    for line in f.readlines():
        # intialize values
        i = 0
        x1 = ""
        y1 = ""
        x2 = ""
        y2 = ""
        # parse values
        x1,i = read_int(line, i)
        i+=1
        y1,i = read_int(line, i)
        i+=1
        x2,i = read_int(line, i)
        i+=1
        y2,i = read_int(line, i)
        # convert strings to ints
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        # determine if one range is encapuslated by the other
        if x1 == x2 or y1 == y2:        # if two start/end points equal there's overlap
            total+=1
        elif x1 <= x2 and x2 <= y1:
                total+=1
        elif x2 <= x1 and x1 <= y2:
                total+=1
    print("Total number of encapusalted ranges =", total)
    f.close()
main()
