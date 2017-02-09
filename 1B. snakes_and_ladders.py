# https://www.hackerrank.com/challenges/the-quickest-way-up

from collections import defaultdict

#the graph is an graph where 99 points to 100
#the ladder start points to ladder end
#the snake end points to snake start
graph = dict()

n = int(input())
for i in range(n):
    num_ladders = int(input())

    for i in range(num_ladders):
        start_lad, end_lad = [int(x) for x in input().split()]
        graph[start_lad] = end_lad



    num_snakes = int(input())
    for j in range(num_snakes):
        start_snake, end_snake = [int(x) for x in input().split()]
        graph[end_snake] = start_snake

    #DO BFS
    queue = []
    length = dict()
    seen = set()


    queue.append(1)
    length[1] = 0
    seen.add(1)
    
    print()
    print()
    
    while len(queue) != 0:
        curr = queue.pop(0)

        if graph.get(curr) != None:
            ladder = graph.get(curr)
            print("moving from : {} to {}".format(curr,ladder))
            length[ladder] = length[curr]
            curr = ladder
            

        curr_neigh = [curr + x for x in range(1,7,1) if curr + x <= 100]

        for nb in curr_neigh:
            if nb not in seen:
                queue.append(nb)
                length[nb] = length.get(curr) + 1
                print("length of {} is {}".format(nb,length[nb]))
                seen.add(nb)

    print(length[100])
      
        
        



 