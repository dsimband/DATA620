#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:36:37 2022

@author: davidsimbandumwe
"""

import tweepy
import random
import pandas as pd





########################################################
#
#   function add user to to list and edge to dataframe
#
#########################################################

def add_user(u, r, n):
    
   
    lst = [u.id,
             u.name,
             u.friends_count,
             u.followers_count,
             u.created_at,
             u.location,
             u.description,
             #random.choices(u.follower_ids(), k=10),
             user.followers()
             ]
    
    r.append(lst)
    
    f_lst = u.follower_ids()
    
    if (len(f_lst) > 10):
        f_lst = random.choices(f_lst, k=10)
        
    for x in f_lst:
        #print(x)
        n = n.append({'id':u.id, 'follower':x }, ignore_index=True)
    
    
    return r,n


########################################################
#
#   function write graph
#
#########################################################



def save_graph(df):
    
    #import networkx as nx
    import matplotlib.pyplot as plt
    #from networkx import algorithms 
    from neo4j import GraphDatabase
    import nxneo4j as neo
    
    
    # Establish connection
    driver = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","AllAcd12"))


    # Initialize graph
    g_neo = neo.Graph(driver)
    
      
    # clean-up graph
    #g_neo.delete_all()
    
    #g_neo.
    
    
    
    
    # Close connection
    driver.close()













# authenticate to twitter and access the user associated with the credentials
auth = tweepy.OAuth2BearerHandler('AAAAAAAAAAAAAAAAAAAAAEQnZgEAAAAAX9TsuDwvnbgMmKlFn%2BYAS05znng%3DFXYgB4FE0QXKlnuXEOx2MNmKZSwFC8GVl3DrqfCGN4VHHHX8lH')


api = tweepy.API(auth)
user = api.get_user(screen_name='broncos')



# initialize return variables
df_edge = pd.DataFrame({'id': pd.Series(dtype='int'),
                    'follower': pd.Series(dtype='int')})
restLst = []



# add initial node
restLst, df_edge = add_user(user,restLst, df_edge)    



# call the create add_user for each 
usersResult = user.followers()
length = len(usersResult)

for i in range(length):
    print(i)
    restLst, df_edge = add_user(usersResult[i],restLst, df_edge)









save_graph(df_edge)










