from evony import *
import time
import os
import sys
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
itemsarray={'player.box.gambling.wood':1,'player.box.gambling.food':0,'player.box.gambling.stone':2,'player.box.gambling.iron':3}
server=sys.argv[1].strip()
prioritylist=sys.argv[2].strip().split(" ")
reslist=['food','wood','stone','iron']
def createacc(server,prioritylist,useclient=None):
	global restypes,quests,itemsarray,reslist
	invalidname=False
	prioritylist=[reslist[(int(j)-1)] for j in prioritylist if int(j)!=0]
	if prioritylist==[]:
		print("INVALIDCHOICE")
		return
	try:
		if useclient==None:
			x=Client(server)
		else:
			x=useclient
		y=x.registernewplayer()
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
		print("Done")
		for g in prioritylist:
			i=0
			while i<(len(result)):
				if result[i]['id']==('player.box.gambling.'+g):
					try:
						x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'0.001','tradeType':1,'amount':result[i]['count'],'resType':itemsarray[result[i]['id']]})
						res=x.responsehandler('trade.newTrade')
						print("SUCCESSFULTRADE"+g+" "+str(result[i]['count']))
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
		print("ERRORREPORT")
		return None
yo=createacc(server,prioritylist)
while True:
	if yo==None:
		break
	yo.registered=False
	yo=createacc(server,prioritylist,useclient=yo)