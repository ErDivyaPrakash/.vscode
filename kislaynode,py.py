class Node:
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

        def insert(self, data):
            if self.data == data:
                return

            if data<self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)

            else:
                if self.right:
                    self.right.insert(data)

                else:
                    self.right = Node(data)


        def search(self,data)  :
            if self.data  == data:
                print('found at root node')

                if data < self.data :
                    if self.left:
                        self.left.search(data)
                    else:
                        print('data is node found')
                else:
                    if self.right :
                        self.right.search(data)
                    else:
                        print('data is not found')
                        
                      
#driver code
root = Node(20)
# root.left = Node(34)
# root.right.insert(25)
# root = 
# root = int(3)



                    


                

            


