class Student:  #类名一般首字母大写，多个单词采用驼峰原则

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def say_score(self):
        print('{0}的分数是：{1}'.format(self.name,self.score))

    def say_age(self):
        print('{0}的年龄是：{1}'.format(self.name,self.age))
s1 = Student('徐超超',28,88)
s1.say_score()
s1.say_age()

s1.salary = 15000
print(s1.salary)
s2 = Student('supassxu',18,88)
s2.say_score()
s2.say_age()
print(dir(s2))
print(s2.__dict__)

s3 = Student
s4 = s3('xuzhenzhen',27,100)
print(id(s2))
print(id(s3))
print(id(s4))
s4.say_score()