f=open('scientist.txt','r',encoding='utf8')
a=f.readlines()
b=[]
c=[]
for i in a:
    i=i.split("#")
    b.append(i)
b1=b.pop(0)
def fast(a):
    """
    Эта функция делает быструю сортировку по дате

    Описание аргументов:
    a - входной список, который нужно отсортировать
    """
    for i in range(1, len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j][2]>temp[2]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
    b=a
    return b
b=fast(b)
for i in range(5):
    print(f'{b[i][0]}: {b[i][1]}')