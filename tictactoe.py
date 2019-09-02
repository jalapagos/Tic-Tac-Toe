class Player:

	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol 


class Move:

	def __init__(self, row, col):
		self.row = row
		self.col = col


class TicTacToe:

	def __init__(self, player):
		self.player = player
		self.opp = Player("AI", "O")
		self.board = [[ "_" for x in range(3)] for y in range(3)]
		self.over = False
		self.turn = 'Player'
		self.winner = ''

	def printBoard(self):
		for row in range(len(self.board)):
			currRow = ''
			for col in range(len(self.board[0])):
				currRow += ' '+self.board[row][col]
			print(currRow)

	def startGame(self):
		
		while not self.gameOver(self.opp.symbol):
			self.printBoard()

			allMoves = self.allPossibleMoves()

			if self.turn == 'Player':
				print("{}'s turn!".format(self.player.name))

				while True:
					row = input


				row = int(input("{}, enter row of your move : ".format(self.player.name)))
				col = int(input("{}, enter col of your move : ".format(self.player.name)))

				if [row, col] in allMoves:
					self.makeMove(self.player.symbol, Move(row,col))

			else:
				print()
				print("{}'s turn!".format(self.opp.name))
				move = self.minmax(len(self.allPossibleMoves()), 1)
				self.makeMove(self.opp.symbol, Move(move[0],move[1]))

			self.turn = "Player" if self.turn == "Opp" else "Opp"


	def allPossibleMoves(self):
		allMoves = []
		for x in range(len(self.board)):
			for y in range(len(self.board[0])):
				if self.board[x][y] == '_':
					allMoves.append([x,y])

		return allMoves

	def gameOver(self,symbol):
		allWinScenarios = [
	        [self.board[0][0], self.board[0][1], self.board[0][2]],
	        [self.board[1][0], self.board[1][1], self.board[1][2]],
	        [self.board[2][0], self.board[2][1], self.board[2][2]],
	        [self.board[0][0], self.board[1][0], self.board[2][0]],
	        [self.board[0][1], self.board[1][1], self.board[2][1]],
	        [self.board[0][2], self.board[1][2], self.board[2][2]],
	        [self.board[0][0], self.board[1][1], self.board[2][2]],
	        [self.board[2][0], self.board[1][1], self.board[0][2]],
	    ]

		if [symbol,symbol,symbol] in allWinScenarios:
			return True
		else:
			return False

	def score(self):
		if self.gameOver(self.opp.symbol):
			return 1
		elif self.gameOver(self.player.symbol):
			return -1
		else:
			return 0

	def gameOverHelper(self):
		return self.gameOver(self.player.symbol) or self.gameOver(self.opp.symbol)

	def makeMove(self, symbol, move):
		self.board[move.row][move.col] = symbol

	def minmax(self, depth, p):
		symbol = 'O' if p == 1 else 'X'

		if p == 1:
			nextMove = [-1,-1,float('-inf')]
		else:
			nextMove = [-1,-1,float('inf')]

		if depth == 0 or self.gameOverHelper():
			score = self.score()
			return [-1,-1, score]

		allMoves = self.allPossibleMoves()

		for move in allMoves:
			row = move[0]
			col = move[1]

			self.board[row][col] = symbol
			score = self.minmax(depth - 1, -p)
			self.board[row][col] = '_'
			score[0] = row
			score[1] = col

			if p == 1:

				if score[2] > nextMove[2]:
					nextMove = score
					
			else:
				if score[2] < nextMove[2]:
					nextMove = score
		return nextMove


p = Player("Jalaj", "X")
board = TicTacToe(p)
board.startGame()
