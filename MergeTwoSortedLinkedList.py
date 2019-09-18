#Merge two sorted Linked Lists

class ListNode(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class Solution(object):
  def mergeTwoLists(self, list1, list2):
    dummy = current = ListNode(0)
    while list1 and list2:
      if list1.value < list2.value:
        current.next = list1
        list1 = list1.next
      else:
        current.next = list2
        list2 = list2.next
      current = current.next
    current.next = list1 or list2
    return dummy.next
