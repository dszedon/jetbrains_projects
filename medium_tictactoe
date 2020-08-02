"""
TIC TAC TOE

About
Everybody remembers this paper-and-pencil game from childhood: 
Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. 
A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. 
Let’s program Tic-Tac-Toe and get playing!

Learning outcomes
After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch, 
using classes and functions, handling errors, and processing user input. 
You will also learn to use OOP (Object-Oriented Programming) in the process.

Stage 1
Learn how to work with the field and the coordinates.

Stage 2
Make an easy difficulty level where the computer just makes random moves: 
simple to make and not too challenging to beat.

Stage 3
Whether you want to play with a friend or take a break and watch computers battle it out, you can do both!

Stage 4
Let’s create a medium difficulty level. This AI should be a lot harder to beat! Are you up to the challenge?

Stage 5
Oh no, what have we created here? An unbeatable AI monster! Indeed, this complex algorithm guarantees a win or a draw.

"""

a = '         '
b = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]
print(f'''---------
| {b[0][0]} {b[0][1]} {b[0][2]} |
| {b[1][0]} {b[1][1]} {b[1][2]} |
| {b[2][0]} {b[2][1]} {b[2][2]} |
---------''')
xwins = 1
owins = 1
i = 0
moves = 0
while True:
    d = input('Enter the coordinates:').split()
    if d[0].isnumeric() and d[1].isnumeric():
        k = d[:]
        k[0] = 3 - int(d[1])
        k[1] = int(d[0]) - 1
        if 1 <= int(d[0]) <= 3 and 1 <= int(d[1]) <= 3:
            if b[k[0]][k[1]] == ' ' and i % 2 == 0:
                b[k[0]][k[1]] = 'X'
                print(f'''---------
| {b[0][0]} {b[0][1]} {b[0][2]} |
| {b[1][0]} {b[1][1]} {b[1][2]} |
| {b[2][0]} {b[2][1]} {b[2][2]} |
---------''')
                i += 1
                if b[0][2] == b[1][1] == b[2][0] == 'X' or b[1][1] == b[0][0] == b[2][2] == 'X':
                    print('X wins')
                    break
                else:
                    for j in range(3):
                        if b[j][0] == b[j][1] == b[j][2] == 'X' or b[0][j] == b[1][j] == b[2][j] == 'X':
                            print('X wins')
                            break

            elif b[k[0]][k[1]] == ' ' and i % 2 == 1:
                b[k[0]][k[1]] = 'O'
                print(f'''---------
| {b[0][0]} {b[0][1]} {b[0][2]} |
| {b[1][0]} {b[1][1]} {b[1][2]} |
| {b[2][0]} {b[2][1]} {b[2][2]} |
---------''')
                i += 1
                if b[1][1] == b[0][0] == b[2][2] == 'O' or b[0][2] == b[1][1] == b[2][0] == 'O':
                    print('O wins')
                    break
                else:
                    for j in range(3):
                        if b[j][0] == b[j][1] == b[j][2] == 'O' or b[0][j] == b[1][j] == b[2][j] == 'O':
                            print('O wins')
                            break
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')
    moves = sum([b[h].count('X') + b[h].count('O') for h in range(3)])
    if moves == 9:
        print(('Draw'))
        break
