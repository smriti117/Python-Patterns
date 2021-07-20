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

for row in range(0,n):
	print(' '*(n-row-1), chr(65+row) * (row+1))

for row in range(0,n):
	print(' '*(row+1), chr(68-row) * (n-row-1))