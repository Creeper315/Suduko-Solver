import numpy as np
import helper as H
import clas as C
import data as D

data = D.data15()
print(data)
total_empty_elements = 0
iteration = 0
#upper_limit_iteration = 1000
#print(np.concatenate((data[5], data[:,6], H.getCluster(data, [5,6]))))

if __name__ == '__main__':
    total_empty_elements = data.shape[0]*data.shape[1] - np.count_nonzero(data)
    S = C.Stack()
    myDATA = H.give_empty_elements_list(data)
    #print(myDATA)
    print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')

    def recurse_f():
        global myDATA
        global iteration
        if S.length() == total_empty_elements:
            print('Total iterations used: ' + str(iteration))
            return True
        else:
            idx_smallest = H.get_index_with_least_available_value(myDATA, S)
            S.add(idx_smallest)
            a, b = S.current()[0], S.current()[1]

        for val in myDATA[a,b]:
            myDATA_save = myDATA.copy() # 注意！注意！ 这里！ 必须加 myDATA.copy() !!! 必须加上 copy。。。这个 bug 卡了几个小时。。
            myDATA = H.update_empty_elements_after_filling_one(myDATA, [a, b], val)
            iteration+=1
            if H.check_all_element_have_nonzero_available_value(myDATA):
                if recurse_f():
                    return True
                else:
                    myDATA = myDATA_save
                    continue
            else:
                myDATA = myDATA_save
                continue   # If violation occurs
        S.pop()
        if S.length() == 0:
            print('Total iterations used: ' + str(iteration))
        return False


    if H.check_input_data_is_valid(data):
        if recurse_f():
            output = H.output_result(myDATA)
            print(output)
        else:
            print('This Suduko has no solution ,,,,')
            print('Last result :')
            print(myDATA)
    else:
        print('Cannot solve, invalid input data,')
        print('Input data has duplicate value in either row / col / groups')

