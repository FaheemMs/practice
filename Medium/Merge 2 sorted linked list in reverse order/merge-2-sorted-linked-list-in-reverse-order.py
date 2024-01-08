#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
        def merge(h1, h2):
            if h1 is None:
                return h2
            if h2 is None:
                return h1
            newLis = Node(-1)
            temp = newLis
            while h1 and h2:
                if h1.data <= h2.data:
                    temp.next = h1
                    h1 = h1.next
                else:
                    temp.next = h2
                    h2 = h2.next
                temp = temp.next
            if h1 is not None:
                temp.next = h1
                temp = temp.next
            if h2 is not None:
                temp.next = h2
                temp = temp.next
            return newLis.next
        
        def reverse(h):
            prev = None
            while h != None:
                newNode = h.next
                h.next = prev
                prev = h
                h = newNode
            return prev
        h = merge(h1, h2)
        #print('n', h.data)
        new_head = reverse(h)
        return new_head
        
        #return head of merged list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        arr2=[int(x) for x in input().split()]
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        ob = Solution()
        resHead=ob.mergeResult(ll1.head,ll2.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends