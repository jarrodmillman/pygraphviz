#!/usr/bin/env python
"""
Draw the graph of cities from miles.dat.
An example that shows how to add your own positions to nodes
and have graphviz neato draw the edges.

miles_graph() returns an undirected graph over the 128 US cities from
the datafile miles.dat.  

This example is described in Section 1.1 in Knuth's book [1,2].

References.
-----------

[1] Donald E. Knuth,
    "The Stanford GraphBase: A Platform for Combinatorial Computing",
    ACM Press, New York, 1993.
[2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html


"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
#    Copyright (C) 2006 by 
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Manos Renieris, http://www.cs.brown.edu/~er/
#    Distributed with BSD license.     
#    All rights reserved, see LICENSE for details.


def miles_graph():
    """ Return the example graph in miles.dat from the Stanford GraphBase.

    Edges are made between cities that are less then 300 miles apart.

    """
    import math
    import re

    try:
        fh=open("miles.dat","r")
    except IOError:
        print "miles.dat not found"
        raise

    G=AGraph(name='miles.dat')
    G.node_attr['shape']='circle'
    G.node_attr['fixedsize']='true'
    G.node_attr['fontsize']='0.1'
    G.node_attr['style']='filled'
    G.graph_attr['outputorder']='edgesfirst'
    G.graph_attr['label']="Knuth's miles.dat"
    G.graph_attr['ratio']='1.0'
    G.edge_attr['color']='#AA00FF'
    G.edge_attr['style']='setlinewidth(2)'
#    G.graph_attr['splines']='true'
#    G.graph_attr['splines']='true'

    cities=[]
    for line in fh.readlines():
        if line.startswith("*"): # skip comments
            continue

        numfind=re.compile("^\d+") 

        if numfind.match(line): # this line is distances
            dist=line.split()
            for d in dist:
                if float(d) < 300: # connect if closer then 300 miles
                    G.add_edge(city,cities[i])
                i=i+1
        else: # this line is a city, position, population
            i=1
            (city,coordpop)=line.split("[")
            cities.insert(0,city)
            (coord,pop)=coordpop.split("]")
            (y,x)=coord.split(",")
            G.add_node(city)
            n=G.get_node(city)
            # assign positions, scale to be something reasonable in points
            n.attr['pos']="%f,%f)"%(-(float(x)-7000)/10.0,(float(y)-2000)/10.0)
            # assign node size, in sqrt of 1,000,000's of people 
            d=math.sqrt(float(pop)/1000000.0)
            n.attr['height']="%s"%d
            n.attr['width']="%s"%d
            # assign node color
            n.attr['fillcolor']="#0000%2x"%(int(d*256))
            # we don't need no labels
            n.attr['label']=' '


    return G            

if __name__ == '__main__':
    from pygraphviz import *

    G=miles_graph()

    print "Loaded Donald Knuth's miles.dat containing 128 cities."
   
    G.string()
    G.write("miles.dot")
    print "Wrote miles.dot"
    G.draw("miles.png",prog='neato',args='-n2')
    print "Wrote miles.png"
