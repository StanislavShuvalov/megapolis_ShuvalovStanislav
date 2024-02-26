import string
import random
c=[]
def password():
    """
    Эта функция создает пароль для пользователя
    """
    pas=''.join(random.choices(string.digits+string.ascii_letters, k=8))
    return pas
def login(name):
    """
    Эта функция создаёт пароль для пользователя

    Описание аргументов:
    name - ФИО пользователя, на основании которого создается логин
    """
    logg=name.split()[0]+'_'+name.split()[1][0]+name.split()[2][0]
    return logg
f=open('scientist.txt','r',encoding='utf8')
a=f.readlines()
b=[]
for i in a:
    i=i.split("#")
    i[3]=i[3][:(-1)]
    b.append(i)
b1=b.pop(0)
b1.append('login')
b1.append('password')
b1='#'.join(b1)
for i in b:
    i.append(login(i[0]))
    i.append(password()+'\n')
for i in b:
    k='#'.join(i)
    c.append(k)
c.insert(0, b1+'\n')
f2=open('scientist_password.csv', 'w', newline='', encoding='utf8')
f2.writelines(c)