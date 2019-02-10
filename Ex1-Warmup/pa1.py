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
	midL = L[len(L)//2 - 1] # element on the left of the mid

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
				boardStr += '\n'		# switch to a new line
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

