hh=int(input("enter number:"))
def fhh(p):
    if p==0:
        return 0
    elif p==1:
        return 1
    else:
        return fhh(p-1)+fhh(p-2)
for g in range (hh) :
    print(fhh(g))

                