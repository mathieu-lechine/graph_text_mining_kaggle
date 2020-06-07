import numpy as np
import networkx as nx
import csv
import os
from sets import Set

with open("training_set.txt", "r") as f:
    reader = csv.reader(f)
    training_set  = list(reader)
training_set = [element[0].split(" ") for element in training_set]

with open("testing_set.txt", "r") as f:
    reader = csv.reader(f)
    testing_set  = list(reader)
testing_set = [element[0].split(" ") for element in testing_set]

with open("node_information.csv", "r") as f:
    reader = csv.reader(f)
    node_info  = list(reader)
IDs = [element[0] for element in node_info]

couple_article = [ [id1,id2] for id1, id2, edge in training_set if int(edge) ==1 ] 
list_couple_article_without_edge = [ [id1,id2] for id1, id2, edge in training_set if int(edge) ==0 ] 


#Build the graph
G = nx.DiGraph() #Graphe d'article
#add all nodes
G.add_nodes_from(IDs)
#add all edges
G.add_edges_from(couple_article)
print 'Number of nodes:', G.number_of_nodes() 
print 'Number of edges:', G.number_of_edges() 

#Local connectivity
from networkx.algorithms.connectivity import local_edge_connectivity
from networkx.algorithms.connectivity import local_node_connectivity
from networkx.algorithms import approximation as approx

print "local_node_connectivity for training set"
list_local_node_connectivity_train = []
compt=0
for id1, id2, edge in training_set:
    if compt % 50000 == 0:
        print compt
    compt += 1
    local_con = approx.local_node_connectivity(G,id1,id2)
    list_local_node_connectivity_train.append([id1,id2,local_con])
    
with open("training_local_node_connectivity.csv", "w") as f:
    for row in list_local_node_connectivity_train:
        f.write(row[0])
        f.write(",")
        f.write(row[1])
        f.write(",")
        f.write(str(row[2]))
        f.write("\n")
        
        
print "local_node_connectivity for testing set"
list_local_node_connectivity_test = []
compt=0
for id1, id2 in testing_set:
    if compt % 10000 == 0:
        print compt
    compt += 1
    local_con = approx.local_node_connectivity(G,id1,id2)
    list_local_node_connectivity_test.append([id1,id2,local_con])
    
with open("testing_local_node_connectivity.csv", "w") as f:
    for row in list_local_node_connectivity_test:
        f.write(row[0])
        f.write(",")
        f.write(row[1])
        f.write(",")
        f.write(str(row[2]))
        f.write("\n")