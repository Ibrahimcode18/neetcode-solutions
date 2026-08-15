class Solution:
    def merge1(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result


    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

        leftArray = self.mergeSort(left)
        rightArray = self.mergeSort(right)
    
        return self.merge1(leftArray, rightArray)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        
        nums1.extend(nums2)
        nums1[:] = self.mergeSort(nums1)


    
