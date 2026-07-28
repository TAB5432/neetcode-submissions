class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows-1):
            tmpRow = [0] + res[-1] + [0]
            resRow = []
            
            for j in range(len(res[-1]) + 1):
                resRow.append(tmpRow[j] + tmpRow[j+1])
            res.append(resRow)
        
        return res