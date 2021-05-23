""" 
E D C B A 
 E D C B 
  E D C
   E D 
    E

"""
n = 5
for row in range(0,n):
	print((row)*" ",end=" ")
	for col in range(n-row):
		print(chr(69-col),end=" ")
	print()