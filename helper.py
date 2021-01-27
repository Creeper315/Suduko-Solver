import numpy as np


def getCluster(data, position=None, cluster_number=None, return_index = False):
    row = []
    col = []
    c_num = cluster_number
    if c_num == None and position == None:
        print('Missing argument, one of "position" or "cluster_number" is required')
        return
    elif c_num != None and position != None:
        print('Only one of "position" or "cluster_number" is required')
        return
    elif c_num == None:
        if position[0] <= 2:
            if position[1] <=2:
                c_num=1
            elif position[1] <=5:
                c_num=2
            elif position[1] <= 8:
                c_num=3
        elif position[0] <= 5:
            if position[1] <=2:
                c_num=4
            elif position[1] <=5:
                c_num=5
            elif position[1] <= 8:
                c_num=6
        elif position[0] <= 8:
            if position[1] <=2:
                c_num=7
            elif position[1] <=5:
                c_num=8
            elif position[1] <= 8:
                c_num=9

    if c_num==1:
        row = [0,0,0,1,1,1,2,2,2]
        col = [0,1,2,0,1,2,0,1,2]
    if c_num==2:
        row = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        col = [3,4,5,3,4,5,3,4,5]
    if c_num==3:
        row = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        col = [6,7,8,6,7,8,6,7,8]
    if c_num==4:
        row = [3,3,3,4,4,4,5,5,5]
        col = [0,1,2,0,1,2,0,1,2]
    if c_num==5:
        row = [3,3,3,4,4,4,5,5,5]
        col = [3,4,5,3,4,5,3,4,5]
    if c_num==6:
        row = [3,3,3,4,4,4,5,5,5]
        col = [6,7,8,6,7,8,6,7,8]
    if c_num==7:
        row = [6,6,6,7,7,7,8,8,8]
        col = [0,1,2,0,1,2,0,1,2]
    if c_num==8:
        row = [6,6,6,7,7,7,8,8,8]
        col = [3,4,5,3,4,5,3,4,5]
    if c_num==9:
        row = [6,6,6,7,7,7,8,8,8]
        col = [6,7,8,6,7,8,6,7,8]
    if return_index==False:
        return data[(np.array(row, dtype=int), np.array(col, dtype=int))]
    else:
        return (np.array(row), np.array(col))

def get_list_of_possible_value(data, position):
    i = position[0]
    j = position[1]

    a = np.concatenate((data[i], data[:,j], getCluster(data, [i,j])))
    a = np.unique(a)
    b = np.array([1,2,3,4,5,6,7,8,9])
    available = [i for i in b if i not in a]
    return np.array(available)

def give_empty_elements_list(data):
    data_copy = data.copy()
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] == 0:
                data_copy[i,j] = get_list_of_possible_value(data, [i,j])
    return data_copy

def get_index_with_least_available_value(data, S):
    smallest = np.inf
    idx_smallest = None
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if type(data[i,j]) is np.ndarray and not S.contain([i,j]):
                if len(data[i,j]) < smallest:
                    smallest = len(data[i,j])
                    idx_smallest = [i,j]
    if idx_smallest == None:
        print('What the heck ?')
    return idx_smallest

def update_empty_elements_after_filling_one(data, position, val):
    this_list = data[position[0], position[1]]
    for i in range(data.shape[0]): # fow a col
        d = data[i,position[1]]
        if (type(d) is np.ndarray) :
            data[i,position[1]] = d[d!=val]

    for j in range(data.shape[1]): # for a row
        d = data[position[0], j]
        if (type(d) is np.ndarray) :
            data[position[0], j] = d[d!=val]

    cluster_idx = getCluster(data, position, return_index=True)
    cluster = data[cluster_idx]
    for i in range(len(cluster)):
        d = cluster[i]
        if type(d) is np.ndarray:
            cluster[i] = d[d!=val]
    data[cluster_idx] = cluster
    data[position[0], position[1]] = this_list # Because when we remove val from these elements, we would remove val from the original one...

    return data  # Is this return necessary

def check_all_element_have_nonzero_available_value(data):
    # If some element has zero available values, return False !
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if type(data[i, j]) is np.ndarray:
                if len(data[i,j]) == 0:
                    return False
    return True

def check_input_data_is_valid(data): # Check if input data has no duplicate value in row, col, cluster
    # for every row:
    for i in range(data.shape[0]):
        r = data[i]
        r = r[r!=0]
        if not len(set(r)) == len(r):
            return False
    for j in range(data.shape[1]):
        c = data[:,j]
        c = c[c!=0]
        if not len(set(c)) == len(c):
            return False
    for k in range(9):
        c = getCluster(data, cluster_number=k)
        c = c[c!=0]
        if not len(set(c)) == len(c):
            return False
    return True


def output_result(data):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            k = data[i, j]
            if type(k) is np.ndarray:
                data[i, j] = k[0]
    return data