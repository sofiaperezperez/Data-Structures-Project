# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:22:27 2020

@author: sofia
"""
from sources.collections import classDoubleLinkedLists

class Package:  #This class is used in the phase 1 to create the packets.
    def __init__(self,Id, address, postalcode):
        self.Id=Id
        self.address=address
        self.postalcode=postalcode
        self.incidents=0

class DSmember:   #This class is used in the phase 1 to create the workers.
    def __init__(self, identifier, name, lastname, status,zone):
        self.identifier=identifier
        self.name=name
        self.lastname=lastname
        self.status=status
        self.zone=zone
        self.orders=classDoubleLinkedLists.DoublyLinkedList()
        
class Zone:   #This class is used in the phase 2 to create the different zones.
    def __init__(self, Id):
        self.Id=Id
        self.workers=classDoubleLinkedLists.DoublyLinkedList()

class worker:  #This class is used in the phase 2 to create the workers.
    def __init__(self,identifier,  name, lastname):
        self.identifier=identifier
        self.name=name
        self.lastname=lastname
        
class point:   #This class is used in the phase 3 to create the points (locations) of the graph.
    def __init__(self, street, number, postalcode):
        self.stree=street
        self.number=self.numer
        self.postalcode=postalcode
        
        
        
        