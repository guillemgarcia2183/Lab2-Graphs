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
    print("Nodes of G:", nodes_of_G)
    print("Edges of G:", edges_graph)
    for i,edge in enumerate(edges_graph):
        weight = 0
        print("In edges" + "(" + str(edge[0]) + "," + str(edge[1]) + ")")
        interest_1 = G.nodes[edge[0]]["topInterests"]
        interest_2 = G.nodes[edge[1]]["topInterests"]
        print("Interest1:", interest_1)
        print("Interest2:", interest_2)
        
        for x in interest_1:
            if x in interest_2:
                weight += 1
       
        G[edge[0]][edge[1]]['weight'] = weight #Add weight to edge

     
        print("Weight:", str(weight))
        print("")
    
        weight2 = G.get_edge_data(edge[0],edge[1])
        if (weight2['weight'] == 0) or (edge[0] == edge[1]): #Remove edge if it's the same or weight is 0
            G.remove_edge(edge[0],edge[1])
        
    return G

#EXAMPLE MAIN PROGRAM OF TASK 1

G = ex.example_monitor_interest() 
plt.title("Example graph")
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

G2 = monitor_interests(G)
plt.title("Monitor interest")
nx.draw(G2, with_labels=True, font_weight='bold')
plt.show()


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

def probability_winning(n,k,v):
    possible_results = []    
    favorable_results = []
    minimum_value = n
    maximum_value = k*n
    
    for value in range(minimum_value,maximum_value+1):
        possible_results.append(value)
    
    print("Possible results:", possible_results, "->", len(possible_results))
    for value in possible_results:
        if value > v:
            favorable_results.append(value)
        
    print("Favorable results:", favorable_results, "->", len(favorable_results))
    
    probability = (len(favorable_results)) / (len(possible_results))
    
    return probability

"""
Report question: Given n, k and v, can you calculate the probability of winning?
n,k,v = 4,6,8
winners = one_thousand_participants(n, k, v)
losers = 1000 - winners
print("Throws:", n)
print("Faces:", k)
print("Value:", v)
print("")
print("Number of winners:", winners, "->", winners*100/1000, "%")
print("Number of Losers:", losers, "->", losers*100/1000, "%")
print("")
print("Probability of winning:", probability_winning(n, k, v)*100, "%")
"""
"""
===============================================
     TASK 3 -> PLANARITY CHECK
===============================================
"""
# First function of task 3
def remove_subdivisions(G):
    returning_graph = nx.Graph.copy(G)
    nodes = list(returning_graph.nodes())
    for node in nodes:
        neighbours = list(nx.neighbors(returning_graph, node))
        if len(neighbours) == 2:
            returning_graph.remove_node(node)
            returning_graph.add_edge(neighbours[0], neighbours[1])
    return returning_graph

# Second function of task 3
def contains_K5(G):
    F = nx.complete_graph(5)
    check = nx.algorithms.isomorphism.GraphMatcher(G, F)
    return check.subgraph_is_isomorphic()

# Third function of task 3
def contains_K33(G):
    k_3_3 = set()
    nodes = list(G.nodes())
    i = 0
    while i < len(nodes):
        neighbours = list(nx.neighbors(G, nodes[i]))
        if len(neighbours) >= 3:
            k_3_3.add(i)
            for neighbour in neighbours:
                if len(list(nx.neighbors(G, neighbour))) >= 3:
                    k_3_3.add(i)
        if len(k_3_3) >= 6:
            i = len(nodes)
        else:
            i += 1
    return len(k_3_3) >= 6
