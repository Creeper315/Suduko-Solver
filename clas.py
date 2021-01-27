import numpy as np


class Stack:
    def __init__(self):
        self.value = np.ndarray([0,2], dtype=int)  # Note: If dtype is not "int", later when we use these number as index, we might return float, but only integers can be index.
        #self.value = np.zeros([0, 2])

    def add(self, position):
        self.value = np.concatenate((self.value, np.array([position])), axis=0)

    def pop(self):
        r = self.value[-1]
        self.value = self.value[0:-1]
        return r

    def current(self):
        return self.value[-1]

    def length(self):
        return len(self.value)

    def contain(self, position):
        for i in self.value:
            if position[0] == i[0] and position[1] == i[1]:
                return True
        return False


if __name__ == '__main__':
    '''s = Stack()
    print(s.value)
    s.add([1,2])
    s.add([4,5])
    s.add([9,10])
    print(s.value)
    print(s.value[0])
    print(s.value)
    print(s.contain([3,5]))
    print(s.current()[0])'''
