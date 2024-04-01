class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = ''
        str1_len = len(str1)
        str2_len = len(str2)
        for i, v in enumerate(str1):
            s = str1[:str1_len - i]
            division1 = str1_len / len(s)
            division2 = str2_len / len(s)
            mod1 = str1_len % len(s)
            mod2 = str2_len % len(s)
            if (mod1 == 0 and mod2 == 0):
                s1 = s * int(division1)
                s2 = s * int(division2)
                if s1 == str1 and s2 == str2:
                    return s
        return ""
