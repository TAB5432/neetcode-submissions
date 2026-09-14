class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = arr
        for index, element in enumerate(arr):
            if index == len(arr)-1:
                res[index] = -1
                break
            res[index] = max(arr[index+1:len(arr)])
            
        return res