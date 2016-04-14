'''
Created on Apr 13, 2016

@author: echglig
'''
class StudentA(object):
    pass

s1=StudentA()
s1.name='Michael'
print(s1.name)

def set_age(self,age):  # 定义一个函数作为实例方法
    self.age=age

from types import MethodType
s1.set_age=MethodType(set_age,s1)
s1.set_age(25)
print(s1.age)

s2=StudentA()

#给class绑定方法
def set_score(self,score):
    self.score=score
    
StudentA.set_score=MethodType(set_score,StudentA)
s1.set_score(90)
s2.set_score(100)

print(s2.score)



#__slots__ can't be inherited by its child in case its child has __slots__

class StudentB(object):
    __slots__=('name','age')


s3=StudentB()
s3.name='Michael'
s3.age=18
#s3.score=20 cant 

class GraduateStudentA(StudentB):
    pass

s4=GraduateStudentA()
s4.score='NewMan'

#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class GraduateStudentB(StudentB):
    __slots__=('score')
    
s5=GraduateStudentB()
s5.name='Didi'
s5.age=27
s5.score=90
#s5.hobby='Baskketball'


###############
##Use property

class PStudent(object):
    
    def __init__(self,score):
        self._score=score
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value >100:
            raise ValueError('score must between 0-100!')
        self._score=value
        
sp=PStudent(100)
print(sp._score)
#sp.set_score(9999)



#######
#@property装饰器
class NStudent(object):
    
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        elif value<0 or value>100:
            raise ValueError('score must be in 0~100')
        self.__score=value
        
ss=NStudent()
ss.score=60
print(ss.score)
        
#############################
##@property即getter  @name.setter即是setter
######
class SStudent():
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        self.__birth=value
    @property
    def age(self):
        return 2016-self.__birth
    
    
class Screen():
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width=value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height=value
    @property
    def resolution(self):
        return self.__height*self.__width
    

##################################
####多重继承 inherit more fathers
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('running.....')
        
class Flyable(object):
    def fly(self):
        print('flying......')
        
        
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass


#class Cat(Mammal,Runnable):
###
#defined classes 
###

#__iter__ use class itself in iteration
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration();
        return self.a
    
for n in Fib():
    print(n)


class FibA(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a 
    
f=FibA()
print(f[0])
print(f[1])
print(f[2])
print(f[3])

class StudentD():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
astudent=StudentD('Michael')
print(astudent)


class FibB():
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a 
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b=b,a+b
            return L
                    
ff=FibB()
print(ff[4])

print(ff[:10])
print(ff[1:5])
    
class StudentC():
    def __init__(self):
        self.name='Michael'           
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        
sss=StudentC()
print(sss.name)
print(sss.score)
#print(sss.height)

class StudentE():
    def __init__(self,name):
        self.name=name
    
    def __call__(self):
        print('My name is %s.' % self.name)
        
ssa=StudentE('Lisa')
ssa()

####我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(StudentE('a')))
print(callable(max))








        







