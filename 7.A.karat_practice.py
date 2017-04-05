
def create_dictionary(lst):
    child_parent = dict()
    
    for parent, child in lst:
        if child_parent.get(child) != None:
            new_parent_l = child_parent.get(child)
            new_parent_l.append(parent)
            child_parent[child] = new_parent_l
        else: 
            child_parent[child] = [parent]     
    return child_parent


def one_parent(dic):
    one_parent = []
    for child in dic:
        if len(dic[child]) == 1:
            one_parent.append(child)
            
    return one_parent


def all_num_present(lst):
    all_child_parent = set()
    for parent, child in lst:
        all_child_parent.add(parent)
        all_child_parent.add(child)
    return all_child_parent

def zero_parent(dic,lst):
    unique_keys = all_num_present(lst)
    for key in dic:
        if key in unique_keys:
            unique_keys.remove(key)
    
    return unique_keys
    

parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9)]

#Create graph here
graph = create_dictionary(parent_child_pairs)

print("testing one parent")
print(one_parent(graph))

print("testing zero parent")
print(zero_parent(graph, parent_child_pairs))


# 
# Your previous Markdown content is preserved below:
# 
# Suppose we have some input data describing relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
# 
# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
#             
#  1   2     4
#   \ /     / \
#    3     5   8
#     \   / \   \
#      \ /   \   9
#       6     7 
# 
# Write a function that takes this data as input and outputs two collections: 
# one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.
# 
# Sample output:
# Zero parents: 1, 2, 4
# One parent: 5, 7, 8, 9
# 
'''
Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one known ancestor.

Sample input and output:
[3, 8] => false
[5, 8] => true
[5, 9] => true


Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for “earliest”, return any one of them. If the input individual has no parents, the function should return null (or -1).

Sample input and output:


8 => 4
7 => 4
6 => 1, 2, or 4

'''
# # Python
parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9)]
# 

def ancestors(graph,first):
    
    ancestors = []
    
    queue = []
    queue.append(first)
    while len(queue) != 0:
        curr = queue.pop(0)    
        if (graph.get(curr) != None):
            parent_l = graph.get(curr)
            for parent in parent_l:
                queue.append(parent)
                ancestors.append(parent)
    return ancestors

print()
print("ancestors of 6")
print(ancestors(graph,6))

def shared_ancestors(graph, first, second):
    first_a = ancestors(graph, first)
    second_a = ancestors(graph, second)
    
    for parent in first_a:
        if parent in second_a:
            return True
    
    return False

print()
print(shared_ancestors(graph, 3, 8))
print(shared_ancestors(graph, 5, 8))
print(shared_ancestors(graph, 5, 9))
                       
def oldest_ancestors(graph,parent_child_pairs, first):
    
    ancestors = []
    count = 0 
    
    if first in zero_parent(graph, parent_child_pairs):
        return null
    
    queue = []
    queue.append((first,count))
    while len(queue) != 0:
        curr_n = queue.pop(0)
        curr = curr_n[0]
        c_count = curr_n[1]
        
        if (graph.get(curr) != None):
            parent_l = graph.get(curr)
            for parent in parent_l:
                queue.append((parent,c_count + 1))
                ancestors.append((parent,c_count + 1))
    
    # print(ancestors)
    parent = None
    max_c = 0
    for key, count in ancestors:
        if count > max_c:
            parent = key
            max_c = count
    return parent

print()
print()
print('oldest')
print(oldest_ancestors(graph, parent_child_pairs, 8))
print(oldest_ancestors(graph, parent_child_pairs, 7))
print(oldest_ancestors(graph, parent_child_pairs, 6))
        
