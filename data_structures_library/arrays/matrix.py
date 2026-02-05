"""
matrix - 2d array
"""

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for_in range(rows)]

    def set(self, r, c, value):
        if 0 <= r self.rows and 0 <= c < self.cols:
            self.data[r][c] = value
        else:
            raise IndexError("index out of bounds") 
    
    def get(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.data[r][c]
        raise IndexError("indecx out of bounds")
    
    def display(self):
        for row in self.data:
            print(row)

if __name__ == "__main__":
    m = Matrix(2,3)
    m.set(0,0,1)
    m.set(1,2,5)
    m.display()
    
    