#三酷猫钓鱼记录查找
fish_record='鲫鱼5条，鲤鱼8条，鲢鱼7条，草鱼2条，黑鱼6条，乌龟1只'
print(len(fish_record))
record_len=len(fish_record)
i=0
while i<record_len:    #从字符串最左下标0开始，以5为间隔，循环查找是否有乌龟记录
    if fish_record[i:i+2]=='乌龟':
        if int(fish_record[i+2])%2==0:
            print("乌龟找到了，是%d只,为偶数"%(int(fish_record[i+2])))
        else:
            print("乌龟找到了，是%d只，为奇数"%(int(fish_record[i+2])))
    i+=5
    
   #三酷猫钓鱼记录查找,使用成员运算符改进
if '乌龟' in fish_record:
    print("乌龟在字符串里！")
else:
    print("乌龟没有在字符串里")
