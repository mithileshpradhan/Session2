def meth(varialble1):
    if varialble1 > 4:
        return True

    else:
        return False


def myfilter(meth,seq):
        for i in seq:

            if meth(i):
                print(i)


myfilter(meth,[1,2,3,4,5,6,7])

