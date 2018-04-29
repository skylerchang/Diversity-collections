print("************variable **************")
print(1)
apple = 10
print(apple)
apple_egg=10+2
print(apple_egg)
a,b,c=1,2,3
print(a,b,c)
a=1
b=a*2
print(a,b)
print("************while*****************")
condition=1
while condition < 10:
    print(condition)
    condition = condition+1
    if condition == 10:
        print("I'm False")
print("************FOR*****************")
example_list = [1,2,4,252,432,34,56,77,3,1]
for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')

for i in range(1,10):
    print(i)
print("RANGE IS 1 FROM 9")
for i in range(1,10,2):
    print(i)
print("************IF*****************")
x=-2
y=2
z=3
d=2
if x<y:
    print('x is less than y')
    if x<=1:
        print("x is 1")
if x<y>z:
    print("result")
if x<y<z:
    print("result2")
if d<=y:
    print("result3")
if d==y:
    print("result4")
if x>1:
    print("x is larger than 1")
elif x<-1:
    print("x < -1")
elif x<1:
    pritn("x < 1")
else:
    print("x is 1")
print("finish running, although x <1 ,only care about 1 round result than jump out")   
print("************DEF*****************")
def function():
    print("This is a function")
    a=1+2
    print(a)
########in the front you should input function(), then it is the real application this "define function"######
def fun(a,b):
    c=a*b
    print("the c is",c)
#######in the front, fun(a=2,b=5) and fun(2,5) are both ok########
print("************PARAMETERS*****************")
def sale_car(price,color,brand,is_second_hand):
    print('price:',price,
          'color:',color,
          'brand:',brand,
          'is_second_hand:',is_second_hand)
sale_car(1000,'red','carmy',True)
def sale_car2(price,color='blue',brand='carmy',is_second_hand='TRUE'):
    print('price:',price,
          'color:',color,
          'brand:',brand,
          'is_second_hand:',is_second_hand)
sale_car2(1222,color='green')
sale_car2(1233,brand="BMW")
print("************global&local*****************")
def fun():
    a=10
    print(a)
    return a+10
print(fun())
APPLE=100    ######global#####
def fun():
    a=10
    return a+100
print(a)    #####because it's local, so can't print####
print(APPLE)
APPLE=100    
def fun():
    a=APPLE
    return a+100
print(fun())
a=None
def fun():
    global a
    a=20
    return a+100
print(APPLE)
print('a past is',a)
print(fun())
print('a now is',a)
print("************READ&WRITE*****************")
text='This is my first test.\nThis is second line.\nThis is the last line.'
my_file = open('my file.txt','w')
my_file.write(text)
my_file.close()
append_text='\nThis is appended file.'
my_file = open('my file.txt','a')
my_file.write(append_text)
my_file.close()
file = open('my file.txt','r')
content1 = file.read()        ###print all content###
#####content2 = file.readline()  ###print the first line,acturally save in a list,the first element in this list###
#####content3 = file.readline()  ###the second element###
#####content4 = file.readlines()   ###print the whole list###
print(content1)
######print(content2)
#####print(content3)
#####print(content4)    ######my computer only works on file.read()####
print("************CLASS*****************")
class Calculator:
    name='Good calculator'
    price=18
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        result=x*y
        print(result)
    def devide(self,x,y):
        result=x/y
        print(result)
#calcul=Calculator()
#calcul.name
#calcul.price
#calcul.add(10,11)    in the front
#calcul.devide(10,2)
    def __init__(self,name,price,height,width,weight):
        self.name=name
        self.price=price
        self.h=height
        self.wi=width
        self.we=weight
        self.add(1,2)
#c=Calculator('Bad_calculator',12,23,45,23)  in the front
#c.name
#c.h
#or def __init__(self,name,price,height=18,width=29,weight=10): give a parameter in advance
print("************INPUT*****************")
a_input=int(input("Please give a number:"))  #####gurantee it is a integrate
print("This input is",a_input)
if a_input<100:
    print('THIS IS LESS THAN 100')
elif a_input>100:
    print("THIS IS GREAT")
else:
    print("GOOD 100")
print("************TUPLE&LIST*****************")
a_tuple=(12,3,4,5,6,88)
another_tuple=2,4,6,78,5
a_list=[12,3,4,5,67]
for content in a_tuple:
    print(content)
for content in a_list:
    print(content)
for index in range(len(a_list)):
    print('index=',index,'number in list=',a_list[index])
print("************LIST*****************")
a=[1,2,45,52,526,6,2,11]
a.append(88)
print(a)   ####append 88 in the end
a.insert(1,0)  ####append 0 in 1 position,list starts from 0
a.insert(0,999)
a.remove(2) ####only remove the first 2
print(a[0]) ###print the first element
print(a[-1]) ####print the last elemet
print(a[0:3]) ####print the first 3 elements
print(a[5:]) ###print 5 to the end
print(a[-3:]) ####print the last
a.index(2)   ####the first time appear 2 and show its index, index starts from 0
print(a.index(2))
a.count(2)  ####print how many times when 2 appear
a.sort()###from small to big
print(a)
a.sort(reverse=True)  ##### from big to small
print(a)
print("************multi-list*****************")
a=[1,2,3,4]
multi_dim_a=[ [1,2,3],
              [2,3,4],
              [3,4,5]]
print(a[1])      #####show 2
print(multi_dim_a[0][1])   ####show 2
print("************DICTIONARY*****************")
a_list = [1,2,3,4,5,6,7]
d={'apple':1,'pear':2,'orange':3}
d2={1:'a','c':'b'}
print(d['apple'])
print(a_list[0])
del d['pear']
d['b']=20
print(d)
d={'apple':[1,2,3],'pear':{1:3,3:'a'},'orange':2}      ####dictionary can include another dictionary and function etc
print(d['pear'][3])
print("************IMPORT MODULE****************")
import time                    #######use time module name and everytime use time
print(time.localtime())
import time as t              #######change module name as t
print(t.localtime())
from time import localtime    ######only import localtime function
print(localtime())
from time import *     #####import all functions
print(localtime())
print("************create own MODULE****************")
#######create a new python script, called module.py#######
###### in module.py#######
####  def printdata(data):   ######
#####  print("I am module")   ######
#####     print(data)        #######
##### in the same root, in another python script######
##### import module  #####
####   module.printdata("I'M DATA") ######
###### put my own module in the address /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages instead the same root limitation ### 
print("************continue and break in loop****************")
a=True
while a:
    b=input('type something:')
    if b=='1':
        a=False     #### if b is 1, jump out this loop, and still print "still in while" and "finish run" because this loop was decided by a not b
    else:
        pass    #### pass means jump out and do nothing
    print('still in run')  
print('finish run')
###### beak 
while True:
    b=input('type something')
    if b=='1':
        break        #### if b is 1, jump out the loop and didn't run "still in run" and print "finish run"
    else:
        pass
    print('still in run')
print('finish run')
###### continue 
#while True:
#    b=input('type something')
#    if b=='1':
#        continue      #### if b is 1, will jump out all the rest keep loop again, print type something again
#    else:             #### if b is 2, print still in run
#        pass
#    print('still in run')
#print('finish run')
print("************error solution TRY****************")
try:
    file=open('eeee','r')
except Exception as e:
    print(e)
##### upgrade #####
try:
    file=open('eeee','r+')
except Exception as e:
    print("There is no file named as this")
    response = input("Do you want to create a new file?")
    if response == 'y':
        file = open('eeee','w')
    else:
        pass
else:      #####try's exception's else####
    file.write('write something in the file:ssss')   ####run it again and will write in 
file.close()    #####acturally a tab should in front of file.close()
print("************zip lambda map****************")
a=[1,2,3]
b=[4,5,6]
zip(a,b)    #### print an object
list(zip(a,b))   ####show [(1,4),(2,5),(3,6)]
for i,j in zip(a,b):
    print(i/2,j*2)
list(zip(a,a,b))
#####original method#####
def fun1(x,y):
    return(x+y)
fun1(2,3)
#############lambda#######
fun2=lambda x,y:x+y
fun2(2,3)
########map:use the function and the input to do the calculation together  #######
map(fun1,[1],[2])    #### print an object
list(map(fun1,[1],[2]))   ### print 1+2 as [3]
list(map(fun1,[1,3],[2,5]))   ##### print [3,8] means 1+2 and 3+5
print("************set ****************")
char_list=['a','b','c','c','d','d','d']
print(set(char_list))   ####print uniqe results
print(type(set(char_list)))  ###show it is a set
sentence="Welcome Back to This Tutorial"
print(set(sentence))
unique_char=set(char_list)
unique_char.add('x')   #### add x
unique_char.remove('x')   ### delete x
set1 = unique_char
set2 = {'a','e','i'}
print(set1.difference(set2))  ###find difference
print(set1.intersection(set2)) ###find identity
unique_char.clear()    ###clear everything

