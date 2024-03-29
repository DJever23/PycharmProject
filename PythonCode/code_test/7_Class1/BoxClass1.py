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

class FishBox(Box2):
    def __init__(self,length1,width1,height1):
        super().__init__(length1,width1,height1)
        self.price=0
        self.amount=0
        self.type=('大礼','小礼')
        self.weight=0
    def countBoxNums(self,fish_nums,f_type_index):
        if f_type_index==0:
            self.amount=20
        else:
            self.amount=10
        if fish_nums%self.amount==0:
            return fish_nums/self.amount
        else:
            return fish_nums/self.amount+1
    def total(self,box_nums,price):
        return box_nums*price