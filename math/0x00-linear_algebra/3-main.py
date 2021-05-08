#!/usr/bin/env python3

matrix_transpose = __import__('3-flip_me_over').matrix_transpose

mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]

for i in mat2:
    print(i)
print('-----------------------------')
for i in matrix_transpose(mat2):
    print(i)
