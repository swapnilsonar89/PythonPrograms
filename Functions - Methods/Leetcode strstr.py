def strStr(haystack, needle):
        n = len(needle)
        h = len(haystack)
        i = 0
        flag = 0
        if len(haystack) == 0:
            return 0
        elif needle in haystack:
            for i in range(h):
                if haystack[i:i+n] == needle:
                    return i
                        
         else:
           return -1
