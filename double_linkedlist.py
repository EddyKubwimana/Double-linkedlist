class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedlist:
    def __init__(self):

        self.head = None
    def insert_right_end(self,node):
        if self.head == None:
            new_node = Node(node)
            self.head = new_node
            
        
        cur_node = self.head
        while cur_node:
            if cur_node.next == None:
                new_node = Node(node)
                cur_node.next = new_node
                cur_node.prev = cur_node
                print(cur_node.next.data)
                print(cur_node.prev.data)
                break
            cur_node = cur_node.next


l = DoubleLinkedlist()
l.insert_right_end(10)
l.insert_right_end(20)
l.insert_right_end(30)
l.insert_right_end(40)
print()
print(l.head.next.next.data)
print(l.head.next.next.prev.data)

            
        
        
        
