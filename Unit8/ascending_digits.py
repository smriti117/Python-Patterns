""" 
	    1 
	  1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5
  1 2 3 4 
    1 2 3
      1 2 
        1

"""

n = 6

for row in range(1,n):
	print("  "*(n-row), end=" ")
	for column in range(1,row+1):
		print(column, end=" ") 
	print()

for row in range(n-1,1,-1):
	print("  "*(n-row+1), end=" ")
	for column in range(1,row):
		print(column, end=" ") 
	print()