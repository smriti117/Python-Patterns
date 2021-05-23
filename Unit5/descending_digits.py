""" 
5 4 3 2 1 
 5 4 3 2
  5 4 3 
   5 4
    5
"""
n = 5
for row in range(0,n):
	print((row)*" ",end=" ")
	for col in range(n-row):
		print(n-col,end=" ")
	print()