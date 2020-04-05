from collections import Counter
import numpy as np
for i in range(int(input())):
    n=int(input())
    mat=[]
    for j in range(n):
        mat.append(list(map(int,input().split())))
    mat=np.array(mat)
    #print(mat)


    # for cols
    cols=0
    for j in range(n):
        #print("array col", mat[:,j])
        a=np.array(mat[:,j])
        #print("a",a)
        cdic=[]
        for k in mat[:,j]:
            if k not in cdic:
                #print(k, "kkkkkkkkk")
                #print("sum", np.sum(a == k))
                if np.sum(a == k) > 1:
                    cols += 1
                    cdic.append(k)
                    break
            #print(cdic)
    # for rows
    rows=0
    for j in range(n):
        #print("array row",mat[j,])
        a=np.array(mat[j,])
        #print("a",a)
        rdic=[]
        for k in mat[j,]:
            if k not in rdic:
                #print(k, "kkkkkkkkk")
                #print("sum", np.sum(a == k))
                if np.sum(a == k) > 1:
                    rows += 1
                    rdic.append(k)
                    break
            #print(rdic)
    arr=np.sum(np.diag(mat))
    print("Case #"+str(i+1)+":",arr,rows,cols)


