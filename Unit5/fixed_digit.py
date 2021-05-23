""" 
1 1 1 1 1
 2 2 2 2
  3 3 3
   4 4 
    5
"""

n = 6 
for row in range(1,n):
	print((row)*" ",end=" ")
	for col in range(n-row):
		print(str(row),end=" ")
	print()