class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Solution:
  def display(self, head):
    current = head
    while current:
      print(current.data, end=' ')
      current = current.next

  def insert(self, head, data):
    nn = Node(data)
    if head is None: return nn
    tail = head
    while tail.next is not None:
      tail = tail.next
    tail.next = nn
    return head


mylist = Solution()
inp = [2, 3, 4, 1]
T = len(inp)
head = None
for i in range(T):
  data = inp[i]
  head = mylist.insert(head, data)
mylist.display(head)
