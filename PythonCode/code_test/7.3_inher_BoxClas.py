class Box1():
    def __init__(self,length1,width1,height1):
        self.length=length1
        self.width=width1
        self.height=height1
    def volume(self):
        return self.length*self.width*self.height

class Box2(Box1):                            #继承Box1定义子类Box2
    def __init__(self,length1,width1,height1):
        super().__init__(length1,width1,height1)
        self.color='black'
        self.material='paper'
        self.type='fish'
    def area(self):
        re=self.height*self.width+self.height*self.length+self.length*self.width
        return re*2
    def volume(self,num=1):
        return self.length*self.width*self.height*num

my_box2=Box2(9,1,1)
print('立方体的体积是%d'%(my_box2.volume()))
print('立方体表面积是%d'%my_box2.area())
print('Box颜色%s,材质%s,类型%s'%(my_box2.color,my_box2.material,my_box2.type))
print('5个立方体体积是%d'%(my_box2.volume(5)))