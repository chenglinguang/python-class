'''
Created on Apr 12, 2016

@author: echglig
'''

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
        
    def print_score(self):
        print('%s: %s' % (self.name,self.score))

    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
        

bart=Student('Bart Simpson',90)
lisa=Student('Lisa Simpson',70)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_grade())

bart.age=9
print(bart.age)
#print(lisa.age)


#Private variables:
class New_Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
        
        
               
    
new_bart=New_Student('Bart Anderson',98)
new_lisa=New_Student('Lisa Anderson',60)
new_bart.print_score()
new_lisa.print_score()

print(new_bart.get_name())
print(new_bart.get_score())


class Animal():
    def run(self):
        print('Animal is running....')
        
class Dog(Animal):
    def run(self):
        print('Dog is running......')
    def eat(self):
        print('Cat is eating.......')

class Cat(Animal):
    def run(self):
        print('Cat is running......')

dog=Dog()
cat=Cat()
dog.run()
cat.run()

a=list()
b=Animal()
c=Dog()
#usage of isinstance
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))
print(isinstance(b,Dog))

def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(Animal())
run_twice(Dog())

#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
#就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
#由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
#只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
    


























