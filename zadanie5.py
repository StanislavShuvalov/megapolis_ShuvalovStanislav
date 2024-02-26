import random
c=[]
def hashh(s):
    """
    Эта функция генерирует хэш

    Описание аргументов:
    s - строка, по которой генерируется хэш
    """
    a = random.choices([i for i in range(1024)], k=1024)
    t=0
    for i in s:
        o=ord(i)%1024
        el=a[o]
        t+=el
    has=t%2048
    has=str(has)
    return has
f=open('scientist.txt','r',encoding='utf8')
a=f.readlines()
b=[]
for i in a:
    i=i.split("#")
    b.append(i)
b1=b.pop(0)
b1.insert(0, 'hash')
b1='#'.join(b1)
for i in b:
    i.insert(0, hashh(i[0]))
print(b)
for i in b:
    k='#'.join(i)
    c.append(k)
c.insert(0, b1)
f2=open('scientist_with_hash.csv', 'w', newline='', encoding='utf8')
f2.writelines(c)

