import numpy as np
a=np.array(input("enter the first matrix a:"))
b=np.array(input("enter the second matrix a:"))
sum=np.add(a,b)
m=np.multiply(a,b)
d=np.divide(a,b)
e=np.subtract(a,b)
g=np.linalg.det(a)
t=np.trace(a)
i=np.linalg.inv(a)
ei=np.linalg.eig(a)
k=np.transpose(a)
l=np.linalg.matrix_rank(a)
print("The two matrix addition is:",sum)
print("the multiplication of two matrix is:",m)
print("the subtraction of two matrix is:",e)
print("the division of two matrix is:",d)
print("the det of the matrix is:",g)
print("the trace of the matrix is:",t)
print("the inverse of the matrix is:",i)
print("the eigen values of the matrix is:",ei)
print("the transpose of the matrix is:",k)
print("the rank of the matrix is:",l)




