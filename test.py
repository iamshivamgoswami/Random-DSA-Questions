def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
	@functools.lru_cache(None)
	def travels(xcurr, ycurr, k):
		if xcurr < 0 or xcurr >= N or ycurr < 0 or ycurr >= N:
			# We're already outside the grid, so probability of staying inside is 0
			return 0
		elif k == 0:
			# We're inside the grid and have no more moves to make
			return 1
		else:
			# Otherwise, we make one of 8 possible moves and find the probability of staying inside after
			# k - 1 more moves. Because each move is equally likely, we average all of these probabilities.
			return (travels(xcurr + 2, ycurr + 1, k - 1) +
					travels(xcurr + 1, ycurr + 2, k - 1) +
					travels(xcurr - 1, ycurr + 2, k - 1) +
					travels(xcurr - 2, ycurr + 1, k - 1) +
					travels(xcurr - 2, ycurr - 1, k - 1) +
					travels(xcurr - 1, ycurr - 2, k - 1) +
					travels(xcurr + 1, ycurr - 2, k - 1) +
					travels(xcurr + 2, ycurr - 1, k - 1)) / 8

	return travels(r, c, K)