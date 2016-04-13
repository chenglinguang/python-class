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


class Cat(Mammal,Runnable):
