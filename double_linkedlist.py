class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedlist:
    
    def __init__(self):

        self.head = None
        self.tail = None
        
    def insert_right(self,node, after = None):
        
        new_node = Node(node)
        if self.head == None:
            self.head = new_node

            
            return
        
        cur_node = self.head
        
        while cur_node:
            if cur_node.next != None and cur_node.data == after:
                    prev_node = new_node
                    prev_node.next = cur_node.next
                    prev_node.prev = cur_node
                    cur_node.next.prev = prev_node
                    cur_node.next =prev_node
                    break

            
            if cur_node.next == None and after == None:
                    
                
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
                prev_node = new_node
                prev_node.next = side_right
                side_right.prev = prev_node
                prev_node.prev = side_left
                side_left.next = prev_node
            
                break
                
            cur_node = cur_node.prev

    
    # function prints the nodes in the list
    def __str__(self):
        if self.head == None:
            return 0
        number = []
        cur_node = self.head
        while cur_node:
            number.append(cur_node.data)
            cur_node = cur_node.next
            return f"{number}"

        
    #function to delete a node after given 
    def delete_node(self,node):
       if self.head == None:
           return
       cur_node = self.head
       while cur_node:
           if cur_node.data == node:
               if cur_node.prev==None:
                   self.head = cur_node.next
                   break
               elif cur_node.next== None:
                   final_list = cur_node.prev
                   self.tail= final_list
                   final_list.next= None
                   break
               else:
                   first_part = cur_node.prev
                   second_part = cur_node.next
                   first_part.next = second_part
                   second_part.prev =first_part
                   break
           cur_node = cur_node.next
    
    #function to find the length of doubly linkedlist
    def size(self):
        if self.head == None:
            return None
        cur_node = self.head
        length = 0
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length
        
    def sort(self):
        if self.head == None:
            return
        cur_node = self.head
        x = True
        while x:
            x = False
            while cur_node.next:
                if cur_node.data > cur_node.next.data:
                    x = True
                    temp_var1 = cur_node.data
                    temp_var2 =cur_node.next.data
                    cur_node.data =temp_var2
                    cur_node.next.data = temp_var1
                    cur_node.next.prev.data = temp_var2
                cur_node = cur_node.next
            cur_node = self.head
    
    
                    
            
        
                   
#testing the different functions  

l = DoubleLinkedlist()
l.insert_right(10)
print(l)



            
        
        
        
