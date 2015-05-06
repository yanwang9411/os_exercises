#coding=utf-8
#!/usr/bin/env python
  
import threading  
import time  
   
condition = threading.Condition()  
account = 0
   
class Store(threading.Thread):
    def __init__(self):  
        threading.Thread.__init__(self)  
          
    def run(self):  
        global condition, account
        while True:  
            if condition.acquire():  
                if account <= 0:
                    account += 10;
                    print "store $10, remain %d" % account
                    condition.notify()  
                else:  
                    account += 10;
                    print "store $10, remain %d" % account

                condition.release()
                time.sleep(2)  
          
class Take(threading.Thread):
    def __init__(self):  
        threading.Thread.__init__(self)  
          
    def run(self):  
        global condition, account
        while True:  
            if condition.acquire():  
                if account > 0:
                    account -= 10
                    print "take $10, remain %d" % account
                else:
                    print "account is overdrawed, wait..."
                    condition.wait();  
                condition.release()  
                time.sleep(2)  
                  
if __name__ == "__main__":  
    for p in range(0, 2):
        p = Store()
        p.start()  
          
    for c in range(0, 2):
        c = Take()
        c.start() 
