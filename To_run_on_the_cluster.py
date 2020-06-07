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

def Create_2_new_features_list_from_dict_node(dict_node,training_set):
    list_res = []
    for el  in training_set:
        id1 = el[0]
        id2 = el[1]
        new_feature1 = dict_node[id1]
        new_feature2 = dict_node[id2]
        list_res.append([id1,id2,new_feature1,new_feature2])
    return list_res

def Create_file_2_new_features(filename, list_feature):
    with open(filename, "w") as f:
        for row in list_feature:
            f.write(row[0])
            f.write(",")
            f.write(row[1])
            f.write(",")
            f.write(str(row[2]))
            f.write(",")
            f.write(str(row[3]))
            f.write("\n")
            
dict_betweenness_centrality = nx.betweenness_centrality(G)
dict_node = dict_betweenness_centrality
filename = "training_betweenness_centrality.csv"
list_feature = Create_2_new_features_list_from_dict_node(dict_node,training_set)
Create_file_2_new_features(filename, list_feature)

filename = "testing_betweenness_centrality.csv"
list_feature = Create_2_new_features_list_from_dict_node(dict_node,testing_set)
Create_file_2_new_features(filename, list_feature)
 