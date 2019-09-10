import threading, time

class oneThread(threading.Thread):

   def __init__(self, num, reps, theLock):
      threading.Thread.__init__(self)
      self.num = num
      self.reps = reps
      self.lock = theLock
      self.cnt = 0

   def run(self) :
      while True :
         time.sleep(1)
         self.lock.acquire()
         print("I am thread number: ", self.num)
         self.lock.release()
         self.cnt += 1
         if self.cnt >= self.reps:
             break