""" 
	A 
   A B 
  A B C 
 A B C D 
A B C D E
"""
n = 5 
for row in range(0,n):
	print((n-row)*" ", end=" ")
	for col in range(row+1):
		print(chr(65+col),end=" ")
	print()
