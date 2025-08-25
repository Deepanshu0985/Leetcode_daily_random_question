
from traitlets import List
def findDiagonalOrder(mat):
    n= len(mat)
    m = len(mat[0])
    row = 0
    col =0
    up = True
    ans =[]
    
    for _ in range(n*m):
        ans.append(mat[row][col])
        if up:
            if col == m-1:
                row+=1
                up = not up
            elif row == 0:
                col+=1
                up = not up
            else:
                row-=1
                col+=1
        else:
            if row==n-1:
                col+=1
                up = not up
            elif col == 0:
                row+=1
                up = not up
            else:
                row+=1
                col-=1
    return ans

print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12,13]]))
                
                