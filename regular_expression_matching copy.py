class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i=j=0
        sLen=len(s)
        pLen=len(p)
        skip=0

        while i<sLen and j<pLen:
            if p[j]=='.':
                if j+1 == pLen-1 and p[j+1]=='*':
                    return True
                if j+1 <pLen and p[j+1]=='*':
                    while i<sLen and s[i]!=s[j]:
                        i+=1
                    j+=2
                else:
                    i+=1
                    j+=1

            elif p[j]=='*':
                prev=p[j-1]
                while i<sLen and s[i]==prev:
                    i+=1
                j+=1
                
            else:
                if j+1<pLen and p[j+1]=='*':
                    j+=1
                    skip+=1
                    continue
                if s[i]!=p[j]:
                    if p[j-1]=='*'and prev==s[i] and skip>0:
                        i+=1
                        j+=1
                        continue
                    else:
                        return False
                i+=1
                j+=1
        if i==sLen and j==pLen:
            return True
        return False
c=Solution()
print(c.isMatch("aaa","a*a"))

        