class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sort = sorted(s)
            sorted_string = "".join(sort)
            groups[sorted_string].append(s)
        return list(groups.values())