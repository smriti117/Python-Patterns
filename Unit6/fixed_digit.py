""" 
     1
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
     1
"""

n = 5
for row in range(1,n):
	print((n-row)*" ", end=" ")
	for column in range(row):
		print(row, end=" ")
	print()


for row in range(n,0,-1):
	print((n-row)*" ", end=" ")
	for column in range(row):
		print(row, end=" ")
	print()