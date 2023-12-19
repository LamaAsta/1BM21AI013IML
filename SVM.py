import numpy as np


def Wval(sol,s):
    a = [np.multiply(i,j) for i,j in zip(sol,s)]
    sum = [0 for i in range(len(s))]
    for i in a:
        sum = [k+j for k,j in zip(sum,i)]
    return [round(i,3) for i in sum]

p = [[3,1],[3,-1],[6,1],[6,-1]]
n = [[1,0],[0,1],[-1,0],[0,-1]]
s = [[3,1],[3,-1],[1,0]]
sb = [i+[1] for i in s]
eq = [[np.dot(i,j) for i in sb] for j in sb]
values = [1,1,-1]
sol = np.linalg.solve(eq,values)
print(Wval(sol,sb))

