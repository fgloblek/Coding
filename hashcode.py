def g(L):
    k=0
    F="-%s %s %s"%L,
    print(F)
    print([X for X in F])
    print([X.split() for X in F])
    while all( sum(map(int,X.split())) for X in F ):
        k+=1
        F=[x[:y/10+1]+str(y%10)+x[y/10+1:] for x in F for y in range(10*len(x))]
    return k

tests=[
([1,1,3],2),
([3,1,1],2),
([14159265,12345678,98712369],3)
]

for inval,outval in tests:
    actval=g((inval[2], inval[0], inval[1]))
    print('--\nInput=%s;\nExpected=%s;\nActual=%s;\nMatch=%s'%(inval,outval,actval,outval==actval)) 