# https://www.hackerrank.com/challenges/the-quickest-way-up

from collections import defaultdict

#the graph is an graph where 99 points to 100
#the ladder start points to ladder end
#the snake end points to snake start
graph = defaultdict(list)

n = int(input())
num_ladders = int(input())

for i in range(num_ladders):
    start_lad, end_lad = [int(x) for x in input().split()]
    graph[start_lad].append(end_lad)



num_snakes = int(input())
for j in range(num_snakes):
    start_snake, end_snake = [int(x) for x in input().split()]
    graph[end_snake].append(start_snake)

    
#for i in range(1,100,1):
#    if not graph[i]:
#        graph[i].append(i + 1)

        
#Run DP 
for i in range(n):
    #base case 
    MAX_DIST = 100
    dist = dict()
    dist[100] = 0

    #DP

    #x run from 99 to 1

    for x in range(99,0,-1):
        min_next_six =  1 + min(
                        dist.get(x + 1,MAX_DIST),
                        dist.get(x + 2,MAX_DIST),
                        dist.get(x + 3,MAX_DIST),
                        dist.get(x + 4,MAX_DIST),
                        dist.get(x + 5,MAX_DIST),
                        dist.get(x + 6,MAX_DIST),
                        )

        #double analysis REDO
        neighbors_snake_ladder = graph.get(x)

        #LATER: FIND HOW TO DO THIS IN LAMBDA   
        min_neighbor  = MAX_DIST
        if neighbors_snake_ladder != None:
            for neighbor in neighbors_snake_ladder:
                min_neighbor = min(min_neighbor, dist.get(neighbor, MAX_DIST))    
        



        min_dist = min(min_neighbor, min_next_six)

        dist[x] = min_dist
        print("distance of {} is {}".format(x, dist[x]))

    print(dist[1])



 