""" 
      5
     5 4
    5 4 3
   5 4 3 2
  5 4 3 2 1
   5 4 3 2
    5 4 3
     5 4
      5
"""
n = 5
for row in range(0,n):
	print((n-row)*" ", end=" ")
	for column in range(row+1):
		print(n-column, end=" ")
	print()

for row in range(n,1,-1):
	print((n-row+2)*" ", end=" ")
	for column in range(0,row-1):
		print(n-column, end=" ")
	print()