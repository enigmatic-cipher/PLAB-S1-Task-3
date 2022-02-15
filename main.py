"""
Define two function named square and cube which takes n as input. Use these functions to print cube and square of every element from the input list. [1,7,9,12]
"""

def Square(n):
  return n*n

def Cube(n):
  return n*n*n

ls = [1,7,9,12]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  sq = Square(e)
  print(sq)
for j in range(0,ln):
  e = ls[j]  
  cu = Cube(e)
  print(cu)
