#!/usr/bin/env python
import struct, string, math, time, copy
num_of_assignments = 0
num_of_con_check = 0

class SudokuBoard:
    """This will be the sudoku board game object your player will manipulate."""
  
    def __init__(self, size, board):
      """the constructor for the SudokuBoard"""
      self.BoardSize = size #the size of the board
      self.CurrentGameBoard= board #the current state of the game board

    def set_value(self, row, col, value):
        """This function will create a new sudoku board object with the input
        value placed on the GameBoard row and col are both zero-indexed"""

        #add the value to the appropriate position on the board
        self.CurrentGameBoard[row][col]=value
        #return a new board of the same size with the value added
        return SudokuBoard(self.BoardSize, self.CurrentGameBoard)
                                                                  
                                                                  
    def print_board(self):
        """Prints the current game board. Leaves unassigned spots blank."""
        div = int(math.sqrt(self.BoardSize))
        dash = ""
        space = ""
        line = "+"
        sep = "|"
        for i in range(div):
            dash += "----"
            space += "    "
        for i in range(div):
            line += dash + "+"
            sep += space + "|"
        for i in range(-1, self.BoardSize):
            if i != -1:
                print "|",
                for j in range(self.BoardSize):
                    if self.CurrentGameBoard[i][j] > 9:
                        print self.CurrentGameBoard[i][j],
                    elif self.CurrentGameBoard[i][j] > 0:
                        print "", self.CurrentGameBoard[i][j],
                    else:
                        print "  ",
                    if (j+1 != self.BoardSize):
                        if ((j+1)//div != j/div):
                            print "|",
                        else:
                            print "",
                    else:
                        print "|"
            if ((i+1)//div != i/div):
                print line
            else:
                print sep

def parse_file(filename):
    """Parses a sudoku text file into a BoardSize, and a 2d array which holds
    the value of each cell. Array elements holding a 0 are considered to be
    empty."""

    f = open(filename, 'r')
    BoardSize = int( f.readline())
    NumVals = int(f.readline())

    #initialize a blank board
    board= [ [ 0 for i in range(BoardSize) ] for j in range(BoardSize) ]

    #populate the board with initial values
    for i in range(NumVals):
        line = f.readline()
        chars = line.split()
        row = int(chars[0])
        col = int(chars[1])
        val = int(chars[2])
        board[row-1][col-1]=val
    
    return board
    
def is_complete(sudoku_board):
    """Takes in a sudoku board and tests to see if it has been filled in
    correctly."""
    BoardArray = sudoku_board.CurrentGameBoard
    size = len(BoardArray)
    subsquare = int(math.sqrt(size))

    #check each cell on the board for a 0, or if the value of the cell
    #is present elsewhere within the same row, column, or square
    for row in range(size):
        for col in range(size):
            if BoardArray[row][col]==0:
                return False
            for i in range(size):
                if ((BoardArray[row][i] == BoardArray[row][col]) and i != col):
                    return False
                if ((BoardArray[i][col] == BoardArray[row][col]) and i != row):
                    return False
            #determine which square the cell is in
            SquareRow = row // subsquare
            SquareCol = col // subsquare
            for i in range(subsquare):
                for j in range(subsquare):
                    if((BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j]
                            == BoardArray[row][col])
                        and (SquareRow*subsquare + i != row)
                        and (SquareCol*subsquare + j != col)):
                            return False
    return True

def init_board(file_name):
    """Creates a SudokuBoard object initialized with values from a text file"""
    board = parse_file(file_name)
    return SudokuBoard(len(board), board)

def solve(initial_board, forward_checking = False, MRV = False, Degree = False,
    LCV = False):
    """Takes an initial SudokuBoard and solves it using back tracking, and zero
    or more of the heuristics and constraint propagation methods (determined by
    arguments). Returns the resulting board solution. """
    print "Your code will solve the initial_board here!"
    print "Remember to return the final board (the SudokuBoard object)."
    print "I'm simply returning initial_board for demonstration purposes."
    global num_of_assignments
    global num_of_con_check
    num_of_assignments = 0
    num_of_con_check = 0
    if forward_checking == False and MRV == False and Degree == False and LCV == False:
        print "back_tracking"
        start = time.time()
        if back_tracking(initial_board):
            end = time.time()
            print round(end - start, 2)
            print "Consistency checks: ", num_of_con_check
            print "variable assignment: ", num_of_assignments
            return True
        return False
    elif forward_checking:
        print "forward_checking"
        # print_domain(create_domain_board(initial_board))
        start = time.time()
        if backtracking_with_fc(initial_board, create_domain_board(initial_board)):
            end = time.time()
            print round(end - start, 2)
            print "Consistency checks: ", num_of_con_check
            print "variable assignment: ", num_of_assignments
            return True
        return False
    
    return initial_board

def back_tracking(initial_board):
    #pass
    board_size = initial_board.BoardSize
    for i in range(board_size):
        for j in range(board_size):
            if initial_board.CurrentGameBoard[i][j] == 0:
                for n in range(1,board_size+1):
                    global num_of_con_check
                    num_of_con_check += 1
                    if isValid(initial_board, i, j, n):
                        global num_of_assignments
                        num_of_assignments += 1
                        initial_board.CurrentGameBoard[i][j] = n
                        if back_tracking(initial_board):
                            return True
                        else:
                            initial_board.CurrentGameBoard[i][j] = 0
                return False
    return True

def isValid(initial_board, i, j, n):
    board_size = initial_board.BoardSize

    for row in range(board_size):
        if initial_board.CurrentGameBoard[row][j] == n:
            return False

    for col in range(board_size):
        if initial_board.CurrentGameBoard[i][col] == n:
            return False

    square_size = int(math.sqrt(board_size))
    for row in range((int(i/square_size))*square_size, (int(i/square_size))*square_size+square_size):
        for col in range((int(j/square_size))*square_size, (int(j/square_size))*square_size+square_size):
            if initial_board.CurrentGameBoard[row][col] == n:
                return False

    return True

def backtracking_with_fc(initial_board, domain_board): #, MRV = False, Degree = False, LCV = False):
    board_size = initial_board.BoardSize
    # domain_board = update_domain(initial_board)

    # for row in range(board_size):
    #     for col in range(board_size):
    #         print domain_board[row][col]

    #print domain_board[0][2]

    for i in range(board_size):
        for j in range(board_size):
            if initial_board.CurrentGameBoard[i][j] == 0:
                #print domain_board[i][j]
                for n in domain_board[i][j]:
                    global num_of_con_check
                    num_of_con_check += 1
                    if isValid(initial_board, i, j, n):
                        global num_of_assignments
                        num_of_assignments += 1

                        initial_board.CurrentGameBoard[i][j] = n

                        cur_domain = domain_board[i][j][:]
                        # domain_board_copy = copy.deepcopy(domain_board)
                        changed = update_domain(domain_board, i, j, n)

                        if backtracking_with_fc(initial_board, domain_board):
                            return True
                        else:
                            initial_board.CurrentGameBoard[i][j] = 0
                            domain_board[i][j] = cur_domain[:]
                            recover(domain_board, changed, n)
                            # domain_board = domain_board_copy
                return False
    return True

def update_domain(domain_board, x, y, n):
    board_size = len(domain_board)
    domain_board[x][y] = []
    # k = 1
    # for i in range(board_size):
    #     for j in range(board_size):
    #         if type(domain_board[i][j]) == type(k):
    #             print type(domain_board[i][j]), i, j
    #             print domain_board[i][j]

    changed = []
    # tmp = []

    # remove n from domains in colum j
    for row in range(board_size):
        if n in domain_board[row][y]:
            domain_board[row][y].remove(n)
            changed.append([row, y])    

    # remove n from domains in row i
    for col in range(board_size):
        if n in domain_board[x][col]:
            domain_board[x][col].remove(n)
            changed.append([x,col])

    # remove n from domains in subsquare
    square_size = int(math.sqrt(board_size))
    for row in range((int(x/square_size))*square_size, (int(x/square_size))*square_size+square_size):
        for col in range((int(y/square_size))*square_size, (int(y/square_size))*square_size+square_size):
            if n in domain_board[row][col]:
                domain_board[row][col].remove(n)
                changed.append([row,col])

    return changed

def recover(domain_board, changed, n):
    for p in changed:
        domain_board[p[0]][p[1]].append(n)

def create_domain_board(initial_board):
    board_size = initial_board.BoardSize
    domain_board = [ [ [] for i in range(board_size) ] for j in range(board_size) ]
    
    for row in range(board_size):
        for col in range(board_size):
            domain_board[row][col] = [ i + 1 for i in range(board_size) ]

    for i in range(board_size):
        for j in range(board_size):
            n = initial_board.CurrentGameBoard[i][j]
            if n != 0:
                update_domain(domain_board, i, j, n)
                domain_board[i][j] = []

    return domain_board

def print_domain(domain_board):
    for row in range(len(domain_board)):
        for col in range(len(domain_board)):
            print row, col, domain_board[row][col]

    # return domain_board
    
    # domain_board = [ [ [] for i in range(board_size) ] for j in range(board_size) ]
    # domain = [ i + 1 for i in range(board_size) ]

    # for row in range(board_size):
    #     for col in range(board_size):
    #         domain_board[row][col] = [ i + 1 for i in range(board_size) ]

    #print domain_board[0][2]

    
            

    # for row in range(board_size):
    #     for col in range(board_size):
    #         print domain_board[row][col]
