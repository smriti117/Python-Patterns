
""" 
Enter n : 5
EEEEE
DDDDD
CCCCC
BBBBB
AAAAA
"""

n = int(input("Enter n : "))
for row in range(0,n):
	for column in range(0,n):
		print(chr(69-row), end="")
	print()


""" 
EDCBA
EDCBA
EDCBA
EDCBA
EDCBA
"""

n = int(input("Enter n : "))
for row in range(0,n):
	for column in range(0,n):
		print(chr(69-column), end="")
	print()
