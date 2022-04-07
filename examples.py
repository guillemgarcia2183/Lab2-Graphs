# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 09:11:23 2022

@author: garci
"""

"""
===============================================
    LAB 2 -> GUILLEM GARCIA I MARTÍ LLINÉS
===============================================
    EXAMPLE 1 -> DO CONTACTS SHARE TASTES? 
===============================================
"""
import networkx as nx
import random as r
import matplotlib.pyplot as plt

#EXAMPLE OF MONITOR_INTERESTS
def example_monitor_interest():
    G = nx.Graph() #We construct a new graph
    list_fighters = [] 
    list_nodes = []
    
    list_random_node = []
    for x in range(8):
        list_random_node.append(x)
    
    file = open("Smash fighters.txt", "r")#Open a file with 80 fighters (Interests)
    for line in file:
        list_fighters.append(line[:-1]) #Append into a list of fighters
    
    for x in range(8):
        list_nodes.append(x) #Add each node in a list of nodes
        auxiliar_list = []
        counter = 0
        while counter < 4: #Iterate for the number of interests we want
            fighter = r.choice(list_fighters) #We choose a random fighter
            if fighter not in auxiliar_list: #We remove the repited fighters
                auxiliar_list.append(fighter) 
                counter += 1 
        G.add_node(x, topInterests=auxiliar_list) #We add the node with his interests    
   
    for y in range(8):
        random_node = r.choice(list_random_node)
        G.add_edge(y,random_node)
    
    return G