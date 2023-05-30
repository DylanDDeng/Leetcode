class Solution:
    def isValid(self, s: str) -> bool: 
        stack = [] 

        for item in s:  
            # 遍历输入的括号， '{', '[', '(' 
            # 栈中存入对应的括号 
            if item == '(': 
                stack.append(')')
            elif item == '[': 
                stack.append(']') 
            elif item == '{':
                stack.append('}')  
            # 遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了
            # 括号不匹配 
            elif stack[-1] != item or not stack: 
                return False  
            # 如果栈中的右括号能与输入的括号相匹配，则删除栈中的右括号
            else: 
                stack.pop() 
        # 遍历完之后 栈如果为空则为True， 不然就是False 
        return True if not stack else False 



# 测试  
st = Solution() 
st.isValid('{[()]}') # True 

st.isValid('{[()}') # False 