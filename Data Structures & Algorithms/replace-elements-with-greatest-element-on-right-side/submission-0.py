class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        great_so_far = -1
        result = []
        for i,a in enumerate(arr[::-1]):
            
            result.append(great_so_far)

            if a > great_so_far:
                great_so_far = a
            
        return result[::-1]

        