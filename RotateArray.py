class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k %= n

        def reverse(l: int, r:int) -> None:
            while l < r:
                l, r = r, l
                nums[l], nums[r] = nums[r], nums[l]

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)