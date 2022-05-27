from random import randint
from itertools import combinations
from traceback import print_tb


def new_board():
    global board
    board = {
        8: " ", 3: " ", 4: " ",
        1: " ", 5: " ", 9: " ",
        6: " ", 7: " ", 2: " "
    }

    global positions
    positions = {
        "X": [],
        "O": []
    }


def print_board():
    print(f"""\n    8  {board[8]}  |3  {board[3]}  |4  {board[4]}  
   ------|------|------
   1  {board[1]}  |5  {board[5]}  |9  {board[9]}  
   ------|------|------
   6  {board[6]}  |7  {board[7]}  |2  {board[2]}  \n""")


class Computer:

    def __init__(self, symbol):
        self.symbol = symbol
        if symbol == "X":
            self.opp_symbol = "O"
        else:
            self.opp_symbol = "X"

    def make_move(self, move):
        if board[move] == " ":
            board[move] = self.symbol
            positions[self.symbol].append(move)
            return True
        else:
            return False

    def play_turn(self):
        move = self.check_for_win()
        if(move):
            self.make_move(move)
            print(f"{self.symbol} Made WINING move")
            return True
        else:
            move = self.check_for_block()
            if(move):
               self.make_move(move)
               print(f"{self.symbol} Made BLOCKING move")
            else:
               self.make_random_move()
               print(f"{self.symbol} Made RANDOM move")
            return False

    def make_random_move(self):
        move = randint(1, 9)
        if(self.make_move(move)):
            return
        else:
            self.make_random_move()
        return

    def check_for_win(self):
        for i in range(0, len(positions[self.symbol])-1):
            for j in range(i+1, len(positions[self.symbol])):
                win_pos = 15 - (positions[self.symbol]
                                [i] + positions[self.symbol][j])
                if(10 > win_pos > 0 and board[win_pos] == " "):
                    return win_pos

    def check_for_block(self):
        for i in range(0, len(positions[self.opp_symbol])-1):
            for j in range(i+1, len(positions[self.opp_symbol])):
                win_pos = 15 - (positions[self.opp_symbol]
                                [i] + positions[self.opp_symbol][j])
                if(10 > win_pos > 0 and board[win_pos] == " "):
                    return win_pos


class Player:

   def __init__(self, symbol):
      self.symbol = symbol

   def play_turn(self):
      move = int(input("Choose an empty position to make a Move : "))
      if board[move] == " ":
         board[move] = self.symbol
         positions[self.symbol].append(move)
         if len(positions[self.symbol]) >= 3:
               for combination in combinations(positions[self.symbol], 3):
                  if sum(list(combination)) == 15:
                     return True
               return False
      else:
         print("Please enter a empty position index.\n")
         self.play_turn()



def p_vs_comp():
    new_board()
    moves = 0
    win = False

    player_symbol = input("\nChoose symbol [X/O] : ")
    if player_symbol in ("X", "x"):
        player1 = Player("X")
        comp1 = Computer("O")
    else:
        player1 = Player("O")
        comp1 = Computer("X")

    print_board()
    for i in range(1, 10):
        win = player1.play_turn()
        moves += 1
        print_board()
        if win:
            print(f"Player1 ({player1.symbol}) WINS!!!")
            break
        if moves == 9:
            break

        win = comp1.play_turn()
        moves += 1
        print_board()
        if win:
            print(f"Computer ({comp1.symbol}) WINS!!!")
            break

    if win == False:
        print("Its a DRAWWW")

    if(input("\nPlay again [y/n] : ") in ("y", "Y")):
        p_vs_comp()


while True:
    print("\n\n")
    print("\033[32mAnish Vaidya Roll-62\033[0m")
    print("\033[32mArtificial Intelligence Assign-1 Part-1\033[0m")
    print(
        "\033[33mImplementation of NON-AI technique to solve TIC TAC TOE problem\033[0m")
    choice = int(input("\nTIC TAC TOE! \n1.Play Game\n2.Exit\nChoice : "))
    if choice == 1:
        p_vs_comp()
    elif choice == 2:
        print("\033[31mProgram Terminated!\033[0m")
        break
    else:
        print("\nPlease enter a valid choice\n")
