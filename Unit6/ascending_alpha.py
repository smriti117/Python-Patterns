""" 
  	  A
     A B
    A B C
   A B C D
  A B C D E
   A B C D
    A B C
     A B
      A
"""

n = 5 
for row in range(0,n):
	print((n-row)*" ", end=" ")
	for column in range(row+1):
		print(chr(65+column), end=" ")
	print()
for row in range(0,n):
	print((row+2)*" ",end=" ")
	for column in range(0,n-row-1):
		print(chr(65+column), end=" ")
	print()