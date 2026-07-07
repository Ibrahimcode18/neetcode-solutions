class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        table_s = {}
        table_t = {}

        for x in s:
            if x not in table_s:
                table_s[x] = 1
            else:
                table_s[x] +=1

        for x in t:
            if x not in table_t:
                table_t[x] = 1
            else:
                table_t[x] +=1
        
        if len(table_s) > len(table_t):
            for y in table_s:
                if not y in table_t:
                    return False
                else:
                    if table_s[y] != table_t[y]:
                        return False
        else:
            for y in table_t:
                if not y in table_s:
                    return False
                else:
                    if table_t[y] != table_s[y]:
                        return False
        return True
        