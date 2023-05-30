"""
利用str.replace() 
"""
class Solution:
    def isValid(self, s) ->bool: 
        # 判断输入的括号里是否存在成对括号
        # 若存在，则用空格替代
        # 最后判断输入的括号是否为空
        while '{}' in s or '()' in s or '[]' in s: 
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == '' 
    
# 测试  
st = Solution() 
st.isValid('{[()]}') # True 

st.isValid('{[()}') # False 