class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 #small number
        r = len(numbers)-1 #larger numbers

        while l<r:
            sum = numbers[l]+numbers[r] #sum left and right index
            if (sum==target): 
                return [l+1, r+1]
            elif (sum<target): #need higher value, move low index up
                l+=1
            else:    #need less juice, move high index down
                r -= 1
        return [] #return empty list if no answer found
