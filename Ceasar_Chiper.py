#Ceaser Chiper
def enc(a,k):
    a=list(a)
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0,len(a)):
        if a[i] in alp:
            c=alp.index(a[i])+1
            if c+k<27:
                a[i]=alp[c+k-1]
            else:
                k1=c+k
                while k1>26:
                    k1-=26
                a[i]=alp[k1-1]
        elif a[i] in Alp:
            c=Alp.index(a[i])+1
            if c+k<27:
                a[i]=Alp[c+k-1]
            else:
                k1=c+k
                while k1>26:
                    k1-=26
                a[i]=Alp[k1-1]
    return ''.join(a)
def dec(a,k):
    a=list(a)
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0,len(a)):
        if a[i] in alp:
            c=alp.index(a[i])+1
            if c-k>0:
                a[i]=alp[c-k-1]
            else:
                k1=c-k
                while k1<1:
                    k1+=26
                a[i]=alp[k1-1]
        elif a[i] in Alp:
            c=Alp.index(a[i])+1
            if c-k>0:
                a[i]=Alp[c-k-1]
            else:
                k1=c-k
                while k1<1:
                    k1+=26
                a[i]=Alp[k1-1]
    return ''.join(a)
print('Do you want encoder or decoder(E/D)?')
y=input()
a=input('The text is: ')
k=int(input())
if y=='E':
    print(enc(a,k))
elif y=='D':
    print(dec(a,k))
else:
    print('Wrong order!!!')