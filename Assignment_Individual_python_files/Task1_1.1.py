
def meth(variable1,variable2):
    return variable1*variable2

def myreduce(meth,mylist):
    s = mylist[0]
    for i in mylist[1:]:
        s =  meth(s,i)
    
    return s


result = myreduce(meth,[4,7,9,10])

print(result)



