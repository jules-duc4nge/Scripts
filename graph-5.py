"""
graph=[
    #       1           2               3              4            5             6             7             8
    [ float('Inf'),     6       , float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 1
    [ float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 2
    [ float('Inf'),     9       , float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 3
    [ float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'),       10    , float('Inf') ], # 4
    [       6     ,     4       , float('Inf'), float('Inf'), float('Inf'), float('Inf'),       -1    , float('Inf') ], # 5
    [ float('Inf'), float('Inf'), float('Inf'),     2       ,       5     , float('Inf'), float('Inf'),     8        ], # 6
    [ float('Inf'),     1       ,       14    , float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 7
    [       4     , float('Inf'), float('Inf'),     5       , float('Inf'), float('Inf'), float('Inf'), float('Inf') ] # 8
]
"""

graph=[
    #       1           2               3              4            5             6             7             8
    [ float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'),     4        ], # 1
    [       2     , float('Inf'), float('Inf'),     3       , float('Inf'), float('Inf'),       2     , float('Inf') ], # 2
    [ float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 3
    [ float('Inf'), float('Inf'),       1     , float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 4
    [       2     , float('Inf'), float('Inf'), float('Inf'), float('Inf'),     3       , float('Inf'), float('Inf') ], # 5
    [ float('Inf'),     7       , float('Inf'),     1       , float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 6
    [       1     , float('Inf'),       3     , float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf') ], # 7
    [ float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'), float('Inf'),       2     , float('Inf') ] # 8
]

def level_decomposition(graph,no_tops):
    levels = [0]*no_tops
    degree = [0]*no_tops
    not_marked_top = []
    marked_top = []
    successor = []
    # Remplissage des degrés
    for i in range(0,no_tops):
        for j in range(0,no_tops):
            if(graph[i][j] != float('Inf')):
                degree[j]+=1

    # Remplissage de L
    for i in range(0,no_tops):
        if (degree[i]==0) and (i not in marked_top) :
            not_marked_top.append(i)


    while(len(not_marked_top)>0): # Pour chaque x
        # not_marked_top[0] -> x
        # successor[0] -> y

        # Remplissage des successeurs
        for i in range(0,no_tops):
            if graph[not_marked_top[0]][i] != float('Inf'):
                successor.append(i)
        
        while(len(successor)>0): # Pour chaque y
            if levels[successor[0]]<levels[not_marked_top[0]]+1 :
                levels[successor[0]]=levels[not_marked_top[0]]+1
            degree[successor[0]]-=1
            successor.pop(0)

        # Mise à jour des marques
        marked_top.append(not_marked_top[0])
        not_marked_top.pop(0)

        # Remplissage de L
        for i in range(0,no_tops):
            if (degree[i]==0) and (i not in marked_top) :
                not_marked_top.append(i)
    print(levels)
    return levels

def bellman_min(graph, levels, first_top):
    no_tops=len(levels)
    level_list = list(dict.fromkeys(levels))
    level_list.sort()

    y = []
    x = []

    # Initialisation de Pred
    predecessor = [0]*no_tops

    # Initialisation de Dist
    distance = [float('Inf')]*no_tops
    distance[first_top-1]=0

    for k in level_list :
        # y[0] -> y
        #x[0] -> x
        for i in range(0,len(levels)):
            if levels[i] == k+1 :
                y.append(i)
        while len(y)>0:
            # Remplissage des prédécesseurs
            for i in range(0,no_tops):
                if graph[i][y[0]] != float('Inf'):
                    x.append(i)
            
            while len(x)>0:
                if (distance[x[0]]+graph[x[0]][y[0]]) < distance[y[0]] :
                    distance[y[0]]=(distance[x[0]]+graph[x[0]][y[0]])
                    predecessor[y[0]]=x[0]
                x.pop(0)
            y.pop(0)

    print(distance)

def bellman_max(graph, levels, first_top):
    no_tops=len(levels)
    level_list = list(dict.fromkeys(levels))
    level_list.sort()

    y = []
    x = []

    # Initialisation de Pred
    predecessor = [0]*no_tops

    # Initialisation de Dist
    distance = [float('Inf')]*no_tops
    distance[first_top-1]=0

    for k in level_list :
        # y[0] -> y
        #x[0] -> x
        for i in range(0,len(levels)):
            if levels[i] == k+1 :
                y.append(i)
        while len(y)>0:
            # Remplissage des prédécesseurs
            for i in range(0,no_tops):
                if graph[i][y[0]] != float('Inf'):
                    x.append(i)
            
            while len(x)>0:
                if distance[y[0]] == float('Inf') : 
                    distance[y[0]]=(distance[x[0]]+graph[x[0]][y[0]])
                    predecessor[y[0]]=x[0]
                elif ((distance[x[0]]+graph[x[0]][y[0]]) > distance[y[0]]) and (distance[x[0]] != float('Inf')) :
                    distance[y[0]]=(distance[x[0]]+graph[x[0]][y[0]])
                    predecessor[y[0]]=x[0]
                x.pop(0)
            y.pop(0)

    print(distance)

def bellman_ford_kalaba(graphe, first_top):
    no_tops=len(graph)
    y = []
    x = []

    # Initialisation de Pred
    predecessor = [0]*no_tops

    # Initialisation de Dist
    distance = [float('Inf')]*no_tops
    distance[first_top-1]=0

    k = 1
    modified = True
    while (k<=len(graph)) and modified :
        # y[0] -> y
        # x[0] -> x

        modified = False
        for i in range(0,len(distance)):
            if distance[i]!=float('Inf') :
                x.append(i)

        while(len(x)>0):
            for i in range(0,no_tops):
                if graph[x[0]][i] != float('Inf'):
                    y.append(i)

            while(len(y)>0):
                if (distance[x[0]]+graph[x[0]][y[0]])<distance[y[0]] :
                    distance[y[0]]=(distance[x[0]]+graph[x[0]][y[0]])
                    predecessor[y[0]]=x[0]
                    modified=True
                y.pop(0)
            x.pop(0)
        k+=1
    print(distance)



bellman_ford_kalaba(graph, 1)

#bellman_min(graph, level_decomposition(graph, 8),5)
#bellman_max(graph, level_decomposition(graph, 8),5)