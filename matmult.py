def main():
    #setup, take input and populate matricies 
    s = input()
    # convert input to int
    aRows = int(s[0])
    aCols = int(s[2])
    matrixA = [[0.0 for i in range(aCols)] for i in range(aRows)] # declare 2d matrix, all values = 0.0 for float array
    matrixA = populate_matrix(matrixA, aRows, aCols)
    s = input()
    bRows = int(s[0])
    bCols = int(s[2])
    if(aCols != bRows):
        print("invalid input") 
        return
    matrixB = [[0 for i in range(bCols)] for i in range(bRows)]
    matrixB = populate_matrix(matrixB, bRows, bCols)
    #initalize result array
    ansRows = aRows
    ansCols = bCols
    matrixAns = [[0 for i in range(ansCols)] for i in range(ansRows)]
    for i in range(aRows):
        for j in range (bCols):
            for k in range (bRows):
                matrixAns[i][j] = matrixAns[i][j] + (matrixA[i][k] * matrixB[k][j])
    for i in range(ansRows):
        for j in range(ansCols):
            print(matrixAns[i][j])
    
# Populates 2d array from stdin 
# Takes matrix, row size and column size as input
def populate_matrix(matrix, rows, cols):
    for i in range(rows):
        s = input()
        spl = s.split(" ")
        for j in range(cols):
            matrix[i][j] = float(spl[j]) 
    return matrix

if __name__ == '__main__':
    main()
