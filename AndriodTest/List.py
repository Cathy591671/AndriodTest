from multiprocessing import Process
from multiprocessing import Pool
import time

la=[1,2,3,4,5,6]
def a():
    la.append(7)
    print la

if __name__ == '__main__':
    a()



