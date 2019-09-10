import thready as th, time, threading

theLock = threading.Lock()

t1 = th.oneThread(1, 6, theLock)
t2 = th.oneThread(2, 5, theLock)
t3 = th.oneThread(3, 7, theLock)

t1.start()
t2.start()
t3.start()

for i in range(10):
    theLock.acquire()
    print("I am the main thread ... ", i)
    theLock.release()
    time.sleep(1)

t1.join()
t2.join()
t3.join()
print("All done from all threads!")
