"""
比较最大值和最小值 
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str: 
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s1[:i]
        return s1 
    
# 测试
s = Solution()
s.longestCommonPrefix(['flower', 'flight','pig']) 