import copy
#继承

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_name(self):
        print('I hive know idea about my name!:{0}'.format(self.name))

    def say_age(self):
        print('How old are you!:{0}'.format(self.age))

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  #必须显示调用父类构造方法，不然不会被调用
        self.score = score
    def say_score(self):
        print('what is my score!:{0}'.format(self.score))

    def say_name(self):
        print('my name is {0}, hello world!'.format(self.name))

#print(Student.mro())
c1 = Person('supassxu',18)
d1 = Person('supassxu',18)
s1 = Student('supassxu',c1,d1)
#s1.say_age()
#s1.say_name()
#s1.say_score()

#浅复制
s2 = copy.copy(s1)
print(s1,s1.name,s1.age)
print(s2,s2.name,s2.age)

#深复制
s3 = copy.deepcopy(s1)
print(s1,s1.name,s1.age)
print(s3,s3.name,s3.age)