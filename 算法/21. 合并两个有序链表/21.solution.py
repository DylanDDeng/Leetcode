# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空 
        if not l2: return l1
        # 如果l1 当前的值小于等于l2当前的值 
        # 则 l1 下一个节点设置为合并l1的下一个节点和l2后的结果 
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        # 如果l2 当前的值小于等于l1当前的值 
        # 则 l2 下一个节点设置为合并l2的下一个节点和l1后的结果 
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2 

# 测试 
s1 = Solution() 
s1.mergeTwoLists([1,2,4], [1,3,4])    
