# hackerrank.com BFS Search
# https://www.hackerrank.com/challenges/bfsshortreach

# Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . We define node  to be the starting position for a BFS.

# Given  queries in the form of a graph and some starting node, , perform each query by calculating the shortest distance from starting node  to all the other nodes in the graph. Then print a single line of  space-separated integers listing node 's shortest distance to each of the  other nodes (ordered sequentially by node number); if  is disconnected from a node, print  as the distance to that node.

# Input Format

# The first line contains an integer, , denoting the number of queries. The subsequent lines describe each query in the following format:

# The first line contains two space-separated integers describing the respective values of  (the number of nodes) and  (the number of edges) in the graph.
# Each line  of the  subsequent lines contains two space-separated integers,  and , describing an edge connecting node  to node .
# The last line contains a single integer, , denoting the index of the starting node.
# Constraints

# Output Format

# For each of the  queries, print a single line of  space-separated integers denoting the shortest distances to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), but should not include node . If some node is unreachable from , print  as the distance to that node.


query = int(input())
length = 6


for qu in range(query):
    num_nodes, num_edges = [int(a) for a in input().split()]
    graph = dict()
    
    
    #create graph
    for j in range(num_edges):
        node1, node2 = [int(a) for a in input().split()]
        a = graph.get(node1,[])
        a.append(node2)
        graph[node1] = a
        
        b = graph.get(node2,[])
        b.append(node1)
        graph[node2] = b
    start = int(input())
    queue = list()
    seen = set()
    dist = [0 for i in range(num_nodes)]
    #BFS
    queue.append(start)
    while (len(queue) != 0):
        curr_node = queue.pop(0)
        neighbors = graph.get(curr_node,[])
        for neighbor in neighbors:
            if dist[neighbor-1] == 0:
                dist[neighbor-1] = dist[curr_node-1] + length
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)

    dist.pop(start-1)
    
    for i in range(len(dist)):
        if dist[i] == 0:
            dist[i] = -1
    print(" ".join([str(x) for x in dist]))