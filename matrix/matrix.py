class Matrix:
    def __init__(self, matrix_string):
        self.mat = matrix_string.split()
        self.nrows = matrix_string.count("\n") + 1
        self.ncols = 1
        for c in matrix_string:
            if c == '\n':
                break
            if c.isspace():
                self.ncols += 1

    def row(self, index):
        mat_row = []
        # row n=index of a (nrows)x(ncols) matrix starts at the ((n-1)*ncols) position of the list (since list elements start at position 0 and i have to traverse ncols worth of elements (n-1) times)
        # loop stops after ncols number of iterations (since every row is has ncols worth of elements)
        # loop increments by 1 since row elements are all sequential 
        for i in range((index-1)*self.ncols, (index-1)*self.ncols+self.ncols):
            mat_row.append(int(self.mat[i]))
        return mat_row

    def column(self, index):
        mat_col = []
        # column n=index always starts at the first row, at the (n-1) index (since list elements start at position 0) 
        # loop increments by ncols elements each time (since that's how many elements we have to skip over in order to reach the next element in column n)
        # (nrows-1)*ncols gets us to the bottom left corner of the matrix, so the last element of the nth column is at position (index+(nrows-1)*ncols)
        for i in range(index-1, (index)+((self.nrows-1)*self.ncols), self.ncols):
            mat_col.append(int(self.mat[i]))
        return mat_col

