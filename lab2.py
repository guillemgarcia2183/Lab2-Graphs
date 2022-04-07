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
import examples as ex

def monitor_interests(G):
    nodes_of_G = G.nodes()
    edges_graph = G.edges()
    new_graph = nx.Graph()
    new_graph.add_nodes_from(nodes_of_G)
    for i,edge in enumerate(edges_graph):
        weight = 0
        print("In node" + " " + str(i) + ":")
        interest_1 = G.nodes[edge[0]]["topInterests"]
        interest_2 = G.nodes[edge[1]]["topInterests"]
        print("Interest1:", interest_1)
        print("Interest2:", interest_2)

        if edge[0] != edge[1]:
            for x in interest_1:
                if x in interest_2:
                    weight += 1

            if weight != 0:
                    new_graph.add_edge(edge[0],edge[1], weight = weight)
        
        print("Weight:", weight)
        print("")
        
    #print("Initial edges:\n", edges_graph)
    #print("")
    #print("Final edges:\n", new_graph.edges())   
    return new_graph

#EXAMPLE PRINCIPAL PROGRAM OF TASK 1
"""
G = ex.example_monitor_interest() 
G2 = monitor_interests(G)
subax1 = plt.subplot(111)
nx.draw(G2, with_labels=True, font_weight='bold')
"""

"""
===============================================
    TASK 2 -> THE LUCKY DRAW
===============================================

Tetrahedron: 4-sided dice
Cube: 6-sided dice
Octahedron: 8-sided dice
Dodecahedron: 12-sided dice
Icosahedron: 20-sided dice

for n throws:
    
Tetrahedron throw: maximum value, n*4; minimum value, n; number of different numbers: n*4-n-1
Cube throw: maximum value, n*6; minimum value, n; number of different numbers: n*6-n-1
Octahedron throw: maximum value, n*8; minimum value, n; number of different numbers: n*8-n-1
Dodecahedron throw: maximum value, n*12; minimum value, n; number of different numbers: n*12-n-1
Icosahedron throw: maximum value, n*20; minimum value, n; number of different numbers: n*20-n-1
"""

def lucky_draw(n):
    """
    INPUT
    n : number of throws a player has.
    ----------
    OUTPUT
    ----------
    list[list]: a list of lists where every element of the main list is n, ···, n+9 
    throws of one dice
    """

    # Initialize a list of lists. It has 5 lists inside for each dice possible
    final_list = [[] for x in range(5)] 
    
    # Lists of the possible results that can be obtained. The first element of each list 
    # belongs to n throws, the second one to n+1 throws, until n+9 throws.
    for m in range(n, n+9):
        final_list[0].append(m*4-m-1)
        final_list[1].append(m*6-m-1)
        final_list[2].append(m*8-m-1)
        final_list[3].append(m*12-m-1)
        final_list[4].append(m*20-m-1)

    return final_list
# ======== second part of task 2 ========
def one_thousand_participants(n,k,v):
    number_of_winners=0
    for participants in range(1000):
        value=0
        for throws in range(n):
            value+=r.randint(1, k)
        if value>v:
            number_of_winners+=1
    return number_of_winners
