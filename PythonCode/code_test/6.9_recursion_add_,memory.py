def recursion_sum(num):
    if num==1:
        return num
    tt=recursion_sum(num-1)+num
    print('第%d次递归'%(num))
    print('返回值%d在内存中的address:%d'%(tt,id(tt)))
    return tt

print(recursion_sum(10))