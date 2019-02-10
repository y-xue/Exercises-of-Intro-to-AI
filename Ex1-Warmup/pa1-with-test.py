# Name: Ye Xue
# Netid: yxe836

# Problem 1:
def binarySearch(L, v):
	""" Searches through a list L for 
	the element v using binary search"""

	lo = 0			# left bound for binary search
	hi = len(L) - 1	# right bound
	iterTimes = 0	# record number of iteration

	while lo <= hi:
		mid = (lo + hi) // 2
		if L[mid] == v:
			return (True, iterTimes)
		if v < L[mid]:
			hi = mid - 1
		else:
			lo = mid + 1
		iterTimes += 1
	return (False, iterTimes)

# Problem 2:
def mean(L):
	""" Calculates the average of list L"""

	if len(L) == 0:
		return 0

	sum = 0
	for item in L:
		sum += item
	return float(sum) / len(L)

def median(L):
	""" Calculates the median of list L"""

	if len(L) == 0:
		return 0

	L.sort()
	mid = L[len(L)//2]		# element in the middle of L
	#print 'mid', mid
	midL = L[len(L)//2 - 1] # element on the left of the mid
	#print 'midL', midL

	if len(L) % 2 == 0:
		if midL == mid:		# if midL equals mid, we don't need to calculate
			return mid 		# their mean. Avoid changing element to float.
		return (mid + midL) / 2.0
	return mid

# Problem 3:
def bfs(T, x):
	""" perform a breadth first search of tree T
	and return whether or not x is in T."""
			
	q = [T]					# put T in a list
	while len(q) != 0:		# keep searching until queue is empty
			
		elem = q.pop(0)		# pop the first elem in queue

		if len(elem) == 0:	# check if elem is empty,
			break;			# before visit it by index

		val = elem[0]		# first part of elem is current node
		q.extend(elem[1:])	# rest part of elem are children of current node
							# put children into queue
		print val 			# print search path
		if val == x:		
			return True		# return true if we find x in T
	return False

def dfs(T, x):
	""" perform a depth first search of tree T
	and return whether or not x is in T."""

	if len(T) == 0:			# check if the tree is empty,
		return False 		# before visit it by index

	val = T[0]				# get the current node value
	print val 				# print search path
	if val == x:
		return True 		# return true if we find x in T

	for item in T[1:]:		# do dfs on each child of current node
		if dfs(item, x) == True:
			return True 	# return true if we find x in T
	return False

# Problem 4:
class TTTBoard:
	""" A TTTBoard contains a board. It has following methods:
	makeMove, hasWon, checkHorizon, checkVertical, checkDiagonal,
	gameOver, isFull and clear """

	def __init__(self):
		""" init board with '*'s, when create an instance """
		self.board = ['*','*','*','*','*','*','*','*','*']

	def __str__(self):
		""" translate board to a 2D matrix """
		boardStr = ""
		i = 0							# count for number of rows
		for item in self.board:
			i += 1
			boardStr += item
			if i % 3 == 0:				# after every three rows,
				boardStr += '\n'	# switch to a new line
			else:
				boardStr += ' '
		return boardStr

	def makeMove(self, player, pos):
		""" put 'player' in 'pos' of the board and return true,
		return false if 'pos' of board is occupied """
		if pos < 0 or pos > 8:
			return False
		if self.board[pos] != '*':
			return False
		self.board[pos] = player
		return True

	def hasWon(self, player):
		""" return true if one of the players has won the game,
		if not return false """
		return self.checkHorizon(player) or self.checkVertical(player) or self.checkDiagonal(player)

	def checkHorizon(self, player):
		""" check whether there are 3 'player's in a row,
		if so, return true, otherwise return false """
		if self.board[0] == player and self.board[1] == player and self.board[2] == player:
			return True
		if self.board[3] == player and self.board[4] == player and self.board[5] == player:
			return True
		if self.board[6] == player and self.board[7] == player and self.board[8] == player:
			return True
		return False

	def checkVertical(self, player):
		""" check whether there are 3 'player's in a column,
		if so, return true, otherwise return false """
		if self.board[0] == player and self.board[3] == player and self.board[6] == player:
			return True
		if self.board[1] == player and self.board[4] == player and self.board[7] == player:
			return True
		if self.board[2] == player and self.board[5] == player and self.board[8] == player:
			return True
		return False

	def checkDiagonal(self, player):
		""" check whether there are 3 'player's in a diagonal,
		if so, return true, otherwise return false """
		if self.board[0] == player and self.board[4] == player and self.board[8] == player:
			return True
		if self.board[2] == player and self.board[4] == player and self.board[6] == player:
			return True
		return False

	def gameOver(self):
		""" return true if one of the players has won the game,
		or there is no blank position on the board to put stone on """
		return self.hasWon("X") or self.hasWon("O") or self.isFull()

	def isFull(self):
		""" return true if there is no blank position
		on the board to put stone on, otherwise return false """
		if '*' in self.board:
			return False
		return True

	def clear(self):
		""" clear the board by filling the board with '*' """
		self.__init__()

print "\nProblem 1: \n"
L = [0,4,6,12,13,25,27]
print "binarySearch test case #1: " + str(binarySearch(L,-1) == (False,3))
print "binarySearch test case #2: " + str(binarySearch(L,12) == (True,0))
print "binarySearch test case #3: " + str(binarySearch(L,25) == (True,1))
L1 = [-1,0,1,1,1,1,2,2,3,4,5,6,7,8,9]
print "binarySearch test case #4: " + str(binarySearch(L1,-1) == (True,3))
print "binarySearch test case #5: " + str(binarySearch(L1,1) == (True,1))
print "binarySearch test case #6: " + str(binarySearch(L1,2) == (True,0))
print "binarySearch test case #7: " + str(binarySearch(L1,9) == (True,3))
print "binarySearch test case #8: " + str(binarySearch(L1,15) == (False,4))
L2 = []
print "binarySearch test case #1: " + str(binarySearch(L2,-1) == (False,0))
print "binarySearch test case #2: " + str(binarySearch(L2,12) == (False,0))
print "binarySearch test case #3: " + str(binarySearch(L2,25) == (False,0))

print "\nProblem 2: \n"
x = [5,1,2,3,1] 
y = [5,1,2,3,1,4]
print "mean test case #1: " + str(mean(x) == float(12)/float(5))
print "mean test case #2: " + str(mean(y) == float(16)/float(6))
print "median test case #1: " + str(median(x) == 2)
print "median test case #2: " + str(median(y) == 2.5)
x1 = [1.1, 2.1, 3.1, 4.1, 5.1, 14.5] 
y1 = []
print "mean test case #1: " + str(mean(x1) == 5.0)
print "mean test case #2: " + str(mean(y1) == 0)
print type(median(x1))
print "median test case #1: " + str(median(x1) == 3.6)
print "median test case #2: " + str(median(y1) == 0)

x2 = [1.1, 2.1, 3.2, 4.4, 5.1, 15.5]
print "median test case #1: " + str(round(median(x2),1) == 3.8)

from decimal import Decimal
print "median test case #1: " + str(Decimal(median(x2)))

x2 = [1.1, 2.1, 3.2, 4.6, 5.1, 15.5]
print "median test case #1: " + str(median(x2) == 3.9)
print "median test case #1: " + str(Decimal(median(x2)))


print "\nProblem 3: \n"
myTree = [4, [10, [33], [2]], [3], [14, [12]], [1]]
print "bfs test case #1: " + str(bfs(myTree, 1) == True)
print "bfs test case #2: " + str(bfs(myTree, 7) == False)

print str(bfs([], 1) == False)
print str(dfs([], 1) == False)
print str(bfs([1], 1) == True)
print str(dfs([1], 1) == True)
print str(bfs([1, [2, [3, [4]]]], 4) == True)
print str(dfs([1, [2, [3, [4]]]], 4) == True)

print "\nProblem 4: \n"
            
myB = TTTBoard()
print myB
myB.makeMove("X", 8)
myB.makeMove("O", 7)
myB.makeMove("X", 5)
myB.makeMove("O", 6)
myB.makeMove("X", 2)
print myB

print "tic tac toe test case #1: " + str(myB.hasWon("X") == True)
print "tic tac toe test case #2: " + str(myB.hasWon("O") == False)
