class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        result = []
        
        for start, end in intervals:
            count = sum(1 for p in result if start <= p <= end)
            
            if count >= 2:
                continue
            elif count == 1:
                result.append(end)
            else:
                result.append(end - 1)
                result.append(end)
        
        return len(result)