def ldambda(x):
    y=''
    for i in range(8):
        y.join(str((x>>i)&1))
    reversed(y)
    return y
        
print(ldambda(100))