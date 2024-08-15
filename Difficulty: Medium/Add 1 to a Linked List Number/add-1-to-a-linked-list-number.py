#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr:
            newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode
        return prev
        
    def addOne(self,head):
        rh1 = Solution.reverse(self, head) 
        carry  = 1
        ans = Node(-1)
        temp = ans
        while rh1 or carry != 0:
            d1 = rh1.data if rh1 is not None else 0
            
            
            summ = d1 + carry
            d = summ % 10
            carry = summ // 10
            
            temp.next = Node(d)
            temp = temp.next
            
            rh1 = rh1.next if rh1 is not None else None
            
            
        res = ans.next
        ans = Solution.reverse(self, res)
        #ans.next = None
        while ans.data == 0 and ans.next is not None:
            ans = ans.next
        if ans is None:
            return Node(0)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        first = arr[0]
        for i in arr:
            list1.insert(i)
        n1 = list1.size
        resHead = Solution().addOne(list1.head)

        n2 = 0
        current = resHead
        while current is not None:
            current = current.next
            n2 += 1
        if n2 == 1:
            if n1 > 1:
                print("Return the modified linkedlist")
            if n1 == 1:
                if first < 9:
                    PrintList(resHead)
                    print()
                else:
                    print("Return the modified linkedlist")
        else:
            PrintList(resHead)
            print()

# } Driver Code Ends