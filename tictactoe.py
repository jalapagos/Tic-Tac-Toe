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
		self.turn = 'Player'
		self.status = 'Draw'

	def startGame(self):
		
		while self.gameOver(self.opp.symbol) == False and len(self.allPossibleMoves()) != 0:
			self.printBoard()

			allMoves = self.allPossibleMoves()

			if self.turn == 'Player':
				print("{}'s turn!".format(self.player.name))

				while True:
					row = (input("{}, enter row of your move : ".format(self.player.name)))
					col = (input("{}, enter col of your move : ".format(self.player.name)))

					try:
						row = int(row)
						col = int(col)
					except ValueError:
						print('Please enter valid row and column')
						continue

					if [row,col] in allMoves:
						self.makeMove(self.player.symbol, Move(row,col))
						break
					else:
						print('Please enter a valid and open move')

			else:
				print()
				print("{}'s turn!".format(self.opp.name))
				move = self.minmax(len(self.allPossibleMoves()), self.opp.symbol)
				self.makeMove(self.opp.symbol, Move(move[0],move[1]))

			self.turn = "Player" if self.turn == "Opp" else "Opp"

		self.printBoard()

		if self.gameOver(self.opp.symbol):
			print('AI has won :) ')
		else:
			print('The match is a draw!')


	def allPossibleMoves(self):
		allMoves = []
		for x in range(len(self.board)):
			for y in range(len(self.board[0])):
				if self.board[x][y] == '_':
					allMoves.append([x,y])

		return allMoves

	def gameOver(self,symbol):
		#rows, cols, and diagonals
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
			self.status = "Win"
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

	def minmax(self, depth, symbol):
		bestMove = [-1,-1,float('-inf')] if symbol == "O" else [-1,-1,float('inf')]

		if depth == 0 or self.gameOverHelper():
			score = self.score()
			return [-1,-1, score]

		allMoves = self.allPossibleMoves()

		for move in allMoves:
			row = move[0]
			col = move[1]

			self.board[row][col] = symbol

			nextTurn = "X" if symbol == "O" else "O"
			score = self.minmax(depth - 1, nextTurn)
			self.board[row][col] = '_'
			score[0] = row
			score[1] = col

			if symbol == "O":

				if score[2] > bestMove[2]:
					bestMove = score
					
			else:
				if score[2] < bestMove[2]:
					bestMove = score
		return bestMove

	def printBoard(self):
		for row in range(len(self.board)):
			currRow = ''
			for col in range(len(self.board[0])):
				currRow += ' '+self.board[row][col]
			print(currRow)

def main():
	playerName = (input("What is your name? : "))
	print('The game is about to begin. Get ready to play the AI, {}!'.format(playerName))
	print()
	print('The board is zero indexed.')
	player = Player(playerName, "X")
	board = TicTacToe(player)
	board.startGame()

if __name__ == '__main__':
	main()