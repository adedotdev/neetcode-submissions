class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_dict = {char: i for i, char in enumerate(s)}
        sizes = []
        
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_dict[char])
            
            if i == end:
                sizes.append(end - start + 1)
                start = i + 1
            
        return sizes