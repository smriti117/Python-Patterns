""" 
	A
   B B
  C C C 
 D D D D 
E E E E E

"""
n=6
for row in range(0,n):
	print((n-row)*" ",end=" ")
	for column in range(0,1):
		print((chr(64+row)+" ")*(row),end=" ")
		for space in range(0,1):
			print((n-row)*" ",end=" ")
	print()
