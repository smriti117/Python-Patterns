""" 
	    5
	  5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1
  5 4 3 2
    5 4 3
	  5 4
	    5

"""
n = 5 
for row in range(1,n+1):
	print("  "*(n-row+1), end=" ")
	for column in range(row):
		print(n-column, end=" ")
	print() 

for row in range(n-1,0,-1):
	print("  "*(n-row+1), end=" ")
	for column in range(row):
		print(n-column, end=" ")
	print() 