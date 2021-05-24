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
for row in range(1,n+1):
	for column in range(0,row):
		print(chr(69-column), end=" ")
	print()
	
for row in range(1,n):
	for column in range(0,n-row):
		print(chr(69-column), end=" ")
	print()