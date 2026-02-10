# Two sum promble

def towSum(nums:list , target:int) -> list:
    # brutefore aproch
    n = len(nums)

    # for i in range(n): 
    #     for j in range(i , n-1):
    #         if nums[i] + nums[j] == target:
    #             return [i , j]
            
    # return None
    l , r = 0 , n-1
    while l< r:
        if nums[l] + nums[r] < target:
            l+=1
        elif nums[l] + nums[r] > target:
            r-=1
        elif nums[l] + nums[r] == target:
            return [l , r]
        else:None




if __name__ == "__main__":

#  input for two sum
# Input
    nums = [2, 7, 11, 15]
    target = 17
    print(towSum(nums , target))