#print("hello world")
from tkinter.ttk import Separator


a="5"
print(type(a))
a= int(a)#5
b=int(a)#5
print(type(b))
c=a+b #10
print(c)
d=c/2 #5.0
print(d)
e=c//2  #5
print(e)#5
e+=1
print(e)
full_name = "Jagadeesh"+" "+"Sahukari"+" "
print(full_name*3)
'''
id =input("please provide your employee id")
id_char=id.split()
#input().split(" ").sep(";").end('/n')
print(id_char)
Separator= id_char.sep
print(Separator)

user_input =input("please provide your employee id")
items = user_input.split(",")  # Split using comma as separator
print(items)
separator = items.sep  # Now this will print a comma
print(separator)
'''
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)


x=list(map(int, input("Enter multiple values: ").split()))
print("list of employees:",x)

t1=list(map(str,input("Enter the name of teachers: ").split()))
t1.append('seetha')
print("List of teachers",t1)

s1=list(map(float,input("Enter the name of marks: ").split()))
s1.append(10)
print(id(s1))
print("list of student marks",s1)
#s1.remove(10)
print("list of student marks",s1)
print(id(s1))

s2=s1[1:]
print(sorted(s2))
print(s2)
t2=t1[-1:]
print(t2)

