from proxyscraper import *
from threading import Thread 
import Queue
import socks
def checkproxy(x):
	if x.count(':')!=1:
		return False
	y=x.strip().split(':')
	if (y[-1]!='80')&(y[-1]!='8080'):
		return False
	port = int(y[1])
	ip=y[0]
	ket=socks.socksocket()
	ket.setproxy(socks.PROXY_TYPE_HTTP,ip,port)
	print("DONE")
	try:
		ket.connect(("google.co.in",80))
		print("CONNECTED")
		ket.close()
		print(r)
		return True
	except:
		return False
def addtoqueue(x):
	global proxyqueue
	proxyqueue.put(x)
def mainchecker():
	global proxyqueue
	proxyqueue=Queue.Queue()
	t=Thread(target=main,args=(addtoqueue,))
	t.daemon=True
	t.start()
	startchecking(t)
def startchecking(c):
	global proxyqueue
	while True:
		try:
			r=proxyqueue.get()
			Thread(target=checkproxy,args=(r,)).start()
		except:
			pass
		time.sleep(1)