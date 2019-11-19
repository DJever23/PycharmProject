def r_dichotomy(nums,find,left,right):
    middle=(left+right)//2
    if nums[middle]==find:
        return middle
    if right==left+1:
        if nums[middle]!=find:
            return -1
    if nums[middle]>find:
        return r_dichotomy(nums,find,left,middle)
    elif nums[middle]<find:
        return r_dichotomy(nums,find,middle+1,right)
nums_L=[1,2,3,4,8,16,20,30]
print(r_dichotomy(nums_L,2,0,len(nums_L)))