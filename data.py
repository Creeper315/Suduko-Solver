import numpy as np


data = np.ndarray([9,9], dtype=object)    # Important to put "dtype=object" here

def data1():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([0,0,0,0,0,0,0,0,0])
    data[1] = np.array([0,0,0,0,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,0,0,0,0])
    data[3] = np.array([0,0,0,0,0,0,0,0,0])
    data[4] = np.array([0,0,0,0,0,0,0,0,0])
    data[5] = np.array([0,0,0,0,0,0,0,0,0])
    data[6] = np.array([0,0,0,0,0,0,0,0,0])
    data[7] = np.array([0,0,0,0,0,0,0,0,0])
    data[8] = np.array([0,0,0,0,0,0,0,0,0])
    return data

def data2():
    data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [4, 5, 6, 7, 8, 9, 1, 2, 3],
                     [7, 8, 9, 1, 2, 3, 4, 5, 6],
                     [2, 3, 1, 6, 7, 4, 8, 9, 5],
                     [8, 7, 5, 9, 1, 2, 3, 6, 4],
                     [6, 9, 4, 5, 3, 8, 2, 1, 7],
                     [3, 1 ,7 ,2 ,6 ,5 ,9 ,4 ,8],
                     [5, 4, 2, 8, 9, 7, 6, 3, 1],
                     [9, 6, 8, 3, 4, 1, 5, 7, 2]], dtype=object)
    return data

def data3():
    data[0] = np.array([8,0,0,0,0,0,2,7,4])
    data[1] = np.array([6,0,9,0,4,0,1,0,0])
    data[2] = np.array([1,2,0,0,0,0,0,6,0])
    data[3] = np.array([0,0,0,4,7,2,0,0,0])
    data[4] = np.array([0,4,0,1,0,8,0,5,0])
    data[5] = np.array([0,0,0,3,5,9,0,0,0])
    data[6] = np.array([0,8,0,0,0,0,0,4,3])
    data[7] = np.array([0,0,5,0,2,0,7,0,6])
    data[8] = np.array([4,1,7,0,0,0,0,0,5])
    return data

def data4():
    data[0] = np.array([8,0,0,0,0,0,0,0,0])
    data[1] = np.array([0,0,3,6,0,0,2,0,0])
    data[2] = np.array([0,7,0,0,9,0,0,0,0])
    data[3] = np.array([0,5,0,0,0,7,0,0,0])
    data[4] = np.array([0,0,0,0,4,5,7,0,0])
    data[5] = np.array([0,0,0,1,0,0,0,3,0])
    data[6] = np.array([0,0,1,0,0,0,0,6,8])
    data[7] = np.array([0,0,8,5,0,0,0,1,0])
    data[8] = np.array([0,9,0,0,0,0,4,0,0])
    return data

def data5():
    data[0] = np.array([0, 0, 5, 3, 0, 0, 0, 0, 0])
    data[1] = np.array([8, 0, 0, 0, 0, 0, 0, 2, 0])
    data[2] = np.array([0, 7, 0, 0, 1, 0, 5, 0, 0])
    data[3] = np.array([4, 0, 0, 0, 0, 5, 3, 0, 0])
    data[4] = np.array([0, 1, 0, 0, 7, 0, 0, 0, 6])
    data[5] = np.array([0, 0, 3, 2, 0, 0, 0, 8, 0])
    data[6] = np.array([0, 6, 0, 5, 0, 0, 0, 0, 9])
    data[7] = np.array([0, 0, 4, 0, 0, 0, 0, 3, 0])
    data[8] = np.array([0, 0, 0, 0, 0, 9, 7, 0, 0])
    return data

def data6():
    data[0] = np.array([0, 0, 3, 8, 4, 9, 1, 0, 0])
    data[1] = np.array([0, 1, 0, 0, 0, 0, 0, 3, 0])
    data[2] = np.array([8, 0, 0, 1, 0, 6, 0, 0, 5])
    data[3] = np.array([3, 0, 5, 2, 0, 4, 8, 0, 1])
    data[4] = np.array([1, 0, 0, 0, 7, 0, 0, 0, 2])
    data[5] = np.array([6, 0, 7, 5, 0, 1, 3, 0, 4])
    data[6] = np.array([9, 0, 0, 6, 0, 7, 0, 0, 3])
    data[7] = np.array([0, 3, 0, 0, 0, 0, 0, 1, 0])
    data[8] = np.array([0, 0, 1, 3, 5, 8, 2, 0, 0])
    return data

def data7():
    data[0] = np.array([0,0,0,0,1,4,0,8,0])
    data[1] = np.array([7,0,8,0,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,8,0,0,0])
    data[3] = np.array([5,0,2,0,0,0,0,0,0])
    data[4] = np.array([0,0,0,6,0,0,0,0,0])
    data[5] = np.array([0,0,0,0,0,0,1,0,8])
    data[6] = np.array([0,0,0,0,0,0,9,0,0])
    data[7] = np.array([0,6,0,0,0,0,0,0,0])
    data[8] = np.array([0,0,0,9,3,0,0,0,0])
    return data

def data8():  # 这个数独 无解
    data[0] = np.array([0, 2, 5, 3, 0, 0, 0, 0, 0])
    data[1] = np.array([8, 0, 0, 0, 0, 0, 0, 2, 0])
    data[2] = np.array([0, 7, 0, 0, 1, 0, 5, 0, 0])
    data[3] = np.array([4, 0, 0, 0, 0, 5, 3, 0, 0])
    data[4] = np.array([0, 1, 0, 0, 7, 0, 0, 0, 6])
    data[5] = np.array([0, 0, 3, 2, 0, 0, 0, 8, 0])
    data[6] = np.array([0, 6, 0, 5, 0, 0, 0, 0, 9])
    data[7] = np.array([0, 0, 4, 0, 0, 0, 0, 3, 0])
    data[8] = np.array([0, 0, 0, 0, 0, 9, 7, 0, 0])
    return data

def data9():
    data[0] = np.array([0,0,0,1,1,4,0,8,0])
    data[1] = np.array([7,0,8,0,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,8,0,0,0])
    data[3] = np.array([5,0,2,0,0,0,0,0,0])
    data[4] = np.array([0,0,0,6,0,0,0,0,0])
    data[5] = np.array([0,0,0,0,0,0,1,0,8])
    data[6] = np.array([0,0,0,0,0,0,9,0,0])
    data[7] = np.array([0,6,0,0,0,0,0,0,0])
    data[8] = np.array([0,0,0,9,3,0,0,0,0])
    return data

def data10():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([6,1,5,0,9,0,0,0,0])
    data[1] = np.array([2,0,0,0,0,0,3,8,0])
    data[2] = np.array([7,0,0,5,4,2,0,1,0])
    data[3] = np.array([0,0,2,4,0,1,6,0,0])
    data[4] = np.array([9,0,1,0,0,0,8,0,4])
    data[5] = np.array([0,0,6,9,0,5,2,0,0])
    data[6] = np.array([0,6,0,7,2,9,0,0,8])
    data[7] = np.array([0,2,8,0,0,0,0,0,9])
    data[8] = np.array([0,0,0,0,3,0,1,4,2])
    return data

def data11():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([0,0,0,4,3,6,0,0,0])
    data[1] = np.array([1,0,0,0,0,0,6,5,7])
    data[2] = np.array([8,0,2,0,0,7,0,0,0])
    data[3] = np.array([0,0,0,0,0,0,1,9,5])
    data[4] = np.array([0,0,0,2,0,8,0,0,0])
    data[5] = np.array([7,4,5,0,0,0,0,0,0])
    data[6] = np.array([0,0,0,6,0,0,7,0,8])
    data[7] = np.array([5,7,6,0,0,0,0,0,9])
    data[8] = np.array([0,0,0,7,2,3,0,0,0])
    return data

def data12():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([0,0,0,0,3,2,5,0,0])
    data[1] = np.array([8,0,4,0,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,0,0,0,0])
    data[3] = np.array([0,3,7,0,0,0,0,2,0])
    data[4] = np.array([0,5,0,0,6,0,0,0,0])
    data[5] = np.array([0,0,0,9,0,0,0,1,0])
    data[6] = np.array([4,0,0,8,0,0,0,0,9])
    data[7] = np.array([0,0,0,0,0,0,3,0,0])
    data[8] = np.array([0,0,0,1,0,0,0,0,0])
    return data

def data13():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([6,0,0,0,0,0,4,0,5])
    data[1] = np.array([0,0,8,2,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,0,0,0,0])
    data[3] = np.array([0,0,0,0,0,6,0,1,0])
    data[4] = np.array([4,0,7,0,0,0,0,0,0])
    data[5] = np.array([0,0,0,1,0,0,0,2,0])
    data[6] = np.array([0,0,6,0,0,0,7,8,0])
    data[7] = np.array([0,0,0,0,5,4,0,0,0])
    data[8] = np.array([0,0,0,9,0,0,0,0,0])
    return data

def data14():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([0,0,0,0,0,0,0,0,0])
    data[1] = np.array([0,0,0,0,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,0,0,0,0])
    data[3] = np.array([0,0,0,0,0,0,0,0,0])
    data[4] = np.array([0,0,0,0,0,0,0,0,0])
    data[5] = np.array([0,0,0,0,0,0,0,0,0])
    data[6] = np.array([0,0,0,0,0,0,0,0,0])
    data[7] = np.array([0,0,0,0,0,0,0,0,0])
    data[8] = np.array([0,0,0,0,0,0,0,0,0])
    return data

def data15():
    # data=np.zeros([9,9], dtype=object)
    data[0] = np.array([0,0,0,0,0,0,0,0,0])
    data[1] = np.array([0,0,0,0,0,0,0,0,0])
    data[2] = np.array([0,0,0,0,0,0,0,0,0])
    data[3] = np.array([0,0,0,0,0,0,0,0,0])
    data[4] = np.array([0,0,1,0,0,0,0,0,0])
    data[5] = np.array([0,0,0,0,0,0,2,0,0])
    data[6] = np.array([0,0,0,0,0,0,0,0,0])
    data[7] = np.array([0,0,0,0,0,0,0,0,0])
    data[8] = np.array([0,0,0,0,0,0,0,0,0])
    return data

