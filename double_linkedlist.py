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
    def insert_left(self,before, node):
          new_node= Node(node)
          if self.tail == None:
              self.tail = new_node
          cur_node = self.tail
        
          while cur_node:
            if cur_node.data == before:
                side_left = cur_node.prev
                side_right = cur_node
                
                
                new_node = Node(node)
                prev_node = new_node
                prev_node.next = side_right
                side_right.prev = prev_node
                prev_node.prev = side_left
                side_left.next = prev_node
            
                break
                
            cur_node = cur_node.prev

    def print_nodes(self):
        if self.head == None:
            return
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
           
              
        

l = DoubleLinkedlist()
l.insert_right(10)
l.insert_right(40)
l.insert_right(20)
l.insert_right(30)
l.print_nodes()
print()
l.insert_left(20,7)
l.insert_left(30,8)
l.insert_left(40,5)
l.insert_left(7,100)
print()
print()

l.print_nodes()


            
        
        
        
