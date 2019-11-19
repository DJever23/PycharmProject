def recursion_power(num,times):
    if times==1:
        return num
    return recursion_power(num,times-1)*num
print(recursion_power(7,10))



i=2
number=7
while i<=10:
    number=number*7
    i+=1
print('7的10次方是%d'%(number))