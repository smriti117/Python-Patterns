""" 
		*
	  * *
  	* * *
  *	* * *
* * * * *
  *	* * *
  	* * *
	  * *
		*
"""
n = int(input("Enter number of stars to print: "))
# n = 5 

for row in range(n):
	print((n-row)*"  ", end="")
	print(row*" *", end="")
	print()

for row in range(n,0,-1):
	print((n-row)*"  ", end="")
	print(row*" *",end="")
	print()


