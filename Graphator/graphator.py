import bellman, csv

while(True):
    cmd = input().split(" ")
    if(cmd[0]=="help"):
        print("How to use graphator : 'command' 'file' 'algorithm' 'arguments'\n")
    elif(cmd[0]=="solve"):
        matrix = []
        results = []
        with open (cmd[1], newline='') as matrix_file:
            matrix_reader = csv.reader(matrix_file, delimiter=',')
            for row in matrix_reader :
                matrix.append(row)
            for index in range(0, len(matrix)):
                matrix[index] = list(map(float,matrix[index]))
            if(cmd[2]=="bellman_min"):
                results = bellman.bellman_min(matrix, int(cmd[3]))
            elif(cmd[2]=="bellman_max"):
                results = bellman.bellman_max(matrix, int(cmd[3]))
            elif(cmd[2]=="bellman_ford_kalaba"):
                results = bellman.bellman_ford_kalaba(matrix, int(cmd[3]))
        print("Results : {}".format(results))
    elif(cmd[0]=="exit"):
        break

