from evony import *
import time
import os
import sys
from threading import Thread
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
itemsarray={'player.box.gambling.wood':1,'player.box.gambling.food':0,'player.box.gambling.stone':2,'player.box.gambling.iron':3}
reslist=['food','wood','stone','iron']
def createacc(server,prioritylist,useclient=None,proxy=None,proxytype='HTTP',callback=None,timeout=30):
	global restypes,quests,itemsarray,reslist
	try:
		invalidname=False
		t=[]
		for p in prioritylist:
			if p not in t:
				t.append(p)
		prioritylist=t
		prioritylist=[reslist[(int(j)-1)] for j in prioritylist if int(j)!=0]
		if prioritylist==[]:
			callback("8||INVALIDCHOICE")
			return
		if proxy!=None:
			try:
				proxyhost=proxy.split(':')[0]
				proxyport=int(proxy.split(':')[1])
				setproxy=True
			except:
				proxyhost=''
				proxyport=0
				setproxy=False
		else:
			proxyhost=''
			proxyport=0
			setproxy=False
		if useclient==None:
			x=Client(server,setproxy=setproxy,proxyhost=proxyhost,proxyport=proxyport,proxytype=proxytype,callback=callback,timeout=timeout)
		else:
			x=useclient
		y=x.registernewplayer()
		callback("|9|9")
		builder=Builder(x)
		castleid=y['data']['player']['castles'][0]['id']
		quest=Quest(x,castleid)
		items=Item(x,castleid)
		items.useitem('player.box.present.2')
		x.client.sendmessage('common.addToFavorites',{})
		res=x.responsehandler('common.addToFavorites')
		builder.createbuilding(castleid,0,1)
		quest.completequest(1)
		quest.completequest(226)
		quest.completequest(535)
		builder.createbuilding(castleid,1,23)
		time.sleep(.5)
		builder.speedup(castleid,'consume.2.a',1)
		while True:
			res=x.responsehandler('server.BuildComplate',checkok=False)
			if res['data']['buildingBean']['endTime']==0.0:
				break
		result=[]
		v=items.useitem('player.box.gambling.3')
		if v['data']['itemBeans'][0]['id'] in itemsarray:
			result.append(v['data']['itemBeans'][0])
		quest.completequest(223)
		v=items.useitem('player.box.gambling.3')
		if v['data']['itemBeans'][0]['id'] in itemsarray:
			result.append(v['data']['itemBeans'][0])
		v=items.useitem('player.box.gambling.3')
		if v['data']['itemBeans'][0]['id'] in itemsarray:
			result.append(v['data']['itemBeans'][0])
		v=items.useitem('player.box.gambling.3')
		if v['data']['itemBeans'][0]['id'] in itemsarray:
			result.append(v['data']['itemBeans'][0])
		pr=[prioritylist[i] for i in range(0,len(prioritylist)) if prioritylist[i] not in prioritylist[:i]]
		for g in pr:
			i=0
			while i<(len(result)):
				if result[i]['id']==('player.box.gambling.'+g):
					try:
						x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'0.001','tradeType':1,'amount':result[i]['count'],'resType':itemsarray[result[i]['id']]})
						res=x.responsehandler('trade.newTrade')
						callback("8||SUCCESSFULTRADE"+g+" "+str(result[i]['count']))
						i=i+1
						continue
					except Exception as e:
						if e.args[0]==-1:
							time.sleep(2)
							continue
						i=i+1
				i=i+1
		return x
	except:
		try:
			x.close()
		except:
			pass
def _stamulet(server,prioritylist,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalrunning=None):
	x=0
	useclient=None
	while x!=None:
		if useclient!=None:
			useclient.registered=False
		if checksource!=None:
			if checksource.killsignal:
				break
		x=createacc(server,prioritylist,useclient,proxy,proxytype,callback,timeout=timeout)
		useclient=x
	totalrunning[0]-=1
def startmarket(server,prioritylist,useclient=None,proxy=None,proxytype='HTTP',callback=None,checksource=None,timeout=30,totalconn=1):
	totalrunning=[0]
	for i in range(0,totalconn):
		totalrunning[0]+=1
		while True:
			try:
				Thread(target=_stamulet,args=(server,prioritylist,proxy,proxytype,useclient,callback),kwargs={'checksource':checksource,'totalrunning':totalrunning,'timeout':timeout}).start()
				break
			except:
				time.sleep(.3)
	while True:
		if checksource!=None:
			if checksource.killsignal:
				if totalrunning[0]>0:
					time.sleep(.3)
					continue
				callback("|NOKILL|")
				return
		if totalrunning[0]==0:
			callback("|KILL|")
			return
		time.sleep(.3)