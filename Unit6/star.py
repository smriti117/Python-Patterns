""" 
      *
     * *
    * * *
   * * * *
  * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *
"""
n = int(input("Enter n : ")) 

for row in range(0,n):
	print((n-row)*" ", end=" ")
	for column in range(row+1):
		print("*", end=" ")
	print()


for row in range(0,n):
	print((row+1)*" ", end=" ")
	for column in range(n-row):
		print("*", end=" ")
	print()


	
