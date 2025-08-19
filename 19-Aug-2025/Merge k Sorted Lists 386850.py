# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        if not lists:
            return ans.next
        heap = []
        heapify(heap)
        while True:
            for i in range(len(lists)):
                if lists[i]:
                    heappush(heap, lists[i].val)
                    lists[i] = lists[i].next
            if heap:
                ans.next = ListNode(heappop(heap))
                ans = ans.next
            flag = True
            for i in range(len(lists)):
                if lists[i] != None:
                    flag = False

            if flag and len(heap) == 0:
                break
        return dummy.next