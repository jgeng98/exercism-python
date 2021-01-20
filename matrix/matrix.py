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
        for i in range((index-1)*self.ncols, (index-1)*self.ncols+self.ncols):
            mat_row.append(int(self.mat[i]))
        return mat_row

    def column(self, index):
        mat_col = []
        for i in range(index-1, len(self.mat), self.ncols):
            mat_col.append(int(self.mat[i]))
        return mat_col
