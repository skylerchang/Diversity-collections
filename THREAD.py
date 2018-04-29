print("#############multi-threading################")

import threading

### count numbers of active threading
### check which threading is using now
### show the running thread
def main():
    print(threading.active_count())    
    print(threading.enumerate())
    print(threading.current_thread())       
if __name__=='__main__':
    main()
####
def thread_job():
       print("This is an added Thread, number is %s" % threading.current_thread())

##### threading.Thread is adding thread, the now work for this thread is thread_job
##### .start() is to run this
def main():
    added_thread=threading.Thread(target=thread_job)
    added_thread.start()
       
if __name__=='__main__':
    main()

print("###########join function in thread###########")
#### Step1. output is T1 start,all done, later T1 finish, this means multi-threads run at the same time
import threading
import time
def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)   ####run every time and sleep 0.1s
    print("T1 finish\n")
def main():
    added_thread=threading.Thread(target=thread_job,name="T1")  ### name this thread as T1
    added_thread.start()
    print("all done\n")
    
if __name__=='__main__':
    main()
#### Join function is to wait all the previous work finish then run the script after join
def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)   ####run every time and sleep 0.1s
    print("T1 finish\n")
def T2_job():
    print("T2 start\n")
    print("T2 finish\n")
def main():
    added_thread=threading.Thread(target=thread_job,name="T1")  ### name this thread as T1
    added_thread2 = threading.Thread(target=T2_job,name="T2")
    added_thread.start()
    added_thread2.start()
    added_thread.join()
    added_thread2.join()
    print("all done\n")    

if __name__=='__main__':
    main()

print("###########Queue function in thread###########")
### in thread, there is no return, put the return in the queue, then put every queue in separate thread in main thread 
import threading
import time
from queue import Queue
def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)
def multithreading():
    q= Queue()
    threads=[]
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)
                        
if __name__=='__main__':
    multithreading()

#####GIL#########
print("###########Lock function in thread###########")
#####Lock is to lock the first thread and then wait to finish and then use the second thread, use when share memory 
import threading
def job1():
    global A
    for i in range(10):
        A+=1
        print('job1',A)

def job2():
    global A
    for i in range(10):
        A+=10
        print('job2',A)
        
if __name__=='__main__':
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()             
    t2.join()
#####USE LOCK first print job1 and then job2#######
import threading
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()
        
if __name__=='__main__':
    lock =threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()             
    t2.join()    


    
