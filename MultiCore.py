print("##############multi-processing############")
print("##############multi-processing create ############")
##### must run in terminal
import multiprocessing as mp
def job(a,d):
    print("aaaaa")
#### if __name__ is a must need###
if __name__=='__main__':
    p1 = mp.Process(target=job,args=(1,2))
    p1.start()
    p1.join()
print("##############Queue function in multi-processing ############")
#### put the multiprocessing result in the queue, wait all the calculation finish and then use them into next step  
def job(q):
    res = 0
    for i in range(1000):
        res +=i+i**2+i**3
    q.put(res)  ## queue

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
print("##############multi-threading VS multi-processing ############")

import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(1000000):
        res +=i+i**2+i**3
    q.put(res)
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1+res2)
def normal():
    res=0
    for _ in range(2):
        for i in range(1000000):
            res +=i+i**2+i**3
    print('normal:',res)
def multithread():
    q = mp.Queue()
    p1 = td.Thread(target=job,args=(q,))
    p2 = td.Thread(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:',res1+res2)

if __name__ == '__main__':
    st = time.time()
    normal()
    st1= time.time()
    print('normal time:',st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:',st2 - st1)
    multicore()
    print('multicore time:',time.time()-st2)

print("############## Pool ############")
#####Python will arrange calculation automatically########
import multiprocessing as mp
def job(x):
    return x*x   ### pool can give a return 
def multicore():
 #  pool = mp.Pool() ##### Python will arrange all cores automatically 
    pool = mp.Pool(processes=2)   ##### assign it use only 2 cores
    res = pool.map(job, range(10)) ###map can work all value
    print(res)
    res = pool.apply_async(job, (2,))   ### apply function only work one
    print(res.get())
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)] #### must run with a for
    print([res.get() for res in multi_res])
    
if __name__=='__main__':
    multicore()

print("############## Shared memory ############")
import multiprocessing as mp
### define shared memory
value = mp.Value('d',1)
### define a list but here called array, only one dimension
array = mp.Array('i',[1,2,3])

print("############## Lock function ############")

import multiprocessing as mp
import time
##### without lock, every processing will fight with value and output weird rsult 
def job(v, num):
    for _ in range(10):
        time.sleep(0.1)
        v.value += num   ### p1 will add 1 and p2 will add 3
        print(v.value)

def multicore():
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()
print("############## add Lock function ############")   
######with lock, will get p1 finish and then based on p1 's memory do p2
import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()

































    











    





