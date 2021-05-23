""" 
* * * * *
 * * * *
  * * *
   * * 
    *
"""

n = 5 
for row in range(n):
	print((row)*" ",end=" ")
	for col in range(0,1):
		print((n-row)*"* ",end=" ")
	print()