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

for row in range(1,n+1):
	print("  "* (n-row), end= " ")
	for column in range(1,row+1):
		print(chr(64+column), end=" ")
	print()

for row in range(n,1,-1):
	print("  "* (n-row+1), end= " ")
	for column in range(1,row):
		print(chr(64+column), end=" ")
	print()


