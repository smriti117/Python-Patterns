"""
	    1
      2 2
    3 3 3 
  4 4 4 4
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2 
        1 

"""
# n = int(input("Enter number of stars to print: "))
n = 5 

for i in range(0,n):
	print(' '*(n-i-1) + (str(i+1)) * (i+1)  )

for i in range(n):
	print(' '*(i+1) + (str(n-i-1) + '') * (n-i-1)  )
