class Solution(object):
    def sortColors(self, nums):
        i = 0           # next position for 0
        j = len(nums)-1 # next position for 2
        k = 0           # current index

        while k <= j:
            if nums[k] == 0:       # move 0 to front
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:     # move 2 to end
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:                  # 1 is fine
                k += 1

        
