""" 
     A
    B B
   C C C
  D D D D
 E E E E E
  D D D D
   C C C
    B B
     A


"""

n = 5
for row in range(1,n):
	print((n-row)*" ", end=" ")
	for column in range(row):
		print(chr(64+row), end=" ")
	print()


for row in range(0,n):
	print((row)*" ", end=" ")
	for column in range(n-row):
		print(chr(69-row), end=" ")
	print()