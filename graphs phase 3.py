#################################PHASE 3###################################

import sys
import sources.collections.graphs
import unittest

class Map():
    def __init__(self):
        self.graph=sources.collections.graphs.Graph()
        
    #With this function we create a new object vertex. 
    def addDeliveryPoint(self, key,street, number, postalcode):
        self.graph.addVertex(key,street, number, postalcode)
        
        
    #With this function we create a new connection between two nodes    
    def addConnection(self, point1, point2, distance):
        self.graph.addEdge(point1, point2, distance)
        
        
   #With this function we remove a new connection between two nodes, if they are in the map.
    def removeConnection(self, point1, point2):
        if point1 not in self.graph.vertices:
            print(point1,' does not exist!')
            return
        
        if point2 not in self.graph.vertices:
            print(point2,' does not exist!')
            return
        
        for a in self.graph.vertices: 
            if a==point1:
                for i in self.graph.vertices[a].neighbors: 
                     if i[0]==point2:  #when the two points are found, we remove the connection 
                         self.graph.vertices[a].neightbors.remove(i)
        
        for i in self.graph.conexions:
            if i[0]==point1 and i[1]==point2:
                self.graph.conexions.remove(i)
                print("we have removed the conexion from "+str(point1)+' to '+str(i[1])+' that takes '+str(i[2])+' km')
        
    
    #This function is used to print all the connections, iterating the list of points.    
    def __str__(self):
        
        for v in self.graph.vertices:
           # result+='\n'+str(v)+':'
            for adj in self.graph.vertices[v].neighbors:
                #result+=str(adj)
                print('from '+ str(v)+' to '+str(adj[0].id)+': takes '+str(adj[1]))
            
      
    #This function is used to see if two nodes are conencted, checking the list of points of the map.
    def areConnected(self,point1, point2):
        for i in self.graph.vertices:
            if i==point1:
                for a in self.graph.vertices[i].neighbors:
                    if a[0].id==point2:
                        return ("yes, they are connected, and the distance is "+ str(a[1]))
        return -1
    
                 
    def generateRoute(self):
        self.graph.dfs()
        print(self.graph.inorder)
        
    #This function returns the index of the point (that must have not been visited) that has the minimum distance. 
    def minDistance(self, distances, visited): 
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for i in self.graph.vertices: 
            if distances[i] <= min and visited[i] == False: 
                min = distances[i] 
                min_index = i 
    
        return min_index 
    
    #This function is used to compute the minimum distance between two nodes.
    def minRoute(self, origin,end): 
        
        visited={}  #we create this dictionary in which we will include the nodes that have been visited, in order to not visitem them again
        for v in self.graph.vertices.keys():
            visited[v]=False

        
        previous={}  #The previous dictionary to add the previous node, to compute the correct path.
        for v in self.graph.vertices.keys():
            previous[v]=-1


        distances={}  #In this dictionary we will add the distances
        for v in self.graph.vertices.keys():
            distances[v]=sys.maxsize


        distances[origin] = 0
        
        for n in range(len(self.graph.vertices)): 
           
            u = self.minDistance(distances, visited) 
            
            visited[u] = True
            
            for adj in self.graph.vertices[u].neighbors:
                i=adj[0].id
                w=adj[1]
                if visited[i]==False and distances[i]>distances[u]+w:
                    distances[i]=distances[u]+w   
                    previous[i]=u       
        
        
        self.printSolution(distances,previous,origin,end)
        
        
    #This function uses the distionaries created before, to print which one would be the minimum path between v and end.
    def printSolution(self,distances,previous,v,end): 
        print("Mininum path from ",v," to ", end)
        for i in self.graph.vertices:
            if i==end:
                if distances[i]==sys.maxsize:
                    print("There is not path from ",v,' to ',i)
                else: 
                    minimum_path=[]
                    prev=previous[i]
                    while prev!=-1:
                        minimum_path.insert(0,prev)
                        prev=previous[prev]
                    
                    minimum_path.append(i)  
    
                    print(v,'->',i,":", distances[i],minimum_path)
                
                
class Test(unittest.TestCase):
    def setUp(self):
        self.Map=Map()
        self.Map.addDeliveryPoint(1, "Fidias", 3, 28232)
        self.Map.addDeliveryPoint(2, "Epidauro", 19, 28232)
        self.Map.addDeliveryPoint(3, "Castellana", 1,10251)
        self.Map.addDeliveryPoint(4, "Princesa", 14, 87432)
        self.Map.addConnection(1,4,30)
        self.Map.addConnection(4,2,15)
        self.Map.addConnection(2,3,4)
        self.Map.addConnection(1,3,33)
    
    def testRemoveConnection(self):
        
        self.Map.removeConnection(1,3)
        self.Map.__str__()
    
    def testAreConnected(self):
        print(self.Map.areConnected(1,3))
        
    def testGenerateRoute(self):
        self.Map.generateRoute()
        print(self.Map.minRoute(1,3))
    
                           
unittest.main(argv=['first-arg-is-ignored'], exit=False)                   

