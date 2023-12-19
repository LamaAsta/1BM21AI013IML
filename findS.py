import numpy as np
data = [['m','s','w','y','m','s','y'],
        ['e','r','c','n','m','n','n'],
        ['m','s','m','y','n','n','y'],
        ['e','s','c','y','h','s','y']]

av = [['m','e'],['s','r'],['w','c','m','c'],['y','n'],['m','n'],['s','n'],['y','n']]

df = np.array(data)
attr = df[:,:-1]
labels = df[:,-1]
hypo = [None for i in attr.shape[1]]#list(np.array(attr.shape[1]))
print(attr)
print(labels)
for i in range(df.shape[0]):
    if(labels[i] == 'n'):
        continue
    if hypo[0] == None:
        hypo = attr[i]
     