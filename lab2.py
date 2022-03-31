# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 08:14:43 2022

@author: garci
"""

"""
===============================================
    LAB 2 -> GUILLEM GARCIA I MARTÍ LLINÉS
===============================================
    TASK 1 -> DO CONTACTS SHARE TASTES? 
===============================================
"""
import networkx as nx
import random as r
import matplotlib.pyplot as plt

def monitor_interests(G):
    list_weight_0 = []
    list_not_0 = []
    
    edges = G.edges.data()
    for values in edges:
        weight = values[2]
        if weight["weight"] == 0:
            nodes = (values[0], values[1])
            list_weight_0.append(nodes)
        else:
            nodes = (values[0], values[1])
            list_not_0.append(nodes)
    
    for x in list_weight_0:
        G.remove_edge(x[0],x[1])
    
    return G,list_weight_0,list_not_0


#EXAMPLE OF MONITOR_INTERESTS
def example():
    G = nx.Graph() #We construct a new graph
    list_fighters = [] 
    list_nodes = []
    file = open("Smash fighters.txt", "r")#Open a file with 80 fighters (Interests)
    for line in file:
        list_fighters.append(line[:-1]) #Append into a list of fighters
    for x in range(10):
        list_nodes.append(x) #Add each node in a list of nodes
        auxiliar_list = []
        counter = 0
        while counter < 4: #Iterate for the number of interests we want
            fighter = r.choice(list_fighters) #We choose a random fighter
            if fighter not in auxiliar_list: #We remove the repited fighters
                auxiliar_list.append(fighter) 
                counter += 1 
        G.add_node(x, topInterests=auxiliar_list) #We add the node with his interests
        
    for x in range(10):
        weight = 0
        random_node = r.choice(list_nodes) #Choose a random node of the list of nodes
        print("Node:", x)
        print("Node2:", random_node)
        interest_x = G.nodes[x]["topInterests"] #See the interests of first node
        print("Interests node:", interest_x )
        interest_random = G.nodes[random_node]["topInterests"] #See the interest of second node
        print("Interests node2:", interest_random )
        if x != random_node: #If it's not the same node both (We don't want loops)
            for y in interest_x: 
                if y in interest_random:
                    weight += 1 #If interests are the same we increment the weight
            print("Weight:", weight)
            print("\n")
            G.add_edge(x,random_node, weight = weight)
    return G

G = example() #The example graph we didn't remove 0-weight
subax1 = plt.subplot(111)
nx.draw(G, with_labels=True, font_weight='bold')
G2, list1, list2 = monitor_interests(G)
print("Edges with weight 0:", list1)
print("Edges with no 0:", list2)
subax1 = plt.subplot(111)
nx.draw(G2, with_labels=True, font_weight='bold')
