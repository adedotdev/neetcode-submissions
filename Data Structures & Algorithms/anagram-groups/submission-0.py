class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                count[idx] += 1
            map[tuple(count)].append(word)

        return list(map.values())