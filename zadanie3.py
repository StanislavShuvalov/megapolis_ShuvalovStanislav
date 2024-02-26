f=open('scientist.txt','r',encoding='utf8')
a=f.readlines()
b=[]
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
    return a
b=fast(b)
def bin_search(a, target):
    """
    Эта функция делает двоичный поиск по дате

    Описание аргументов:
    a - входной список, в котором проводится поиск
    target - элемент, который нужно найти
    """
    low = 0
    high = len(a)-1
    while low<=high:
        mid = (low + high) // 2
        if a[mid][2]==target:
            return mid
        elif a[mid][2]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(b)
while True:
    s=input()
    if s=='эксперимент':
        break
    s1=s[0:2]
    s2=s[3:5]
    s3=s[6:]
    s=s3+'-'+s2+'-'+s1
    t=bin_search(b, s)
    y=''
    k=0
    if t!=-1:
        print(f'Ученый {b[t][0].split()[0]} {b[t][0].split()[1][0]}.{b[t][0].split()[2][0]}. создал {b[t][3]} - {b[t][2]}')
    else:
        print('В этот день ученые отдыхали')
