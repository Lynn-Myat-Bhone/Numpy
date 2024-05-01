import  numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[2,4,3],[1,9,5]])
#finding outer product
print(np.outer(a,b)) # ( a*b = |a||a|sinQ ) formula
#cross product of two vector
print(np.cross(a,b))