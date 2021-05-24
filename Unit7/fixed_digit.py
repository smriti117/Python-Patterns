""" 
1
22
333
4444
55555
4444
333
22
1

"""

n = 5 

for row in range(0,n+1):
	print(str(row)*row, end=" ")
	print()
	
for row in range(1,n):
	print(str(n-row)*(n-row), end=" ")
	print()
