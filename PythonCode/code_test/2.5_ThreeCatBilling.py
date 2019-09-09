num1,num2,num3=8,7,12                       #鱼的数量
price1,price2,price3=8.1,8.2,8              #鱼的单价
fish1,fish2,fish3='鲫鱼','鲤鱼','草鱼'      #鱼的种类
date='2018年5月'
Total_number=num1+num2+num3                 #鱼的总数
Total_Amount=num1*price1+num2*price2+num3*price3    #总金额
print("-----"*4+"三酷猫记账单"+"-----"*4)
print('钓鱼地点   '+'钓鱼日期   '+'  鱼名  '+'数量（条）'+'单价（元）')
print('左小河   '+date+'1日 '+'  '+fish1+'  '+'  '+str(num1)+'     '+'    '+str(price1))
print('右小河   '+date+'2日 '+'  '+fish2+'  '+'  '+str(num2)+'     '+'    '+str(price2))
print('长江     '+date+'3日 '+'  '+fish3+'  '+'  '+str(num3)+'     '+'    '+str(price3))
print("----"*12+'----')
print('鱼数总%d条，市场价格总%.2f元，每天平均钓鱼数量约%d条（%f条)，鱼的平均价格为%f元(%.2f元，%d元))'
      %(Total_number,Total_Amount,int(Total_number/3),Total_number/3,Total_Amount/Total_number,Total_Amount/Total_number,Total_Amount/Total_number))
print('    '*8+'记账日期:'+date+'4日')
print('    '*8+'记账人：'+'  '+'dengjie')
