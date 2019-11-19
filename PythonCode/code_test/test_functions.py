def find_factor(nums):
    '''
    find_factor is a custom function.
    :param nums:is a parameter to convey positive integer
    :return: return all factors of a positive integer in the from of string
    '''
    if type(nums)!=int:
        print('input type is wrong,it must be integer!')
        return
    if nums<=0:
        print('input out of range,it must be positive integer!')
        return
    i=1
    str1=''
    while i<=nums:
        if nums%i==0:
            str1=str1+' '+str(i)
        i+=1
    return str1             #返回因数字符串

def say_ok():
    print('OK')