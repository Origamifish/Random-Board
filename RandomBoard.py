import random



def printBoard(board):
  for i in range(10):
    print()
    for j in range(10):
      print(randomBoard[i][j], end = '')

def sum(board):
  counter = 0
  for i in range(10):
    print()
    for j in range(10):
      counter = counter + board[i][j]
  print("The sum is " + str(counter))


randomBoard = [[]]
for i in range(10):
  randomBoard.append([])
  for j in range(10):
    randomBoard[i].append(random.randint(0,9))
printBoard(randomBoard)
sum(randomBoard)
