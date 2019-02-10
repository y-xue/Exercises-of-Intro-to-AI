# File: Player.py
# Author(s) names AND netid's:
# Date:
# Group work statement: <please type the group work statement
#      given in the pdf here>
# Defines a simple artificially intelligent player agent
# You will define the alpha-beta pruning search algorithm
# You will also define the score function in the MancalaPlayer class,
# a subclass of the Player class.


from random import *
from decimal import *
from copy import *
from MancalaBoard import *
import time

# a constant
INFINITY = 1.0e400

class Player:
    """ A basic AI (or human) player """
    HUMAN = 0
    RANDOM = 1
    MINIMAX = 2
    ABPRUNE = 3
    CUSTOM = 4
    CHALLENGER = 5
    
    def __init__(self, playerNum, playerType, ply=0):
        """Initialize a Player with a playerNum (1 or 2), playerType (one of
        the constants such as HUMAN), and a ply (default is 0)."""
        self.num = playerNum
        self.opp = 2 - playerNum + 1
        self.type = playerType
        self.ply = ply
        self.time = 0

    def __repr__(self):
        """Returns a string representation of the Player."""
        return str(self.num)
        
    def minimaxMove(self, board, ply):
        """ Choose the best minimax move.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.minValue(nb, ply-1, turn)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def maxValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.minValue(nextBoard, ply-1, turn)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
        return score
    
    def minValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue(nextBoard, ply-1, turn)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
        return score


    # The default player defines a very simple score function
    # You will write the score function in the MancalaPlayer below
    # to improve on this function.
    def score(self, board):
        """ Returns the score for this player given the state of the board """
        if board.hasWon(self.num):
            return 100.0
        elif board.hasWon(self.opp):
            return 0.0
        else:
            return 50.0

    # You should not modify anything before this point.
    # The code you will add to this file appears below this line.

    # You will write this function (and any helpers you need)
    # You should write the function here in its simplest form:
    #   1. Use ply to determine when to stop (when ply == 0)
    #   2. Search the moves in the order they are returned from the board's
    #       legalMoves function.
    # However, for your custom player, you may copy this function
    # and modify it so that it uses a different termination condition
    # and/or a different move search order.
    def alphaBetaMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        #print "Alpha Beta Move not yet implemented"
        #returns the score and the associated moved
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.alphaBetaMinValue(nb, ply-1, turn, -INFINITY, INFINITY)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s

        return score, move
                
    def alphaBetaMaxValue(self, board, ply, turn, alpha, beta):
        """ """
        if board.gameOver():
            return turn.score(board)
        
        score = -INFINITY

        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)

            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            s = opponent.alphaBetaMinValue(nextBoard, ply-1, turn, alpha, beta)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
            if score >= beta:
                return score
            if score > alpha:
                alpha = score
        return score

    def alphaBetaMinValue(self, board, ply, turn, alpha, beta):
        """ """
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)

            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            s = opponent.alphaBetaMaxValue(nextBoard, ply-1, turn, alpha, beta)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
            if score <= alpha:
                return score
            if score < beta:
                beta = score
        return score

    def customMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        move = -1
        score, alpha, beta = -INFINITY, -INFINITY, INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            s = -1
            #make a new board
            if nb.makeMove(self, m):
                s = self.customMaxValue(nb, ply, turn, alpha, beta)
            else:
                #try the move
                opp = Player(self.opp, self.type, self.ply)
                s = opp.customMinValue(nb, ply-1, turn, alpha, beta)
                #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
            #if score >= beta:
            #    return score, move
            #alpha = max(alpha, score)

        return score, move
                
    def customMaxValue(self, board, ply, turn, alpha, beta):
        """ """
        if board.gameOver():
            return turn.score(board)
        
        score = -INFINITY

        for m in board.legalMoves(self):
            if ply == 0:
                return turn.score(board)

            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            s = -1
            if nextBoard.makeMove(self, m):
                # move again
                s = self.customMaxValue(nextBoard, ply, turn, alpha, beta)
            else:
                # make a new player to play the other side
                opponent = Player(self.opp, self.type, self.ply)
                s = opponent.customMinValue(nextBoard, ply-1, turn, alpha, beta)
            
            if s > score:
                score = s
            if score >= beta:
                return score
            if score > alpha:
                alpha = score
        return score

    def customMinValue(self, board, ply, turn, alpha, beta):
        """ """
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                return turn.score(board)

            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            
            s = -1
            if nextBoard.makeMove(self, m):
                # move again
                s = self.customMinValue(nextBoard, ply, turn, alpha, beta)
            else:
                # make a new player to play the other side
                opponent = Player(self.opp, self.type, self.ply)
                s = opponent.customMaxValue(nextBoard, ply-1, turn, alpha, beta)
            
            if s < score:
                score = s
            if score <= alpha:
                return score
            if score < beta:
                beta = score
        return score

    def chooseMove(self, board):
        """ Returns the next move that this player wants to make """
        if self.type == self.HUMAN:
            move = input("Please enter your move:")
            while not board.legalMove(self, move):
                print move, "is not valid"
                move = input( "Please enter your move" )
            return move
        elif self.type == self.RANDOM:
            move = choice(board.legalMoves(self))
            print self.num, "chose move", move
            return move
        elif self.type == self.MINIMAX:
            val, move = self.minimaxMove(board, self.ply)
            print self.num, "chose move", move, " with value", val
            return move
        elif self.type == self.ABPRUNE:
            val, move = self.alphaBetaMove(board, self.ply)
            print self.num, "chose move", move, " with value", val
            return move
        elif self.type == self.CUSTOM:
            # TODO: Implement a custom player
            # You should fill this in with a call to your best move choosing
            # function.  You may use whatever search algorithm and scoring
            # algorithm you like.  Remember that your player must make
            # each move in about 10 seconds or less.
            start = time.time()
            val, move = self.customMove(board, self.ply)
            end = time.time()
            self.time += (end - start)
            print self.num, "chose move", move, " with value", val, round(end-start, 2), self.time
            return move
        elif self.type == self.CHALLENGER:
            challenger = Challenger(self.num, self.type, self.ply)
            start = time.time()
            val, move = challenger.customMove(board, challenger.ply)
            end = time.time()
            self.time += (end - start)
            print challenger.num, "chose move", move, " with value", val, round(end-start, 2), self.time
            return move
        else:
            print "Unknown player type"
            return -1


# Note, you should change the name of this player to be your netid
class yxe836(Player):
    """ Defines a player that knows how to evaluate a Mancala gameboard
        intelligently """

    def score(self, board):
        """ Evaluate the Mancala board for this player """
        # Currently this function just calls Player's score
        # function.  You should replace the line below with your own code
        # for evaluating the board

        # How far I am ahead of my opponent
        h1 = board.scoreCups[self.num-1] - board.scoreCups[self.opp-1]
        # How far my opponent is going to win
        h2 = 25 - board.scoreCups[self.opp-1]
        return h1 + h2


# choose the move that try first, based on the score of the move
class Challenger(Player):
    """ Defines a player that knows how to evaluate a Mancala gameboard
        intelligently """

    def customMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self

        prioMoveList = self.prioMoves(board, board.legalMoves(self))
        sorted(prioMoveList, key=lambda tup: tup[0])
        prioMoveList.reverse()

        for m in prioMoveList:
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.customScore(board), m[1])
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            s = -1
            #make a new board
            if nb.makeMove(self, m[1]):
                s = self.customMaxValue(nb, ply, turn, -INFINITY, INFINITY)
            else:
                #try the move
                opp = Player(self.opp, self.type, self.ply)
                s = opp.customMinValue(nb, ply-1, turn, -INFINITY, INFINITY)
                #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m[1]
                score = s

        return score, move
                
    def customMaxValue(self, board, ply, turn, alpha, beta):
        """ """
        if board.gameOver():
            return turn.customScore(board)
        
        score = -INFINITY

        prioMoveList = self.prioMoves(board, board.legalMoves(self))
        sorted(prioMoveList, key=lambda tup: tup[0])
        prioMoveList.reverse()

        for m in prioMoveList:
            if ply == 0:
                return turn.customScore(board)

            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            s = -1
            if nextBoard.makeMove(self, m[1]):
                # move again
                s = self.customMaxValue(nextBoard, ply, turn, alpha, beta)
            else:
                # make a new player to play the other side
                opponent = Player(self.opp, self.type, self.ply)
                s = opponent.customMinValue(nextBoard, ply-1, turn, alpha, beta)
            
            if s > score:
                score = s
            if score >= beta:
                return score
            if score > alpha:
                alpha = score
        return score

    def customMinValue(self, board, ply, turn, alpha, beta):
        """ """
        if board.gameOver():
            return turn.customScore(board)
        score = INFINITY

        prioMoveList = self.prioMoves(board, board.legalMoves(self))
        sorted(prioMoveList, key=lambda tup: tup[0])
        prioMoveList.reverse()

        for m in prioMoveList:
            if ply == 0:
                return turn.customScore(board)

            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            
            s = -1
            if nextBoard.makeMove(self, m[1]):
                # move again
                s = self.customMinValue(nextBoard, ply, turn, alpha, beta)
            else:
                # make a new player to play the other side
                opponent = Player(self.opp, self.type, self.ply)
                s = opponent.customMaxValue(nextBoard, ply-1, turn, alpha, beta)
            
            if s < score:
                score = s
            if score <= alpha:
                return score
            if score < beta:
                beta = score
        return score

    def customScore(self, board):
        """ Evaluate the Mancala board for this player """
        # Currently this function just calls Player's score
        # function.  You should replace the line below with your own code
        # for evaluating the board

        # How far I am ahead of my opponent
        h1 = board.scoreCups[self.num-1] - board.scoreCups[self.opp-1]
        # How far my opponent is going to win
        h2 = 25 - board.scoreCups[self.opp-1]
        return h1 + h2

        #print "Calling score in MancalaPlayer"
        
    def moveScore(self, board, move):
        n = board.P1Cups[move-1]
        overflow = max(n-6+move, 0)
        score = (n+move+7) / 13
        extra = 0
        landpos = move + n%13
        if landpos < 6 and board.P1Cups[landpos] == 0:
            extra += board.P2Cups[5-landpos]*0.25
        return score - (overflow*0.3)**2 + extra

    def prioMoves(self, board, legalMoves):
        prioMoveList = []
        for m in legalMoves:
            prioMoveList.append(self.moveScore(board, m))
        #return prioMoveList
        return zip(prioMoveList, legalMoves)

    def scores(self, board):
        """ """
        overflows = [None]*6
        scores = [None]*6
        nets = [None]*6
        maxValue = -INFINITY

        for i, n in enumerate(board.P1Cups):
            overflows[i] = max(n-6+i, 0)
            scores[i] = (n+i+7) / 13

            extra = 0
            landpos = i + n%13
            if landpos < 6 and board.P1Cups[landpos] == 0:
                extra += board.P2Cups[5-landpos]*0.25

            nets[i] = scores[i] - (overflows[i]*0.3)**2 + extra

            if nets[i] > maxValue:
                maxValue = nets[i]
                move = i

        return maxValue, move