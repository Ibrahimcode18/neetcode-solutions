class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        
        i = j = 0
        while i < len(nums2) and j < len(nums1):
            if nums2[i] < nums1[j]:
                nums1.insert(j, nums2[i])
                i += 1
            j += 1
        
        nums1.extend(nums2[i:])
    
        

        