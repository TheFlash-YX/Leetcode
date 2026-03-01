from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=collections.defaultdict(list)
        for str in strs:
            key="".join(sorted(str))
            map[key].append(str)

        return list(map.values())
