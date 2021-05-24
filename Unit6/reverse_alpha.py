""" 
      E
     E D
    E D C
   E D C B
  E D C B A
   E D C B
    E D C
     E D
      E
"""

n = 5
for row in range(0,n):
	print((n-row)*" ", end=" ")
	for column in range(row+1):
		print(chr(69-column), end=" ")
	print()

for row in range(n,1,-1):
	print((n-row+2)*" ", end=" ")
	for column in range(0,row-1):
		print(chr(69-column), end=" ")
	print()