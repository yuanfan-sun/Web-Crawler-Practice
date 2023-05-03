"""
x = 1, 3, 5, 7                      #Python中的封装，注意，这里把等号后边的int数据类型封装成元组了
print(x)

a, b = [100, 200]                   #线性结构，可以同时为多个变量赋值
a, b = b, a                         #可以很轻松的实现数据交换
print(a, b)

m,n = {"name":"jason","age":18}     #非线性结构也可以解构,即2边的个数要相同，m和n这2个变量分别赋值
print(m,n)

y, *z=100,200,300,400,500,600       #注意，y为变量标识符，而z则为可变参数（可变参数只能存在一个，存在2个会报语法错误），他会把后面的元素放入到一个列表中
print(y,z)

head,*mid,tail=range(10)            #注意，这也是结构，左边的标识符要大于或等于2个才能算得上结构哟~
print(head,mid,tail)

x,[a,b],z = (1,[2,3],(4,5))         #当然，咱们也可以这样去解构，它会按照我们的想法对号入座
print(x,a,b,z)
"""
''' 
#set()-->new empty set object
#set(iterable)-->new set object

s1=set()
s2=set(range(10))
s3=set(list(range(20)))

#dict
s4=()

#set
s5={1,3,5,7,9}
s6={(1,3),5,'A'}

#集合只能存放不可变的的元素，如果存放list和bytearray时会报错:"unhashable type"
s7={(2,),3,None,"abc",b"abc"}

s8 = set(enumerate(range(5)))

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)

set的元素要求必须可以hash
不可hash的类型有list、set，bytearray,dict
元素不可以索引
set可以迭代
'''

'''
add(elem)
    增加一个元素到set中
    如果元素存在，什么都不做
'''
'''
s1 = {1,3,5}
print(s1)

s1.add(100)
print(s1)
'''

'''
update(*others)
    合并其他元素到set集合中来
    参数others必须是可迭代对象
    就地修改
'''

'''s1 = {1,3,5}
print(s1,id(s1))

s1.update([1,3,2],[2,3,4],(6,8))
print(s1,id(s1))'''

i=0
while i<10:
    i += 1
    print(i)
