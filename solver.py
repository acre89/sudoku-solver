import numpy as np

def split_into_subarrays(array, subarray_shape):
    rows, cols = array.shape
    subrows, subcols = subarray_shape
    return (array.reshape(rows // subrows, subrows, -1, subcols)
            .swapaxes(1, 2)
            .reshape(-1, subrows, subcols))

# Split en sous-tableaux de 3x3

def del_in_sub(sub, li):
    ret_li = []
    for el in li:
        if el not in sub:
            ret_li.append(el)
    if len(ret_li) == 0:
        ret_li.append(0)
    return ret_li
    
def solver(entry_grille):
    finished = False
    while not finished:
        print(entry_grille)
        subarrays = split_into_subarrays(entry_grille, (3, 3))
        finished = True
        for i in range(9):
            for j in range(9):
                if entry_grille[i][j] == 0:
                    finished = False
                    pos_liste = [num for num in range(1,10)]
                    #CHECK LIGNE
                    for ligne in range(9):
                        if entry_grille[i][ligne] != 0:
                            if entry_grille[i][ligne] in pos_liste:
                                pos_liste.pop(pos_liste.index(entry_grille[i][ligne]))

                    
                    if len(pos_liste) > 1:
                        #CHECK COLONNE
                        for col in range(9):
                            if entry_grille[col][j] != 0:
                                if entry_grille[col][j] in pos_liste:
                                    pos_liste.pop(pos_liste.index(entry_grille[col][j]))

                        
                        if len(pos_liste) > 1:
                            #CHECK SUBARRAY
                            sub = 0 
                            if i//3 == 1:
                                sub += 3
                            if i//3 == 2:
                                sub += 6
                            sub += j//3
                            pos_liste = del_in_sub(subarrays[sub], pos_liste)
                            if len(pos_liste) == 1:
                                entry_grille[i][j] = pos_liste[0]
                                
                            else: 
                                if i > 0:
                                    sub_i = int((i-0.05)//3)
                                else: 
                                    sub_i = 0
                                if j > 0:
                                    sub_j = int((j-0.05)//3)
                                else:
                                    sub_j = 0                            
                                rows = []
                                cols = []
                                zeros = []
                                for k in range(3):
                                    rows.append(sub_i*3 + k)
                                    cols.append(sub_j*3 + k)
                                for row in rows:
                                    for col in cols:
                                        if row == i and col == j:
                                            pass
                                        else:
                                            if entry_grille[row][col] == 0:   
                                                zeros.append([row, col])
                                
                                for el in pos_liste:
                                    somme = 0
                                    for zero in zeros:
                                        if el in entry_grille[zero[0]]:
                                            somme += 1 
                                        for col_in in range(9):
                                            if entry_grille[col_in][zero[1]] == el:
                                                somme +=1
                                    if somme == len(zeros):
                                        entry_grille[i][j] = el         
                        else:
                            if len(pos_liste) == 1:
                                entry_grille[i][j] = pos_liste[0]             
                    else:    
                            if len(pos_liste) == 1:
                                entry_grille[i][j] = pos_liste[0]
    return entry_grille


liste = [[1,2,3],[4,5,6],[7,8,9]]
grille =np.array(liste)

     
                        

