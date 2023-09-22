def display(theboard):
    print([theboard[1] + '|' + theboard[2] + '|' + theboard[3]])
    print( [theboard[4] + '|' + theboard[5] + '|' + theboard[6]])
    print([theboard[7] + '|' + theboard[8] + '|' + theboard[9]])

#input your marker choice
def user_input():
    mark_choice=''
    while mark_choice not in ['X','O']:
        mark_choice=input("please input your marker choice in 'X' OR 'O'").upper()
        if mark_choice not in ['X','O']:
            print("please input the right  type")
        if mark_choice=='X':
            return ('X','O')
        else:
            return ('O','X')

def repalce_position(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board,position):
    return board[position]==' '

def full_check(board):
    time=0
    for i in range(1,10):
        time+=space_check(board,i)
        if time==9:
            print("the game is draw")

def goon_choice():
    goon_marker=int(input("please input your go on chioce from 1(yes) or 0(no)"))
    if goon_marker == 1:
        return True
    else:
        return False
import random
def first_chioce():
    #从0和1里面随机选一个
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def position_choice(board):
    position=0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


print("welcome to tic toe game")
while True:
    theboard=[' ']*10
    gameon_chioce=goon_choice()
    if gameon_chioce:
        player1_marker,player2_marker=user_input()
        turn = first_chioce()
        print(turn + "will first choose")
    while gameon_chioce:
        if turn=='Player 1':
            print(turn+"make your choice")
            position=position_choice(theboard)
            repalce_position(theboard,player1_marker,position)
            display(theboard)
            win_mark=win_check(theboard,player1_marker)
            if win_mark:
              print("game over"+turn+"kill the game")
              break
            else:
                if full_check(theboard):
                    print("game over because of full board")
                    gameon_chioce=0
                else:
                    turn="Player 2"
        else:
            print(turn + "make your choice")
            position=position_choice(theboard)
            repalce_position(theboard,player2_marker,position)
            display(theboard)
            win_mark=win_check(theboard,player2_marker)
            if win_mark:
              print("game over"+turn+"kill the game")
              break
            else:
                if full_check(theboard):
                    print("game over because of full board")
                    gameon_chioce=0
                else:
                    turn="Player 1"
    if not gameon_chioce:
        break