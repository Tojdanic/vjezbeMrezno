from threading import Thread,current_thread
import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	def run(self):
		print "Pokrece se nit " + self.name
		process_data(self.name, self.q)
		print "izlazi iz niti " + self.name

def process_data(threadName, q):
	while not exitFlag:
		queueLock.acquire()
	if not workQueue.empty():
		data = q.get()
		queueLock.release()
		print "Procesuira %s" %(threadName, data)
	else:
		queueLock.release()
		time.sleep(1)
		
threadList = [ "Thread-1","Thread-2", "Thread-3" ]
nameList = [ "Jedan", "Dva", "Tri", "Cetri", "Pet" ]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
	thread = myThread(threadID, tName, workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1
	
queueLock.acquire()
for word in nameList:
	workQueue.put(word)
queueLock.release()

while not workQueue.empty():
	pass
	
exitFlag = 1

for t in threads:
	t.join
print "\nIzlazim\n"