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
		self.opp = Player("AI", "X")
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
		
		while not self.gameOver():
			self.printBoard()

			allMoves = self.allPossibleMoves()
			#print('All moves are {}'.format(allMoves))
			#break

			if self.turn == 'Player':
				print("{}'s turn!".format(self.player.name))
				row = int(input("{}, enter row of your move : ".format(self.player.name)))
				col = int(input("{}, enter col of your move : ".format(self.player.name)))

				if (row, col) in allMoves:
					self.makeMove(self.player.symbol, Move(row,col))

			else:
				print()
				print("{}'s turn!".format(self.opp.name))
				self.minmax()

			self.turn = "Player" if self.turn == "Opp" else "Opp"


	def allPossibleMoves(self):
		allMoves = set()
		for x in range(len(self.board)):
			for y in range(len(self.board[0])):
				if self.board[x][y] == '_':
					allMoves.add((x,y))

		return allMoves

	def gameOver(self):

		symbol = self.opp.symbol if self.turn == "Opp" else self.player.symbol

		allWinningBoards = [[self.board[0][0], self.board[0][1], self.board[0][2]],
				        [self.board[1][0], self.board[1][1], self.board[1][2]],
				        [self.board[2][0], self.board[2][1], self.board[2][2]],
				        [self.board[0][0], self.board[1][0], self.board[2][0]],
				        [self.board[0][1], self.board[1][1], self.board[2][1]],
				        [self.board[0][2], self.board[1][2], self.board[2][2]],
				        [self.board[0][0], self.board[1][1], self.board[2][2]],
				        [self.board[2][0], self.board[1][1], self.board[0][2]] ]

		if [symbol, symbol, symbol] in allWinningBoards:
			return True

		else: 
			return False







p = Player("Jalaj", "1")
board = TicTacToe(p)
board.startGame()
