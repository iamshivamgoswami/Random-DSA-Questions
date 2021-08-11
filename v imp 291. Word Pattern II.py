import collections


class Solution:
    def wordPatternMatch(self, pattern, str):
        def func(pattern,str,i=0,j=0,ptable={},stable={}):
            if i==len(pattern) and j==len(str):
                return True

            elif i==len(pattern) or j==len(str):
                return False

            else:
                p = pattern[i]
                added = False
                for k in range(j,len(str)):
                    word=str[j:k+1]

                    if p in ptable and ptable[p]!=word or word in stable and stable[word]!=p:
                        continue
                    if p not in ptable and word not in stable:
                        ptable[p]=word
                        stable[word]=p
                        added=True

                    ret=func(pattern,str,i+1,k+1,ptable,stable)

                    if added:
                        del ptable[p]
                        del stable[word]
                        added=False
                    if ret:
                        return True

            return False
        return func(pattern,str)