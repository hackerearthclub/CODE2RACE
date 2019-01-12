# Grid Illumination: You are given an empty NxN grid and an array
# of lamp coordinates. Each lamp provides illumination to every
# square in their row, every square in their column, and every
# square that lies in their diagonal (aka chess Queen). Given an
# array of query coordinates, determine whether that point is
# illuminated or not. The catch is that when checking a query
# all lamps adjacent to, or on, that query get turned off.
# The ranges for the variables/arrays were about:
# 10^3 < N < 10^9, 10^3 < lamps < 10^9, 10^3 < queries < 10^9.

class Grid:
    def __init__(self, n, lamps):
        self.columns = [0] * n
        self.rows = [0] * n
        self.lamps = lamps
        self.left_diagonals = [0] * (2 * (n - 1) + 1) # cascading diagonals
        self.right_diagonals = [0] * (2 * (n - 1) + 1)
        for lamp in lamps:
            self.add_lamp(lamp)
    
    def add_lamp(self, lamp):
        x = lamp[0]
        y = lamp[1]
        self.columns[x] += 1
        self.rows[y] += 1
        self.left_diagonals[x+y] += 1
        self.right_diagonals[x-y] += 1
    
    def remove_lamp(self, lamp):
        x = lamp[0]
        y = lamp[1]
        self.columns[x] -= 1
        self.rows[x] -= 1
        self.left_diagonals[x+y] -= 1
        self.right_diagonals[x-y] -= 1
        
        self.lamps.remove(lamp)
    
    def query(self, x, y):
        # 8 adjacent cells of queried box
        neighbors = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x, y], [x + 1, y], [x - 1, y + 1], [x , y + 1], [x + 1, y + 1]]
        for neighbor in neighbors:
            if neighbor in self.lamps:
                self.remove_lamp(neighbor)
        return (self.columns[x] or self.rows[y] or self.left_diagonals[x+y] or self.right_diagonals[x-y])
