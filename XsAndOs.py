import random
#-----------main set up----------#
def checkIfWon(player, board):
    if(board[0]== player and board[0]==board[1] and board[0]==board[2]):
        return player
    if(board[3]== player and board[3]==board[4] and board[3]==board[5]):
        return player
    if(board[6]== player and board[6]==board[7] and board[6]==board[8]):
        return player
    if(board[0]== player and board[0]==board[3] and board[3]==board[6]):
        return player
    if(board[1]== player and board[1]==board[4] and board[4]==board[7]):
        return player
    if(board[2]== player and board[2]==board[5] and board[5]==board[8]):
        return player
    if(board[0]== player and board[0]==board[4] and board[0]==board[8]):
        return player
    if(board[2]== player and board[2]==board[4] and board[2]==board[6]):
        return player
    else:
        return 'No one'
    
def displayOptions(board):
    possibleMoves = []
    for i in range(len(board)):
        if(board[i] == ' '):
            possibleMoves.append(i+1)
    return possibleMoves

def move(board,player, position):
    board[postion-1]=player
    return board

def printBoard(board):
   
    print()
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
    print("------------")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("------------")
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+" ")
    print()

def checkIfValid(board, pos):
    if(not(board[pos]==" ")):
#        print("error occured")
        playO(board,1)
    return True

#---------End main set up--------#
    
#---------------AI---------------#

#          blocking methods         #   
def TwoInRow(board,start, player):
    row = []
    if(start<7):
        for i in range(start,start+3):
            row.append(board[i])
        if (row.count(player)==2 and row.count(" ")==1):
            return row.index(" ")+(start)
        else:
            return TwoInRow(board,start+3)
    return -1

def TwoInCol(board, start, player):
    col = []
    if(start<7):
        for i in range(start,7+start,3):
            col.append(board[i])
        if (col.count(player)==2 and col.count(" ")==1):
            print((col.index(" ")*3)+start)
            return (col.index(" ")*3)+start
        else:
            return TwoInRow(board,start+1)
    return -1

def TwoInDiag(board,start, player):
    if(start==2):
        return -1
    if(start==0):
        diag = []
        diag.append(board[0])
        diag.append(board[4])
        diag.append(board[8])
        if(diag.count(player)==2 and diag.count(" ")==1):
            return diag.index(" ")*4
        else:
            return TwoInDiag(board,start+1)
    else:
        diag = []
        diag.append(board[2])
        diag.append(board[4])
        diag.append(board[6])
        if(diag.count(player)==2 and diag.count(" ")==1):
            return (diag.index(" ")+1)*2
        else:
            return -1
    
def stopRow(board,player):
    res=TwoInRow(board,0, player)
    if(not(res==-1)):
       checkIfValid(board,res)
       board[res]="O"
       return True
    return False

def stopCol(board,player):
    res=TwoInCol(board,0, player)
    if(not(res==-1)):
       checkIfValid(board,res)
       board[res]="O"
       return True
    return False

def stopDiag(board, player):
    res=TwoInDiag(board,0, player)
    if(not(res==-1)):
       checkIfValid(board,res)
       board[res]="O"
       return True
    return False

def stopOtherPlayer(board):
    if(stopRow(board,"X")):
        return True
    elif(stopCol(board,"X")):
        return True
    elif(stopDiag(board,"X")):
        return True
    return False
#      End of blocking methods      #

def iCanWin(board):
    if(stopRow(board,"O")):
        return True
    elif(stopCol(board,"O")):
        return True
    elif(stopDiag(board,"O")):
        return True
    return False

def findRow(pos):
    if(pos>=0 and pos<=2):
        return 0
    if(pos>=3 and pos<=5):
        return 1
    if(pos>=6 and pos<=8):
        return 2
    return 0

def findCol(pos):
    return pos%3

def findDiag(pos):
    if(pos%4==0):
        return 0
    if(pos%2==0):
        return 2
    return -1
        
def AddToRow(pos,board, player):
    rowLst = []
    rowNum =findRow(pos)
    for i in range(0+rowNum*3,3+(rowNum*3)):
        rowLst.append(board[i])
    if(rowLst.count("X")==0 and rowLst.count(" ")>0 and rowLst.count("O")>0):
        checkIfValid(board,rowLst.index(" ")+(3*rowNum))
        board[rowLst.index(" ")+(3*rowNum)] = "O"
        return True 
    else:
        return False

def AddToCol(pos,board,player):
    colLst = []
    colNum =findCol(pos)
    for i in range(0+colNum,7+colNum,3):
        colLst.append(board[i])
    if(colLst.count("X")==0 and colLst.count(" ")>0 and colLst.count("O")>0):
        checkIfValid(board,colLst.index(" ")*3+colNum)
        board[colLst.index(" ")*3+colNum] = "O"

        return True 
    else:
        return False

def AddDiag(pos,board,player):
    DiagLst = []
    if(findDiag(pos)==-1):
        return False
    DiagNum = findDiag(pos)
    if(DiagNum==0):
        for i in range(0,9,4):
            DiagLst.append(board[i])
    else:
        for i in range(2,7,2):
            DiagLst.append(board[i])
    if(DiagLst.count("X")==0 and DiagLst.count(" ")>0 and DiagLst.count("O")>0):
        if(DiagNum==0):
            checkIfValid(board,DiagLst.index(" ")*3+DiagNum)
            board[DiagLst.index(" ")*4] = "O"
        else:
            checkIfValid(board,DiagLst.index(" ")*3+DiagNum)
            board[DiagLst.index(" ")*2+2] = "O"
        return True 
    else:
        return False

def createSensor(board):#this is the centre function in the AI
    #  0 | 1 | 2
    # ------------
    #  3 | 4 | 5
    # ------------
    #  6 | 7 | 8  
    posOs = findOs(board)#this lists all the possible positions not taken up by an "X"
    moveOptions = displayOptions(board)
    for i in range( len(posOs)):
#checks if O can win in that turn.
        if(iCanWin(board)):
            return True
        if(stopOtherPlayer(board)):#this fucntion is specifically used to stop a human user from winning
            return True
#if their are no immidiate threats, the program jumps to this funciton, if there is an "O" already in a row. it will add to that row.
        if(AddToRow(posOs[i],board,"O")):
            return True
#if their are no rows available, the program jumps to this funciton, if there is an "O" already in a column. it will add to that column.
        if(AddToCol(posOs[i],board,"O")):
            return True
#if their are no columns available, the program jumps to this funciton, if there is an "O" already in a diagonal. it will add to that diagonal.
        if(AddDiag(posOs[i],board, "O")):
            return True 
    return False
        
def findOs(board):
    pos = []
    for i in range(len(board)):
        if(board[i]=="O"):
            pos.append(i)
    return pos

#this is the AI that controls the oposition   
def AI(board):
    if(len(displayOptions(board))>0):#if there are options to choose from on the board
        if(createSensor(board)):
            return True
    return False
        
#-------------End AI-------------#            

#------------- MAIN- ------------#
def playO(board,rNum):
    if(rNum == 1):
        play = random.randint(1,9)
        if(board[int(play)-1] ==" "):
            board[int(play)-1] = "O"
        else:
            playO(board,1)
    else:
        if(not(AI(board))):
            playO(board,1)
    pass

def playX(board):
    play = input("Which option would you like?:")
    if(int(play)<1 or int(play)>9):
        print("invalid move")
        playX(board)
    if(board[int(play)-1] ==" "):
        board[int(play)-1] = "X"
    else:
        print("invalid move")
        playX(board)
    pass

def main():
    roundNum = 0
    board= [" "," "," ",
            " "," "," ",
            " "," "," "]
    players = ["X","O"]
    player=players[random.randrange(0,2)]
    print(player+ " Starts")
    print("you are X")
    while(len(displayOptions(board))>0):
        posMoves = displayOptions(board)
        if (player == "X"):
            printBoard(board)  
            playX(board)
            if(not(checkIfWon("X",board)=="No one")):
                break
            player="O"    
        else:
            roundNum+=1
            playO(board,roundNum)
            if(checkIfWon("O",board)=="O"):
                break
            player="X"   
    printBoard(board)   
    input(checkIfWon(player,board)+" Won the Game")
    pa = input("would you like to play again?")
    if(pa == "yes"):
        main()
    return True
if __name__ == "__main__":
    main()

