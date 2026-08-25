nums = [8,2,3,4,6]
nums_set = set(nums)
k = 2
#fze mmc do dentro da lista 
maior =  k
while maior in nums_set:
    if maior % k == 0:
        maior +=k
        if maior not in nums_set:
            print("ele n está em nums",maior)
            break
