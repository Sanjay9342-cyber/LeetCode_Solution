class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        cnt = Counter(nums1)
        result = []
        for num in nums2:
            if cnt[num]>0:
                result.append(num)
                cnt[num]-=1
        return result