from multiprocessing import Process
from multiprocessing import Pool
result=[]
para=[]

def a():
    para.append('x')
    para.append('y')
    return para

if __name__ == '__main__':
    pool = Pool(processes=4)
    result.append(pool.apply_async(a))
    pool.close()
    pool.join()
    for res in result:
        print ":::", res.get()


