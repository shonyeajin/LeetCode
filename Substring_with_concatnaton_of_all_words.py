import copy

# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         if s=="" or len(words)==0:
#             return []
#         element_length=len(words[0])
#         s_length=len(s)

#         ret=[]
#         i=0
#         while i <s_length:
#             word_list=copy.copy(words)
#             j=i
#             while s[j:j+element_length] in word_list:
#                 word_list.remove(s[j:j+element_length])
#                 j+=element_length
#             if word_list==[]:
#                 ret.append(i)
#             i+=1
#         return ret
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s=="" or len(words)==0:
            return []
        element_length=len(words[0])
        s_length=len(s)
        ret=[]
        i=0
        hash=dict()
        for i in range(len(words)):
            if words[i] in hash:
                hash[words[i]]+=1
            else:
                hash[words[i]]=1
        i=0
        while i <s_length:
            temp=hash.copy()
            j=i
            while s[j:j+element_length] in temp:
                tempstr=s[j:j+element_length]
                if temp[tempstr]==1:
                    temp.pop(tempstr)
                else:
                    temp[tempstr]-=1
                j+=element_length
            if len(temp)==0:
                ret.append(i)
            i+=1
        return ret

c=Solution()
print(c.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]))
                
            
        