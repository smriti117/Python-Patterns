
""" 
55555
44444
33333
22222
11111

"""

n = int(input("Enter n : "))
for row in range(0,n):
	for column in range(0,n):
		print((n-row),end="")
	print()




""" 
54321
54321
54321
54321
54321
"""
n = int(input("Enter n : "))
for row in range(0,n):
	for column in range(0,n):
		print((n-column),end=" ")
	print()
