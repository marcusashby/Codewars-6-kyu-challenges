def tribonacci(signature, n):
    if n==0:
        return []
    elif n<3:
        newlist=[]
        for i in range(0,n):
            newlist.append(signature[i])
            return newlist
    else:
        x=3
        while x<n:
            signature.append('')
            x+=1
        for i in range(0,n-3):
            signature[i+3]=signature[i]+signature[i+1]+signature[i+2]
        return signature