"""
E D C B A 
E D C B 
E D C 
E D 
E 
"""

n = 5
for row in range(n,0,-1):
	for col in range(row):
		print(chr(69-col),end=" ")
	print()