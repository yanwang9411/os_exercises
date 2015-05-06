#coding=utf-8
import threading  
import random  
import time  

account = 10000


class SemaphoreThread(threading.Thread):  
    """classusing semaphore"""  
     

    def __init__(self,threadName,semaphore):  
       """initialize thread"""  
         
       threading.Thread.__init__(self,name=threadName)  
       self.sleepTime=random.randrange(1,6)  
       #set the semaphore as a data attribute of the class  
       self.threadSemaphore=semaphore


    def store(self):  
       global account
       self.threadSemaphore.acquire()
       account += 10
       time.sleep(self.sleepTime)
       print "%s store 10 to account, remain %d" % (self.getName(), account)
       self.threadSemaphore.release()


    def take(self):
       global account
       self.threadSemaphore.acquire()
       account -= 10
       time.sleep(self.sleepTime)  
       print "%s take 10 from account, remain %d" % (self.getName(), account)
       self.threadSemaphore.release()


    def run(self):  
       print "%s entered;" % self.getName()
       for i in range(0, 5):
           self.store()
           self.take()

threads=[]
threadSemaphore=threading.Semaphore(1)
for i in range(1,3):
   threads.append(SemaphoreThread("thread"+str(i),threadSemaphore))  
for thread in threads:
   thread.start()  
