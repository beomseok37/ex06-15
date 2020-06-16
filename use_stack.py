from Stack import Stack

def isit(a):
    if a=='+' or a=='-' or a=='*' or a=='/' or a=='$':
        return True
    else:
        return False

def priority(a):
    if a=='+' or a=='-':
        return 1
    elif a=='*' or a=='/':
        return 2
    else:
        return 0

def calc(a,b,c):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        return a/b
    
s1=Stack()
s2=Stack()
sen=input("계산식 입력:")
l=sen.split()
l.insert(0,'$')
l.append('$')
s1.push(l[0])
for i in l[1:]:
    if isit(i):
        while not s1.is_empty():
            if priority(s1.top())>=priority(i):
                if s1.top()=='$' and i=='$':
                   break
                num2=s2.pop()
                num1=s2.pop()
                oper=s1.pop()
                num3=calc(num1,num2,oper)
                s2.push(num3)
            else:
                s1.push(i)
                break
    else:
        s2.push(int(i))

print(s2.top())
