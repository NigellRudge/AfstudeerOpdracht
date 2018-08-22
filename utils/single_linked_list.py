class  Node:
    """ 
        This node is that will be used in an singly
        linked list implementation
    """
    def __init__(self,data):
        self.value = data
        self.pointer = None
    
    def setPointer(self, value):
        self.pointer = value
    
    def removePointer(self):
        self.pointer = None
    
    def  deleteValueAtPointer(self):
        del self.pointer

class SingleLinkedList:
    """ 
        An implementation of a singly linked list
         i may this to hold the values of the Road objects
    
    """
    def __init__(self):
        self.head = None
    
    def listPrint(self):
        node_to_print = self.head
        while node_to_print is not None:
            print(node_to_print.value)
            node_to_print = node_to_print.pointer
    
    def insertAtStart(self, value):
        new_node = Node(value)
        new_node.setPointer(self.head)
        self.head = new_node
    
    def insertAtEnd(self, value):
        new_node = Node(value)
        loop_node = self.head
        while loop_node.pointer is not None:
            loop_node.setPointer(loop_node.pointer)       
        loop_node.setPointer(new_node)
    
    def insertAtPosition(self,between_node,value):
        if between_node is None:
            print("node passed to the funcion not part of a linked_list")
            return
        new_node = Node(value)
        new_node.setPointer(between_node.pointer)
        between_node.setPointer(new_node)

    def DeleteNode(self,data_to_remove):
        list_head = self.head

        if(list_head is not None):
            if(list_head.value == data_to_remove):
                self.head.setPointer(list_head.pointer)
                list_head = None
                return
        
        while list_head.pointer is not None:
            if(list_head.value == data_to_remove):
                break
            prev_node = list_head
            list_head.setPointer(list_head.pointer)
        
        if(list_head == None):
            return
        
        prev_node = list_head
        list_head = None


            