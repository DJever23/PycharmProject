from BoxClass1 import *

big_gift_box=FishBox(60,30,40)
big_gift_box.price=1000
big_gift_box.amount=20
big_gift_box.weight=10
print('大礼的体积是%d立方厘米'%(big_gift_box.volume()))
print('大礼的表面积是%d平方厘米'%(big_gift_box.area()))
index=big_gift_box.type.index('大礼')
g_box_num=big_gift_box.countBoxNums(200,index)
print('200条鱼需要%d只大礼'%(g_box_num))
print('200条鱼装大礼的价值为%d元'%(g_box_num*big_gift_box.price))

small_gift_box=FishBox(50,20,30)
small_gift_box.price=500
small_gift_box.amount=10
small_gift_box.weight=5
print('小礼的体积是%d立方厘米'%(small_gift_box.volume()))
print('大礼的表面积是%d平方厘米'%(small_gift_box.area()))
index=small_gift_box.type.index('小礼')
g_box_num=small_gift_box.countBoxNums(200,index)
print('200条鱼需要%d只小礼'%(g_box_num))
print('200条鱼装小礼的价值为%d元'%(g_box_num*small_gift_box.price))

print(issubclass(Box2,Box1))
