def add(a,b):
    print('result:',a+b)
def sub(a,b):
    print('reult:',a-b)
def mul(a,b):
    print('reult:',a*b)
def div(a,b):
    if b!=0:
       print('reult:',a/b)
    else:
        print('error! Divivsion by zero is not allowed.')
while True:
    print('Arthmetic operation is:\n1.add\n2.sub\n3.mul\n4.div')
    ch=int(input('enter ur choice:'))
    if ch==5:
        print('invalid option!')
        break
    a=int(input('enter ur first num:'))
    b=int(input('enter ur second num:'))
    if ch==1:
        add(a,b)
    elif ch==2:
        sub(a,b)
    elif ch==3:
        mul(a,b)
    elif ch==4:
        div(a,b)











