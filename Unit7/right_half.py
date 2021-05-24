"""
*
**
***
****
*****
****
***
**
*
"""
n = 5 
for row in range(0,n):
	print(row*"*", end=" ")
	print()

for row in range(0,n):
	print((n-row)*"*",end=" ")
	print()