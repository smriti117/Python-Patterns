""" 
	*
   * *
  * * *
 * * * * 
* * * * * 
"""

n = 5 

# for row in range(0,n):
# 	print((n-row)*" ",end=" ")
# 	print((row)*" * ",end=" ")
# 	print((n-row)*" ",end=" ")
# 	print()

#OR 

for row in range(0,n):
	print((n-row)*" ",end=" ")
	for column in range(0,1):
		print((row)*" *",end=" ")
		for space in range(0,1):
			print((n-row)*" ",end=" ")
	print()

