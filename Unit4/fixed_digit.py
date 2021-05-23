""" 
	1
   2 2
  3 3 3 
 4 4 4 4
5 5 5 5 5

"""
n=6
for row in range(1,n):
	print((n-row)*" ",end=" ")
	for column in range(0,1):
		print((str(row)+" ")*(row),end=" ")
		for space in range(0,1):
			print((n-row)*" ",end=" ")
	print()

