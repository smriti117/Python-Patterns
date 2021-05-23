""" 
1 2 3 4 5 
 1 2 3 4
  1 2 3
   1 2
    1

"""
n = 5
for row in range(0,n):
	print((row)*" ",end=" ")
	for col in range(n-row):
		print(col+1,end=" ")
	print()