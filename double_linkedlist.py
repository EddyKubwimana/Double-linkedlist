class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedlist:
    def __init__(self):

        self.head = None
        self.tail = None
    def insert_right(self,node):
        new_node = Node(node)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node:
            if cur_node.next == None:
                
                new_node = Node(node)
                prev_node = new_node
                prev_node.prev = cur_node
                cur_node.next = new_node
                self.tail= cur_node.next
    
    
                break
            cur_node = cur_node.next
    def insert_left(self,node):
          new_node= Node(node)
          if self.tail == None:
              self.tail = new_node
          cur_node = self.tail
        
          while cur_node:
            if cur_node.prev != None:
                
                new_node = Node(node)
                prev_node = new_node
                prev_node.next = cur_node
                cur_node.next = prev_node
                break
            cur_node.next = cur_node.prev
           
              
        

l = DoubleLinkedlist()
l.insert_right(10)
l.insert_right(20)
l.insert_right(30)
l.insert_right(40)

print()
print(l.tail.prev.prev.prev.data)


            
        
        
        
