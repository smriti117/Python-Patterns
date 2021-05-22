""" 
E 
E D 
E D C 
E D C B
E D C B A
"""

n = 5
for row in range(0,n):
	for col in range(row+1):
		print(chr(69-col), end=" ")
	print()
