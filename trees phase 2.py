##########################PHASE 2#######################################

from sources.collections import BinarySearchTree
from sources.collections import classDoubleLinkedLists
import unittest
 

#import main
import smallclasses

class tree:
    
    def __init__(self):
        
        self.tree=BinarySearchTree.BinaryTree()
        self.size=self.tree.size(self.tree.root)
        
              
    #The time complexity is O(n). The best case is the element is already in the tree, and the worst case if it is not. 
    #With this function we create a new zone.
    def CreateZone(self, x):
        
        self.tree.insert(x)
        
        
        self.size+=1
        
    #The time complexity is O(n^2). In this case, there is no best case and worst case, since in every case we have to do the same, add the worker to the zone list.   
    #This function is used to add a worker to a zone.
    def AssignDistributor(self,zone,distributor):
        
        zone= self.find(zone)
        
        zone.element.workers.addLast(distributor)
        print("we have added the distributor "+ distributor.name+ " to the zone "+str(zone.element.Id))


    #The time complexity is O(n^2). The best case is if the worker is at the beginning of the list, therefore the while loop is shorter. However, the worst case would be if th eworker is found at the end of the list, having to go through the whole of it.
    #This function is used to delete a distributor from a zone.
    def DeleteDistributor(self, zone, distributorId):
        zone=self.find(zone)
        
        head=zone.element.workers.head
        found=False
        counter=0
        
        while head and not found:  #we iterate through the lsit of workers until we find it.
            
            if head.element.identifier==distributorId:
                
                zone.element.workers.removeAt(counter)
                print("worker "+ str(distributorId)+" has been removed")
                
                found=True
                
            else:
                
                counter+=1
                head=head.next
                
    
        
    #The time complexity is O(n^2)
    #This function is used to print the workers of each zone from the root to the buttom (using recursion).
    def ShowZones(self):
        self.allNodes=classDoubleLinkedLists.DoublyLinkedList()
        self.inorder=self.inorder()
        
    
    #The time complexity is O(n^2)   
    def inorder(self):
        print('in ascending order:')
        self.allNodes=classDoubleLinkedLists.DoublyLinkedList()
        self._inorder(self.tree.root)
        print()
        return self.allNodes

    #The time complexity is O(n^2). There is not best case or worst case, since we have to print them all.
    def _inorder(self,currentNode):
        if currentNode!=None:
            
            self._inorder(currentNode.leftChild)
            
            print("zone: "+ str(currentNode.element.Id))
            head=currentNode.element.workers.head
            print("the list of workers of the zone "+str(currentNode.element.Id)+":")
            while head: 
                
                print(head.element.name)
                head=head.next
            self.allNodes.addLast(currentNode.element)                
            
               
            self._inorder(currentNode.rightChild)
    
    #The time complexity is O(n^2).The best case was if the list of workers is empty, and the worst case if it is not. 
    def ShowDistributors(self, zone):
        self.sorted=classDoubleLinkedLists.DoublyLinkedList()
        self.workers=zone.workers
        head=self.workers.head
    
        while head:
            self.insert(self.sorted, head.element)
            head=head.next
       
        
        head1=self.sorted.head
        print("the workers of the zone "+str(zone.Id)+" in alphabetical order:")
        while head1!=None:
            
            print(head1.element.name+" "+head1.element.lastname)
            head1=head1.next
            
    #The time complexity is O(n^3).The best case is if the zone does not have workers, and the worst case if it has.  
    #This function is used to delete z given zone, having to reassign its workers.     
    def DeleteZone(self, zone):
        
        listofWorkers=zone.workers
                
        self.previous=classDoubleLinkedLists.DoublyLinkedList()
        self.post=classDoubleLinkedLists.DoublyLinkedList()
        
        node=self.find(zone)   
        self.tree.removeNode(node)
        
        head=self.allNodes.head
        
        while head:  #we iterate through the list of zones
            headElem=head.element
            if headElem.Id < zone.Id: #we add the zones whose id is smaller than the one that is being deleted. 
                self.previous.addLast(head.element)   
                
            elif headElem.Id>zone.Id:   #we add the zones whose id is larger than the one that is being deleted. 
                self.post.addLast(head.element)
                
            head=head.next
            
        
            
        if self.previous.isEmpty():  #if there is no smaller zone
            
            head=listofWorkers.head
            zone=self.post.head
            
            while head: #we iterate through the list of bigger zones
                zoneElem=zone.element
                while zone and head: #we start assigning workers to each of the zones of the list
                    zoneElem.workers.addLast(head)
                    print("the worker "+head.element.name+" has been reassigned to zone "+str(zoneElem.Id))
                    zone=zone.next
                    
                    head=head.next
                
                
                if not zone:
                    zone=self.post.head
                    
                
              
        
        elif self.post.isEmpty():  #if there is no bigger zone
            
            head=listofWorkers.head
            zone=self.previous.head
            
            while head:
                zoneElem=zone.element
                
                while zone and head: #we start assigning workers to each of the zones of the list
                    zoneElem.workers.addLast(head)
                    print("the worker "+head.element.name+" has been reassigned to zone "+str(zoneElem.Id))
                    zone=zone.next
                    
                    head=head.next
                
            
                if not zone:
                    zone=self.post.head
              
        
        else:   #if we have bigger and smaller zones
            counter=0
            head=listofWorkers.head
            zone=self.previous.head
            
            while head and counter<= listofWorkers.size//2:   #We divide the list of workers by halves
               
                zoneElem=zone.element
                while zone and head:   #we assign the first half to the smaller zones
                    zoneElem.workers.addLast(head)
                    print("the worker "+head.element.name+" has been reassigned to zone "+str(zoneElem.Id))
                    zone=zone.next
                        
                    head=head.next
                
                
                if not zone:
                    zone=self.previous.head
                
            
            zone=self.post.head
            while head and counter<= listofWorkers.size:
                zoneElem=zone.element
                while zone and head:   #we assign the second half to the bigger zones
                    zoneElem.workers.addLast(head)
                    print("the worker "+head.element.name+" has been reassigned to zone "+str(zoneElem.Id))
                    zone=zone.next
                    head=head.next
                
                if not zone:
                    zone=self.post.head
        
   
    #The time complexity is O(n). The best case is if the list of members is empty, and the worst case if it is not.    
    #This method is used to add a member to a list in alphabetical order.
    def insert(self,lista, member):
        header=lista.head
        
        if lista.isEmpty():
            lista.addFirst(member)
            
        else:
            headersurname=lista.head.element
            counter=0
            
            while header!=None and member.lastname > headersurname.lastname:  #we iterate through the list until we find the right position.
                header=header.next
                counter+=1
            
            if member.lastname<= headersurname.lastname:
                lista.insertAt(counter , member)
            
            if header==None:
                lista.addLast(member)   
                
         
            
    #The time complexity is O().The best case is if the tree is balanced and the worst if it is not.
    def IsBalanced(self):
        if self.tree._checksizeBalanced(self.tree.root)==True:
            print("the tree is size balanced")
        
        else:
            print("the tree is not size balanced")
            self.Balance(self.tree.root)
            
    #The time complexity is O(n). There is not best or worst case since all the node and its childs have to do all the steps.        
    def Balance(self, node):
        
        #we do the right steps in order to balance the tree, taking into account both sides of the tree adn their sizes.    
        if self.tree.size(node.rightChild) < self.tree.size(node.leftChild):
            
            predecessor= self.tree.predecessor(node)
                    
            predecessorElem= predecessor.element
             
            nodeElem = node.element
             
            node.elem= predecessorElem
             
            self.tree.insertNode(predecessor, nodeElem)
            
            self.tree.removeNode(predecessor)
                    
                      
               
        else: 
            
            sucessor= self.tree.sucessor(node)
            
            sucessorElem=sucessor.element
            
            
            nodeElem=node.element
            
            node.element=sucessorElem
            
            self.tree.removeNode(sucessor)
            
            self.tree.insert(nodeElem)
            
            
            
        self._Balance(node.leftChild)
        self._Balance(node.rightChild)
        

      
        
      
    #The time complexity is O(n^3). The best case is ifonce you neter in the loop, the size balance factor is one, and the worst if it is not.
    def _Balance (self, node):  
        
        #we continue doing recursively this balancing until the whole tree is balanced.
        if node:
            while abs(self.tree.size(node.leftChild)-self.tree.size(node.rightChild))>1:
       
                if node.leftChild and node.rightChild:
                
                   left=self.tree.size(node.leftChild)
                   right=self.tree.size(node.rightChild)
                   
                   if abs(left-right)>1:
                       
                       self.Balance(node)
                       
                   else:
                       
                       self._Balance(node.rightChild)
                       self._Balance(node.leftChild)
                       
    
    #This function is used to check if a tree is size balance, and if not, balance it.
    def IsBalancedHeight(self):
        if self.tree.CheckHeightbalance(self.tree.root)==True:
            print("the tree is height balanced")
        
        else:
            print("the tree is not height balanced")
            self.BalanceHeight(self.tree.root)
            
            
    
    def BalanceHeight(self, node):
        
        #First we need to know which type of rotation is needed.
        if self.tree._height(node.leftChild)>self.tree._height(node.rightChild):
            
      
            if abs(self.tree._height(node.leftChild.leftChild)-self.tree._height(node.leftChild.rightChild))<=1:  #simple right rotation
                
                self.RightRotate(node.leftChild)
            
            else:  #double right rotation
                self.LeftRotate(node.leftChild)
                self.RightRotate(node)
        
        else:
            
            if abs(self.tree._height(node.rightChild.rightChild)-self.tree._height(node.rightChild.leftChild))<=1: #simple left rotation
                self.LeftRotate(node)
            
            
            else: #double left rotation
                self.RightRotate(node.rightChild)
                self.LeftRotate(node)
                
                
            
        self._BalanceHeight(node.leftChild)
        self._BalanceHeight(node.rightChild)    

      
    def RightRotate(self, node):
        print("right rotation")
        if node:
            left=node.leftChild
            if left:
                
                #perform rotation
                copy=node.element
                leftelem=left.element
                node.element=leftelem
                if left.rightChild!=None: #if it has a child
                    
                    x=left.rightChild
                    self.tree.removeNode(left.rightChild)
                    self.tree.removeNode(left)
                    new=BinarySearchTree.Node(copy)
                    
                    if node.rightChild!=None:
                        C=node.rightChild
                        node.rightChild=new
                        new.rightChild=C
                    else:  #no child
                        node.rightChild=new
                      
                    n=BinarySearchTree.Node(x.element)
                    new.leftChild=n
                
                else:
                    self.tree.removeNode(left)
                    new=BinarySearchTree.Node(copy)
                    C=node.rightChild
                    node.rightChild=new
                    new.rightChild=C
                    
        
    def LeftRotate(self,node):
        print("left rotation")
        if node:
            right=node.rightChild
            if right:
                #perform rotation
                copy=node.element
                rightelem=right.element
                node.element=rightelem
                if right.leftChild!=None: #if it has a child
                    x=right.leftChild
                    self.tree.removeNode(right.leftChild)
                    self.tree.removeNode(right)
                    new=BinarySearchTree.Node()
                    if node.leftChild!=None:
                        C=node.leftChild
                        node.leftChild=new
                        new.leftChild=C
                        
                    else:   #no child
                        node.leftChild=new
                      
                    n=BinarySearchTree.Node(x.element)
                    new.rightChild=n
                
                else:
                    self.tree.removeNode(right)
                    new=BinarySearchTree.Node(copy)
                    C=node.leftChild
                    node.leftChild=new
                    new.leftChild=C
          
      
    #This function is used to check if a tree is height balance, and if not, balance it.
    def _BalanceHeight (self, node):  
        
        #we continue doing recursively this balancing until the whole tree is balanced.
        if node:
            #while abs(self.tree._height(node.leftChild)-self.tree._height(node.rightChild))>1:
       
            if node.leftChild and node.rightChild:
            
               left=self.tree._height(node.leftChild)
               right=self.tree._height(node.rightChild)
               
               if abs(left-right)>1:
                   
                   self.BalanceHeight(node)
                   
               else:
                   
                   self._BalanceHeight(node.rightChild)
                   self._BalanceHeight(node.leftChild)
                    
          
        
        
    #The time complexity is O(n^2)        
    def find(self,x):
        
        return self.findNode(self.tree.root,x)
    
    #Time complexity is O(n^2). The best case is if the element coincides with the node, and the worst case if it does not and we have to apply recursion.
    def findNode(self,node,x):
        if node is None:
            return None
        
        if node.element.Id==x.Id:
            return node
        
        if x.Id<node.element.Id:
            return self.findNode(node.leftChild,x)
        
        if x.Id>node.element.Id:
            return self.findNode(node.rightChild,x) 
        
   #The time complexity is O(n).The best case is if the root is none, and the worst case is if it is not.
   #This function is used to print the tree.
    def print2DUtil(self, root, space=0):
        
        if root==None:
            return None
        
        space+=1
        
        self.print2DUtil(root.rightChild, space)
        
        print()
        for i in range(0, space+5):
            print(end="")
        print(root.element.Id)
        
        self.print2DUtil(root.leftChild, space)
        
        
        
    def print2D(self,root) : 
        self.print2DUtil(self.tree.root, 2)
    

            
            
          
    
class Test(unittest.TestCase):
    def setUp(self):
        self.tree=tree()

            
    def test(self):
       
        zone1=smallclasses.Zone(1)
        zone2=smallclasses.Zone(5)
        zone3=smallclasses.Zone(4)
        zone4=smallclasses.Zone(8)
        
        
        print(self.tree.CreateZone(zone1))
        print(self.tree.CreateZone(zone2))
        print(self.tree.CreateZone(zone3))
        print(self.tree.CreateZone(zone4))
        
        worker1=smallclasses.worker(1, "sofia", "perez")
        worker2=smallclasses.worker(2, "keyla", "muñoz")
        worker3=smallclasses.worker(3, "marta", "yusta")
        
        self.tree.AssignDistributor(zone1, worker1)
        self.tree.AssignDistributor(zone2, worker2)
        self.tree.AssignDistributor(zone4, worker3)
        self.tree.AssignDistributor(zone4, worker1)
        
        print(self.tree.IsBalanced())
        print(self.tree.IsBalanced())       
        
         
        self.tree.ShowZones()
        
        self.tree.ShowDistributors(zone4)
        
        print(self.tree.DeleteDistributor(zone2,2 ))
        
        print(self.tree.DeleteZone(zone1)) 
        
        
        print(self.tree.IsBalancedHeight())
        print(self.tree.IsBalancedHeight())
       
        
unittest.main(argv=['first-arg-is-ignored'], exit=False)
