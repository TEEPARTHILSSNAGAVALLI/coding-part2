class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        if len(d) == 0:
            return [1]
        if d[-1] != 9:
            d[-1] += 1
            return d
        else:
            d = self.plusOne(d[:-1])
            d.append(0)
            return d
