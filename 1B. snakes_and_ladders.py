# https://www.hackerrank.com/challenges/the-quickest-way-up

from collections import defaultdict

#the graph is an graph where 99 points to 100
#the ladder start points to ladder end
#the snake end points to snake start


n = int(input())
for i in range(n):
    graph = dict()
    num_ladders = int(input())

    for i in range(num_ladders):
        start_lad, end_lad = [int(x) for x in input().split()]
        graph[start_lad] = end_lad



    num_snakes = int(input())
    for j in range(num_snakes):
        end_snake, start_snake = [int(x) for x in input().split()]
        graph[end_snake] = start_snake

    #DO BFS
    queue = []
    length = dict()
    seen = set()


    queue.append(1)
    length[1] = 0
    seen.add(1)
    

    while len(queue) != 0:
        curr = queue.pop(0)
      #  print("popping {} from the queue".format(curr))
        if graph.get(curr) != None:
            ladder = graph.get(curr)
            #print("moving from : {} to {}".format(curr,ladder))
            length[ladder] = length[curr]
            curr = ladder
            

        curr_neigh = [curr + x for x in range(1,7,1) if curr + x <= 100]
        if len(curr_neigh) != 0:
            for nb in curr_neigh:
                if nb not in seen:
                    queue.append(nb)
                    if length.get(nb) == None:
                        length[nb] = length.get(curr) + 1
                 #   print("length of {} is {}".format(nb,length[nb]))
                    seen.add(nb)
                    if nb ==100:
                        break

    print(length.get(100,-1))
      
        
        



 