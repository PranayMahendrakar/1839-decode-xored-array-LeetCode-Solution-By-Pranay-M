class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # XOR property: if a XOR b = c, then a XOR c = b
        # Time: O(n), Space: O(n) for output
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr