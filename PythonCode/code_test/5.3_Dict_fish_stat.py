#-----------------------------钓鱼原始记录
d_date1={'鲫鱼':[18,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}
d_date2={'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}
d_date3={'乌龟':[1,71],'鲫鱼':[1,9.8],'草鱼':[5,7.2],'黄鱼':[2,40]}
fish_records={'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}
#-----------------------------修改错误记录
d_date1['鲫鱼']=[17,10.5]
del(d_date3['黄鱼'])
for get_name,get_L in d_date3.items():
    get_L[1]=get_L[1]*1.1
    d_date3[get_name]=get_L
#------------------------------打印修改后的结果
nums=0
amounts=0
day=''
day_records={}
stat_records={} #统计记录变量初始化定义
name_n=''       #最大数量鱼的名称
max_nums=0
name_a=''       #最大金额鱼的名称
max_amount=0
print('----------每日钓鱼记录-----------')

for day,day_record in fish_records.items():
    print('%s钓鱼记录为:'%(day))
    for name,sub_record in day_record.items():
        nums+=sub_record[0]
        amounts+=sub_record[0]*sub_record[1]
        print('%s数量%d,单价%.2f元'%(name,sub_record[0],sub_record[1]))

        if name in stat_records:                           #判断鱼是否在stat字典里，若存在，则作累计
            stat_records[name][0]+=sub_record[0]
            stat_records[name][1]+=sub_record[0]*sub_record[1]
        else:
            stat_records[name]=[sub_record[0],sub_record[0]*sub_record[1]] #第一次累计，直接在字典里赋值
print('----按鱼进行数量，金额统计----')
for name1,get_L in stat_records.items():
    print('%s的总数量%d,金额为%.2f元'%(name1,get_L[0],get_L[1]))
    gets_num_d={name1:get_L[0]}              #取鱼对应的数量
    if get_L[0]>max_nums:
        name_n=name1
        max_nums=get_L[0]
    gets_amount_d={name1:get_L[1]}
    if get_L[1]>max_amount:
        name_a=name1
        max_amount=get_L[1]
#---------------------------------------统计结果打印
print('----最大值，总数量，总金额统计----')
print('最大数量的鱼是%s,%d条'%(name_n,max_nums))
print('最大金额的鱼是%s,%.2f元'%(name_a,max_amount))
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amounts))
