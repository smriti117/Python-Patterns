""" 

A A A A A
 B B B B
  C C C
   D D
    E

"""

n = 5
for row in range(0,n):
	print((row)*" ",end=" ")
	for col in range(n-row):
		print(chr(65+row),end=" ")
	print()