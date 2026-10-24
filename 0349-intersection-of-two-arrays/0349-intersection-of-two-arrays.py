class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mp={}
        for num in nums1:
            mp[num]=mp.get(num,0)+1
        result=[]
        for num in nums2:
            if num in mp:
                result.append(num)
                del mp[num]
        return result