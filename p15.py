# answer for n x n grid is the sum of the numbers along a diagonal in a Pascal's triangle

def pascal(n):
    max_level = 2*n
    pascal_triangle = [[0], [1], [1, 1]]
    for i in range(2, max_level):  
        prev_row_length = len(pascal_triangle[i]) # = 2
        row = []
        for j in range(0, prev_row_length + 1):
            if j == 0:
                row.append(pascal_triangle[i][j])
            elif j == prev_row_length:
                row.append(pascal_triangle[i][j - 1])
            else: 
                total = pascal_triangle[i][j-1] + pascal_triangle[i][j]
                row.append(total)
        pascal_triangle.append(row)

    return pascal_triangle

def solution(n):

    pascal_triangle = pascal(n)
    index = 0
    total_routes = 0
    for i in range(n, 2*n + 1):
        total_routes += pascal_triangle[i][index]
        index += 1

    return total_routes

print solution(20)
