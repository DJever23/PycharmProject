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
for day,day_record in fish_records.items():
    print('%s钓鱼记录为:'%(day))
    for name,sub_record in day_record.items():
        nums+=sub_record[0]
        amounts+=sub_record[0]*sub_record[1]
        print('%s数量%d,单价%.2f元'%(name,sub_record[0],sub_record[1]))
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amounts))
#print(fish_records,d_date1,d_date3)