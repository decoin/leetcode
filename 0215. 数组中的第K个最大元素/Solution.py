class Solution:
    def partition(self, nums, l, r):
        k = random.randint(l, r)
        pivot = nums[k]
        nums[l], nums[k] = nums[k], nums[l]
        index = l
        for i in range(l + 1, r + 1):
            if nums[i] > pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[l], nums[index] = nums[index], nums[l]
        return index

    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r, k = 0, len(nums) - 1, k - 1
        while 1:
            p = self.partition(nums, l, r)
            if p == k:
                return nums[p]
            elif p > k:
                r = p - 1
            else:
                l = p + 1
