# write your code here
state = list("_________")
coordinates = {
    (1, 1) : state[0],(1, 2) : state[1],(1, 3) : state[2],
    (2, 1) : state[3],(2, 2) : state[4],(2, 3) : state[5],
    (3, 1) : state[6],(3, 2) : state[7],(3, 3) : state[8]
    }
print(f"---------\n| {coordinates[1, 1]} {coordinates[1, 2]} {coordinates[1, 3]} |\n| {coordinates[2, 1]} {coordinates[2, 2]} {coordinates[2, 3]} |\n| {coordinates[3, 1]} {coordinates[3, 2]} {coordinates[3, 3]} |\n---------")
winner = []
coordinates = {
    (1, 1) : state[0],(1, 2) : state[1],(1, 3) : state[2],
    (2, 1) : state[3],(2, 2) : state[4],(2, 3) : state[5],
    (3, 1) : state[6],(3, 2) : state[7],(3, 3) : state[8]
    }
p1 = True
p2 = True
game = True
X = []
O = []
while game :
    while p1:
        try:
            x, y = input().split()
            x = int(x)
            y = int(y)
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
            elif coordinates[x, y] == "X" or coordinates[x, y] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                coordinates[x, y] = "X"
                X.append("X")
                p1 = False
        except ValueError:
            print("You should enter numbers!")
    print(f"---------\n| {coordinates[1, 1]} {coordinates[1, 2]} {coordinates[1, 3]} |\n| {coordinates[2, 1]} {coordinates[2, 2]} {coordinates[2, 3]} |\n| {coordinates[3, 1]} {coordinates[3, 2]} {coordinates[3, 3]} |\n---------")
    p2 = True
    winning = [[coordinates[1, 1],coordinates[1, 2],coordinates[1, 3]],
               [coordinates[2, 1],coordinates[2, 2],coordinates[2, 3]],
               [coordinates[3, 1],coordinates[3, 2],coordinates[3, 3]],
               [coordinates[1, 1],coordinates[2, 1],coordinates[3, 1]],
               [coordinates[1, 1],coordinates[2, 2],coordinates[3, 3]],
               [coordinates[3, 1],coordinates[2, 2],coordinates[1, 3]]]
    empty = abs((len(O) + len (X)) - 9)
    if abs(len(X) - len(O)) == 1 or abs(len(X) - len(O)) == 0:
            for i in range(len(winning)):
                if len(set(winning[i])) == 1 and winning[i][0] != "_":
                    winner.append(winning[i])
    if  len(winner) == 1 and (winner[0][0] == "X" or winner[0][0] == "O"):
        if winner[0][0] == "X":
            print("X wins")
            exit()
        else:
            print("O wins")
            exit()
    elif len(winner) == 0 and empty == 0:
        print("Draw")
        exit()
    while p2:
        try:
            x, y = input().split()
            x = int(x)
            y = int(y)
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
            elif coordinates[x, y] == "X" or coordinates[x, y] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                coordinates[x, y] = "O"
                O.append("O")
                p2 = False
        except ValueError:
            print("You should enter numbers!")
    print(f"---------\n| {coordinates[1, 1]} {coordinates[1, 2]} {coordinates[1, 3]} |\n| {coordinates[2, 1]} {coordinates[2, 2]} {coordinates[2, 3]} |\n| {coordinates[3, 1]} {coordinates[3, 2]} {coordinates[3, 3]} |\n---------")
    p1 = True
    winning = [[coordinates[1, 1],coordinates[1, 2],coordinates[1, 3]],
               [coordinates[2, 1],coordinates[2, 2],coordinates[2, 3]],
               [coordinates[3, 1],coordinates[3, 2],coordinates[3, 3]],
               [coordinates[1, 1],coordinates[2, 1],coordinates[3, 1]],
               [coordinates[1, 1],coordinates[2, 2],coordinates[3, 3]],
               [coordinates[3, 1],coordinates[2, 2],coordinates[1, 3]]]
    empty = abs((len(O) + len (X)) - 9)
    if abs(len(X) - len(O)) == 1 or abs(len(X) - len(O)) == 0:
            for i in range(len(winning)):
                if len(set(winning[i])) == 1 and winning[i][0] != "_" :
                    winner.append(winning[i])
    if  len(winner) == 1 and (winner[0][0] == "X" or winner[0][0] == "O"):
        if winner[0][0] == "X":
            print("X wins")
            exit()
        else:
            print("O wins")
            exit()
    elif len(winner) == 0 and empty == 0:
        print("Draw")
        exit()
