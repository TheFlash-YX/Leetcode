from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=map(int,version1.split('.'))
        ver2=map(int,version2.split('.'))

        for v1,v2 in zip_longest(ver1,ver2,fillvalue=0):
            if v1<v2:
                return -1
            elif v1>v2:
                return 1

        return 0