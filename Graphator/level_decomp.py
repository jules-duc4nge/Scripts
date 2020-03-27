def level_decomposition(graph):
    no_tops=len(graph)
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
    return levels