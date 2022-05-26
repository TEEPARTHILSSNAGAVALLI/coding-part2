import math
A = int(input("Enter number of items sold in a day:"))
B = int(input("Enter number of items to be sold:"))
c = math.ceil(B/A)
d = math.ceil(c/6)
print("To sell ",B," no of items it take totally ",d," weeks")
