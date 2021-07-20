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
	print("  "*(n-row+1), end=" ")
	for column in range(row):
		print(chr(69-column), end=" ")
	print() 

for row in range(n-1,0,-1):
	print("  "*(n-row+1), end=" ")
	for column in range(row):
		print(chr(69-column), end=" ")
	print() 