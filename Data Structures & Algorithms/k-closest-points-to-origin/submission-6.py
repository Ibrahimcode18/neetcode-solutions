class Solution:
    def merge(self, left, right):
        results = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                results.append(left[i])
                i += 1
            else:
                results.append(right[j])
                j += 1
        
        results.extend(left[i:])
        results.extend(right[j:])

        return results

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        leftArray = self.mergeSort(left)
        rightArray = self.mergeSort(right)

        return self.merge(leftArray, rightArray)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        i = 0
        answer = []

        for x in points:
            calSum = (x[0]) ** 2 + (x[1]) ** 2
            distance = round(math.sqrt(calSum), 5)
            distances.append([distance, i])
            i += 1
        
        results = self.mergeSort(distances)

        for i in range(k):
            index = results[i][1]
            answer.append(points[index])
        
        return answer