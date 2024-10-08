class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class SLinkedList:
    def __init__(self):
        self.head = Node()
        
    def add_node(self, data):
        cur = self.head
        
        while cur.next:
            cur = cur.next
        
        cur.next = Node(data)
        
    def display(self):
        cur = self.head
        
        elem = []
        while cur.next:
            elem.append(cur.next.data)
            cur = cur.next
        
        print(elem)

    def delete(self, idx):
        cur = self.head
        
        if cur.next == None:
            raise Exception("No nodes exist in list")
        
        elif idx == 0:
            cur.next = cur.next.next
        
        count = 0
        while cur.next:
            if count == idx:
                cur.next = cur.next.next
            
            cur = cur.next
            count+=1
    
    def index_add(self, idx, data):
        cur = self.head
        index_node = Node(data)
        #if idx == 0:
        #    index_node.next = cur.next
        #    cur.next = index_node
            
        count = 0
        while cur.next:
            if count == idx:
                index_node.next = cur.next
                cur.next = index_node
            cur = cur.next
            count+=1
            
            
if __name__ == "__main__":
    SLL = SLinkedList()
    SLL.add_node(5)
    SLL.add_node(2)
    SLL.add_node(4)
    SLL.display()
    SLL.delete(1)
    SLL.display()
    SLL.index_add(0, 20)
    SLL.index_add(2, 19)
    SLL.display()