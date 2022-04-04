##########################PHASE 1##########################################
import smallclasses
import random
from sources.collections import classDoubleLinkedLists
import unittest
 

class AmazonManagement:
    def __init__(self):
        self.Orders= classDoubleLinkedLists.DoublyLinkedList()
        self.DSmembers=classDoubleLinkedLists.DoublyLinkedList()
        self.delivered=classDoubleLinkedLists.DoublyLinkedList()
        self.incidents=classDoubleLinkedLists.DoublyLinkedList()
        self.activestaff= classDoubleLinkedLists.DoublyLinkedList()  
        
    
    #The time complexity is O(n) and the best case would be if the list order was empty, adn the worst one if it was not.   
    #With this funcion we create the list of orders and print them.      
    def loadOrders(self, order):
        
        for i in order:
            self.Orders.addLast(i) #the time complexity is O(1)
            
        head=self.Orders.head
        while head!=None:
            print("the id of the new packet is"+ " "+str(head.element.Id))
            head=head.next
            
        
    #The time complexity is O(n), and the best case would be if  the list member was empty, and the worst oneif it was not.   
    #With this funcion we create the list of the workers, and print them.
    def loadDSmembers(self,member):
        
        for i in member:  
            
            self.DSmembers.addLast(i)
            print("we have added a new member: " + i.name+ " "+ i.lastname)
            
            if i.status=="active":
                
                self.activestaff.addLast(i)  
            
                
    #The time complexity is O(n^2) The best case is that the list is empty, so that the member were added the first one and would not be necessary to go through the whole list. The worst case would be if the member's surname were the last one in alphabetical order, and the whole list need to be travelled. 
    #With this function iteartes through the whole list in order to add member in the correct alphabetical position.
    def insert(self,lista, member):
                header=lista.head
                
                
                if lista.isEmpty():
                    lista.addFirst(member) #time complexity O(1)
                    
                else:
                    headersurname=lista.head.element
                    counter=0
                    
                    while header!=None and member.lastname > headersurname.lastname:   #we iterate until we find the right position
                        header=header.next
                        counter+=1
                    
                    if member.lastname<= headersurname.lastname:
                        lista.insertAt(counter , member) #Time complexity O(n)
                    
                    if header==None:
                        lista.addLast(member)   #Time complexity O(n)
    
    #The time complexity is O(n). The best case is if the list DSmembers is empty, and the worst if it is not, since it would have to go through the whole list. 
    #With this function we go iterate through the list of workers, and then we use the funcion insert(), that sorts them.        
    def sort(self):
            self.sortedDSmembers=classDoubleLinkedLists.DoublyLinkedList()
            head=self.DSmembers.head
            
            while head:
                self.insert(self.sortedDSmembers, head.element)
                head=head.next
        
             
    
    #The time complexity is O(n) The best case is if the list sortedDSmembers is empty, and the worst if it is not, since it would have to go through the whole list. 
    #This function prints all the workers in alphabetical order that we had obtain in the previous functions.
    def showDSmembers(self):
        
        self.sort()
        print("A list of the workers by alphabetical order:")
        
        head=self.sortedDSmembers.head
        while head:
            print(head.element.name, head.element.lastname)
            head=head.next
            
        
    #The time complexity is O(n^3) The best case is if the list of orders were empty or if the list of members was empty, and the worst case would be if the list of orders and th eone of members were not empty.
    #This function iterates through the list of orders and assignates each to a worker of the same with the assigned zone.
    def assingDistribution(self):
        
        head=self.Orders.head  #we start with the first order
        found=False
        
        while head:   #we iterate through the orders
            found=False
            location=head.element.postalcode
            members=self.DSmembers.head
            
            while members and not found: #until we do not find a member, we also iterate through that list.
                
                memberzone=members.element.zone.head
                while memberzone and memberzone.element!= location:
                    memberzone=memberzone.next
                    
                
                if memberzone and memberzone.element==location and members.element.status=="active":  #we check if the location of the member is the same as the one of the packet, and if the member is active.
                    members.element.zone.addLast(location)
                    members.element.orders.addLast(head.element)
                    
                    print("we have added to the worker"+" "+members.element.name+" "+"the packet with id"+" "+str(head.element.Id))
                    found=True  #if it is, we go out of the loop, and assign the next order.
                
                members=members.next
            
            if not found:  #if after goign through all the members, no one coincides, we assign if to the one with less zones.
                
                length=100
                
                first_distributor=self.DSmembers.head
                while first_distributor:
                    
                    if first_distributor.element.zone.size<=length: #we find the minimum of number of zones
                        length=first_distributor.element.zone.size
                        
                    first_distributor=first_distributor.next
                    
               
                min_head=self.DSmembers.head
                while min_head and min_head.element.zone.size!=length:  #we iterate to find the worker with less zones.
                    min_head=min_head.next
                    
                if min_head and min_head.element.zone.size==length: #we add the new zone to the worker and the order.
                   
                    min_head.element.zone.addLast(location)
                    min_head.element.orders.addLast(head.element)
                    
                    print("we have added to the worker"+" "+min_head.element.name+" "+"the packet with id"+" "+str(head.element.Id))
                    found=True
                
                  
            
            head=head.next
               
    
    
    #The time complexity is O(n^2). The best case is if the list of headorders is empty, and the worst one if it is not, since it would have to travel the whole list.
    #This function, given a distributor, tries to deliver all its packages.
    
    def deliverPackage(self,distributor):
        headorders=distributor.orders.head
        
        while headorders: #we iterate through all of its orders.
            package=headorders.element
            
            finalresult=""
        
            
            if random.randint(0,1)==1:
                
                correctly=True
            else:
                correctly=False
            
            if correctly:
                
                distributor.orders.removeFirst() #Time complexity O(1)
                
                self.delivered.addLast(package) #O(n)
                                
                finalresult= str(package.Id)+","+"correctly delivered"
                
                print(finalresult)
            
            else:  #if it is not delivered, we check the number of incidents of the package in order to add it there or to the incidents list.
                if package.incidents<=3:
                    
                    distributor.orders.removeFirst()
                    distributor.orders.addLast(package)
                    finalresult+= str(package.Id)+ ","+"pending"
                    
                    print(finalresult)
                    package.incidents+=1
                    
                else:
                    self.incidents.addLast(package)
                    finalresult+=str(package.Id)+ "added to the incidents list"
                    print(finalresult)
            
            headorders=headorders.next #once we have dealt with one order, we go to the next one.
  
    
    
            
    #The time complexity is O(n^3). The best case is if there were not any active staff, and the worst one if there were a lot of them.
    #This function iterates through the list of active staff to deliver all of their orders.
    def deliver(self):
        
        head=self.activestaff.head
            
        while head:
            
            worker=head.element
        
            self.deliverPackage(worker)
            
            head=head.next
          
            
    #The time complexity is O(n^4). The best case would be if there were not orders ro distribute, so that the list orders was empty. And the worst case is if it was not empty.
    #This function distributes all of the orders of a removed distributer.
    def removeDSmember(self,distributor):
        
        if distributor!=None:
            distributor.status="inactive"
        
            head=distributor.orders.head
            
            
            
            while head:  #we iterate through al of the orders
                order=head.element
                found=False
                location=order.Id
              
                members=self.DSmembers.head
                
                while members and not found: #we iterate through the rest of the members
                    membersObj=members.element
                    headzones=membersObj.zone.head
                    while headzones:  #we iterate through all of the zones of each member, in order to see if the zone coincides with the one of the order.
                        
                        zone=headzones.element
                        
                        if headzones.element!= location:
                            headzones=headzones.next
                            
                            
                        if membersObj.status=="active" and zone==location:  #if we find it, we add the order to the list, adn the zone.
                            members.element.zones.addLast(location)
                            members.element.orders.addLast(order)
                            print("we have associated the packet with id"+ str(location)+"to the distributor"+str(zone))
                            found=True
                        
                    if not found: 
                        members=members.next
                    
                if not found:  #if no other member has the same zone, we add the order to the incidents list.
                    self.incidents.addLast(order)
                    print("we have added the packet with id "+str(location)+" to the incidents list")
                    
                    
                    
                head=head.next
                
                
class Test(unittest.TestCase):
    def setUp(self):
        zone1=classDoubleLinkedLists.DoublyLinkedList()
        zone1.addFirst(10)
        zone1.addLast(13)
        zone1.addFirst(20)
        zone2=classDoubleLinkedLists.DoublyLinkedList()
        zone2.addFirst(12)
        zone2.addLast(50)
        zone2.addFirst(22)
        zone3=classDoubleLinkedLists.DoublyLinkedList()
        zone3.addFirst(11)
        zone3.addLast(25)
        zone3.addFirst(15)
        zone4=classDoubleLinkedLists.DoublyLinkedList()
        zone4.addFirst(17)
        zone4.addLast(16)
        zone4.addFirst(24)
        self.Amazon=AmazonManagement()
        self.order=[smallclasses.Package(1, "las rozas", 10), smallclasses.Package(2, "pozuelo", 10), smallclasses.Package(3, "majadahonda", 12), smallclasses.Package(4, "leganes", 13), smallclasses.Package(5, "madrid centro", 14)]
        self.member=[smallclasses.DSmember(200, "sofia", "perez", "active", zone1), smallclasses.DSmember(201, "maria", "martín", "active", zone2), smallclasses.DSmember(202, "keyla", "juñoz", "active", zone3), smallclasses.DSmember(203, "marta", "garcia", "active", zone4)]
        self.Amazon.loadOrders(self.order)
        
        self.Amazon.loadDSmembers(self.member)

    
    def testAlphabeticalOrder (self):
        
        print(self.Amazon.showDSmembers())
    
    def testAssigndistribution(self):
        
        print(self.Amazon.assingDistribution())  
        
        print(self.Amazon.deliverPackage(self.Amazon.DSmembers.head.element))
        print(self.Amazon.deliver())
        print(self.Amazon.removeDSmember(self.Amazon.DSmembers.head.next.element))
  
        
        
unittest.main(argv=['first-arg-is-ignored'], exit=False)
