class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # initialize output array
        pref = 1           # prefix product
        post = 1           # suffix product

        # forward pass to get prefix products of all i-1 #s
        for i in range(n):
            answer[i] = pref
            pref *= nums[i]

        # backward pass (suffix products multiplied by all
        # of the prefix   products found in loop #1
        for i in range(n-1, -1, -1):
            answer[i] *= post
            post *= nums[i]

        return answer

