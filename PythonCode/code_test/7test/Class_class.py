class Class1():
    def __init__(self,students1,teachers1):
        self.student=students1
        self.teacher=teachers1
    def count(self,people):
        return len(people)
stu1=['张','李','高','刘','刘星','王','任','张静','赵','丁','乔','李四','林','王五','毛']
tea1=['高老师','丁老师','刘老师']
class1=Class1(stu1,tea1)

class subClass(Class1):
    def __init__(self,students1,teachers1):
        super().__init__(students1,teachers1)
        self.class_name=''
        self.class_address=''
    def addTeacher(self,teachername,subject):
        self.teacher[teachername]=subject    #增加字典中的键值对
    def reduceStudent(self,tName):
        self.student.remove(tName)    #列表操作，删除列表中指定元素

tea2={'高老师':'语文','丁老师':'英语','刘老师':'数学'}    #字典
class2=subClass(stu1,tea2)
class2.addTeacher('李老师','计算机')
class2.reduceStudent('王五')
class2.reduceStudent('毛')
print(class2.student)
print(class2.teacher)
print('学生有%d人，老师有%d人'%(class2.count(class2.student),class2.count(class2.teacher)))