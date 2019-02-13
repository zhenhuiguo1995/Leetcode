class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return board
        self.UNREVEALED_MINE = 'M'
        self.UNREVEALED_EMPTY_SQUARE = 'E'
        self.REVEALED_BLANK_SQUARE = 'B'
        self.REVEALED_MINE = 'X'
        # you have to add a visited set to remove duplicates
        # otherwise one node may enqueue multiple times
        self.visited = set()
        
        x, y = click[0], click[1]
        if board[x][y] == self.UNREVEALED_MINE:
            board[x][y] = self.REVEALED_MINE
        elif board[x][y] == self.UNREVEALED_EMPTY_SQUARE:
            self.mark_by_bfs(board, x, y)
        return board
        
    def mark_by_bfs(self, board, x, y):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                     (1, 1), (-1, 1), (1, -1), (-1, -1)]
        queue = [(x, y)]
        self.visited.add((x, y))
        while queue:
            i, j = queue.pop(0)
            mines = 0
            pending = []
            # search for 8 directions
            for (m, n) in directions:
                if self.in_bound(board, i + m, j + n):
                    if board[i+m][j+n] == self.UNREVEALED_MINE:
                        mines += 1
                    elif board[i+m][j+n] == self.UNREVEALED_EMPTY_SQUARE:
                        # print(board[i+m][j+n])
                        pending.append((i+m, j+n))
            # if there are mines surrounding board[i][j]
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = self.REVEALED_BLANK_SQUARE
                for pair in pending:
                    if pair not in self.visited:
                        queue.append(pair)
                        self.visited.add(pair)
                
                
    def in_bound(self, board, x, y):
        rows, columns = len(board), len(board[0])
        if x >= 0 and x < rows and y >= 0 and y < columns:
            return True
        return False
        