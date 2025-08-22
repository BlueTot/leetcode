from collections import Counter

class Solution:

    def __merge(self, array, left, mid, right):
        output = []
        i = left
        j = mid+1
        while (i <= mid and j <= right):
            if (array[i][0] < array[j][0]):
                output.append(array[i])
                i+=1
            else:
                output.append(array[j])
                j+=1
        while (i <= mid):
            output.append(array[i])
            i+=1
        while (j <= right):
            output.append(array[j])
            j+=1
        for index in range(len(output)):
           array[left+index] = output[index]
        return array
    
    def __mergeSort(self, array, left, right):
        print(left, right)
        if left < right:
            mid = (left+right)//2
            array = self.__mergeSort(array, left, mid)
            array = self.__mergeSort(array, mid+1, right)
            array = self.__merge(array, left, mid, right)
        return array

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [(k,v) for k, v in Counter(nums).items()]
        counter = self.__mergeSort(counter, 0, len(counter)-1)
        i = 0
        for k,v in counter:
            for _ in range(v):
                nums[i] = k
                i+=1
