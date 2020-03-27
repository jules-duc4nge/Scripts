import level_decomp
def bellman_min(graph,first_top):
    levels = level_decomp.level_decomposition(graph)
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

    return distance

def bellman_max(graph, first_top):
    levels = level_decomp.level_decomposition(graph)
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

    return distance

def bellman_ford_kalaba(graph, first_top):
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
    return distance
