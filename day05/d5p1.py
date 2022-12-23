# Hard coded stacks
# will research better way to parse this in the future
#[N]             [R]             [C]
#[T] [J]         [S] [J]         [N]
#[B] [Z]     [H] [M] [Z]         [D]
#[S] [P]     [G] [L] [H] [Z]     [T]
#[Q] [D]     [F] [D] [V] [L] [S] [M]
#[H] [F] [V] [J] [C] [W] [P] [W] [L]
#[G] [S] [H] [Z] [Z] [T] [F] [V] [H]
#[R] [H] [Z] [M] [T] [M] [T] [Q] [W]
# 1   2   3   4   5   6   7   8   9

def stackMove(dishRack, moves, origin, dest):
    '''
    takes 1 list as input, move count and 2 list indices
    moves k objects from one stack to the other
    inputs: list dishRack, int moves, int origin, int dest
    returns: null
    '''
    for i in range(moves):
        temp = dishRack[origin].pop()
        dishRack[dest].append(temp)
    return

def main():

    s1 = ['R','G','H','Q','S','B','T','N']
    s2 = ['H','S','F','D','P','Z','J']
    s3 = ['Z','H','V']
    s4 = ['M','Z','J','F','G','H']
    s5 = ['T','Z','C','D','L','M','S','R']
    s6 = ['M','T','W','V','H','Z','J']
    s7 = ['T','F','P','L','Z']
    s8 = ['Q','V','W','S']
    s9 = ['W','H','L','M','T','D','N','C']

    dishRack = [s1,s2,s3,s4,s5,s6,s7,s8,s9]

    # open movelist
    f = open("d5.txt", "r")
    
    for line in f.readlines():
        # parse move info
        i = 0
        moveInfo = []       # 3 element list [move, origin, destination]
        #while char is not a number, skip
        while line[i] != "\n":
            if line[i].isnumeric():
                num = ""
                # once number found, contcat until next char is not a number
                while line[i].isnumeric() and line[i] != "\n":
                    num = num + line[i] 
                    i += 1
                moveInfo.append(int(num))
            else:
                i += 1
        # make stack transfer
        # -1 on stack indices as list starts at 0
        stackMove(dishRack, moveInfo[0], moveInfo[1]-1, moveInfo[2]-1)       
        
    # all moves done, output value at the top of each stack
    for stack in dishRack:
        print(stack[-1])
main()
