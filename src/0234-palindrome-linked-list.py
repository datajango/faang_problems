# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# get tail
# this could be expensive

# compare head to tail
# increment head
# decrement tail

# This is a single linked-list, not doubly linked list

# get length of list 
# 1 to 1,000,000 nodes


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # set list head
        list_head = head
        values = [] # list of values

        def get(node):
            if not node:
                return None, None
            val = node.val
            node = node.next
            return val,node
        
        loop=True
        while loop:
            value,list_head = get(list_head)            
            if value==None:
                loop = False
            else:
                values.append(value)
                
        half = int(len(values)/2)
        if half==0:
            return True 

        l2 = values[0:half]
        l3 = values[-half:]
        l3.reverse()

        if l2==l3:
            return True

        return False

n = ListNode(1)
n1 = ListNode(0, n)
n2 = ListNode(0, n1)
n3 = ListNode(2, n2)
n4 = ListNode(1, n3)

fun = Solution()
results = fun.isPalindrome(n2)
print(results)
