#coding=utf-8
import threading  
import random  
import time  
  
class SemaphoreThread(threading.Thread):  
    """classusing semaphore"""  
     
    account = 10000
    
    def __init__(self,threadName,semaphore):  
       """initialize thread"""  
         
       threading.Thread.__init__(self,name=threadName)  
       self.sleepTime=random.randrange(1,6)  
       #set the semaphore as a data attribute of the class  
       self.threadSemaphore=semaphore


    def store(self):  

       self.threadSemaphore.acquire()
       accout += 10
       time.sleep(self.sleepTime)  
       print "%s store 10 to account, remain %d" % (self.getName(), account)
       SemaphoreThread.availableTables.append(table)
    
    def take(self):  
       self.threadSemaphore.acquire()
       accout -= 10
       time.sleep(self.sleepTime)  
       print "%s take 10 from account, remain %d" % (self.getName(), account)
       SemaphoreThread.availableTables.append(table)


    def run(self):  
       print "%s entered;" % self.getName()
       for i in range(0, 5):
           self.store()
           self.take()
       self.threadSemaphore.release()  
         
threads=[]
threadSemaphore=threading.Semaphore(1)
for i in range(1,3):
   threads.append(SemaphoreThread("thread"+str(i),threadSemaphore))  
for thread in threads:
   thread.start()  
