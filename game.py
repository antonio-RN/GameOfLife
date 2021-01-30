from random import choices

#game variables -   aliveProb is the probability (out of 1) of a cell to be alive at seed generation; 
#                   dimension is the size of the square game board (both rows and columns)
aliveProb = 0.45
dimension = 3

#matrix declaration -   m0 is the actual time game board; m1 is the next generation (t+1) game board. Both start full of 0.
m0 = [[0 for i in range(dimension)] for j in range(dimension)]
m1 = [[0 for i in range(dimension)] for j in range(dimension)]

#random seed creation - seed is a list of all the cells, 0 or 1, from i0j0, i0j1 ... to injn (n = dimensions-1)
seed = choices([0,1],[1-aliveProb,aliveProb], k=dimension**2)

#m0 matrix filling
for i in range(dimension):
    for j in range(dimension):
        m0[i][j] = seed[dimension*i+j]
        m1[i][j] = seed[dimension*i+j]

while True:
    #m0 formatted printing
    for i in range(dimension):
        print(m0[i])

    #game logic
    for i1 in range(dimension):
        for j1 in range(dimension):

            #calculating surrounding alive cells in nearAlive counter
            nearAlive = 0
            for i0 in range(max(0,i1-1),min(i1+2,dimension)):
                for j0 in range(max(0,j1-1),min(j1+2,dimension)):
                    if i0==i1 and j0==j1:
                        pass
                    else:
                        nearAlive=nearAlive+m0[i0][j0]
            #reproduction, represented with a 2
            if not(m0[i1][j1]) and nearAlive==3:
                m1[i1][j1] = 2
            #underpopulation and overpopulation, represented with a -1
            if (m0[i1][j1]) and not (1<nearAlive<4):
                m1[i1][j1] = -1

    print()
    input()

    #m1 formatted printing
    for i in range(dimension):
        print(m1[i])

    #change of generation
    for i in range(dimension):
        for j in range(dimension):
            if m1[i][j]>1:
                m0[i][j]=1
                m1[i][j]=1
            elif m1[i][j]<0:
                m0[i][j]=0
                m1[i][j]=0     

    print()
    input()
