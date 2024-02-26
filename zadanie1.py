f=open('scientist.txt','r',encoding='utf8')
a=f.readlines()
b=[]
c=[]
for i in a:
    i=i.split("#")
    b.append(i)
b1=b.pop(0)
b1='#'.join(b1)
b.sort(key=lambda x: x[2])
print(f'Разработчиками Аллопуринола были такие люди:')
k=0
for i in b:
    if i[1]=='Аллопуринол':
        if k == 0:
            s = i[0]
            k = 1
        print(f'{i[0]} - {i[2]}')
print(f'Оригинальный рецепт принадлежит: {s}')
for i in b:
    k='#'.join(i)
    c.append(k)
c.insert(0, b1)
f2=open('scientist_origin.txt', 'w', newline='', encoding='utf8')
f2.writelines(c)
