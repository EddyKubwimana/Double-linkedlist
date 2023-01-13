class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedlist:
    
    def __init__(self):

        self.head = None
        self.tail = None
        self.size = None
        
    def append(self,node):
        
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
    
    def insert_left(self,node,before):
        
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
        ''' print the list object'''
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
       ''' delete a given node'''
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
    @property
    def sort(self):
        ''' sort and return the sorted list in ascending order'''
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

    def reverse(self):
      '''reverse and return the reversed list'''
      pass

    def index(self, value):
        ''' the function return the index of the value in a list and return None if the value is not in the list'''
        if self.head == None:
            return -1
        cur_node = self.head
        index = 0
        while cur_node:
            if cur_node.data == value:
                return index
            else:
                index +=1
                cur_node = cur_node.next
        return index
            
    
                    
            
        
                   
#testing the different functions  

l = DoubleLinkedlist()
l.append(10)
l.append(20)
l.append(4)
l.append(30)
l.sort
print(l)
print(l.index(30))



            
        
        
        
