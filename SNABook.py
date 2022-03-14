# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import networkx as nx



g = nx.generators.small.krackhardt_kite_graph() 
num_nodes = g.number_of_nodes()
num_edges = g.number_of_edges()
