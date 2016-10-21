from GUIMARKET import *
from threading import Thread
import subprocess
import os
import json
import sys
import time
thrd=None
app=wx.App(False)
frame=MyFrame1(None)
votecount=0
def killtrade(pid,triedone=False):
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	subprocess.Popen(["TASKKILL","/F","/T","/pid",str(pid)],startupinfo=startupinfo)
	if not triedonce:
		wx.CallLater(1000,killtrade,pid,True)
def onclose(event):
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	subprocess.Popen(["TASKKILL","/F","/im","market.exe"],startupinfo=startupinfo)
	sys.exit()
def checkprocess():
	global tradeprocess,lastupdate
	try:
		if (frame.m_button2.GetLabel())=="Start":
			return
		else:
			if (time.time()-lastupdate)>15:
				try:
					ppid=tradeprocess.pid
					killtrade(ppid)
				except:
					pass
				lastupdate=time.time()
				frame.m_textCtrl3.SetValue("Error in connection. Trying again.")
				wx.CallLater(100,exectrade,None)
				return
			wx.CallLater(1000,checkprocess)
	except:
		wx.CallLater(1000,checkprocess)
		return
frame.Bind(wx.EVT_CLOSE,onclose)
if os.path.exists('tradeconfig.json'):
	try:
		config=json.loads(open('tradeconfig.json','r').read())
		if 'server' in config:
			frame.m_textCtrl1.SetValue(config['server'])
		if 'resource1' in config:
			frame.m_choice6.SetSelection(config['resource1'])
		if 'resource2' in config:
			frame.m_choice7.SetSelection(config['resource2'])
		if 'resource3' in config:
			frame.m_choice8.SetSelection(config['resource3'])
		if 'resource4' in config:
			frame.m_choice9.SetSelection(config['resource4'])
	except:
		pass
def handletext(value):
	global lastupdate
	lastupdate=time.time()
	frame.m_textCtrl3.write(value)
def handleerror(value):
	global lastupdate,tradeprocess
	try:
		killtrade(tradeprocess.pid)
	except:
		pass
	if value==0:
		frame.m_textCtrl3.SetValue("Invalid resource priority. Try again.")
		frame.m_button2.SetLabel("Stop")
		return
	if value==1:
		frame.m_textCtrl3.SetValue("Error occured. Trying again in 3 seconds.")
		wx.CallAfter(exectrade,None)
		return
	lastupdate=time.time()
def finishhandler(value):
	global woodcount,foodcount,stonecount,ironcount
	value=value.strip().split("SUCCESSFULTRADE")[-1].split(" ")
	if value[0]=="food":
		foodcount+=int(value[1])
		frame.m_staticText17.SetLabel("Food Sold : "+str(foodcount))
		return
	if value[0]=="wood":
		woodcount+=int(value[1])
		frame.m_staticText23.SetLabel("Wood Sold : "+str(woodcount))
		return
	if value[0]=="stone":
		stonecount+=int(value[1])
		frame.m_staticText24.SetLabel("Stone Sold : "+str(stonecount))
		return
	if value[0]=="iron":
		ironcount+=int(value[1])
		frame.m_staticText25.SetLabel("Iron Sold : "+str(ironcount))
		return
def fff(comm):
	global tradeprocess
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(comm,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	tradeprocess=p
	for q in p.stdout:
		if "INVALIDCHOICE" in q:
			wx.CallAfter(handleerror,0)
			break
		if "SUCCESSFULTRADE" in q:
			wx.CallAfter(finishhandler,q)
			continue
		if "ERRORREPORT" in q:
			wx.CallAfter(handleerror,1)
			break
		wx.CallAfter(handletext,q)
def exectrade(event):
	global thrd,tradeprocess,lastupdate,foodcount,woodcount,stonecount,ironcount
	if ((frame.m_button2.GetLabel())=="Stop")&(event!=None):
		try:
			killtrade(tradeprocess.pid)
		except:
			pass
		frame.m_button2.SetLabel("Start")
		return
	if (event==None)&((frame.m_button2.GetLabel())=="Start"):
		return
	if event!=None:
		foodcount=0
		woodcount=0
		stonecount=0
		ironcount=0
		frame.m_staticText17.SetLabel("Food Sold : 0")
		frame.m_staticText23.SetLabel("Wood Sold : 0")
		frame.m_staticText24.SetLabel("Stone Sold : 0")
		frame.m_staticText25.SetLabel("Iron Sold : 0")
	frame.m_button2.SetLabel("Stop")
	frame.m_textCtrl3.SetValue("Starting to build account for trading....")
	server=frame.m_textCtrl1.GetValue()
	resource1=frame.m_choice6.GetSelection()
	resource2=frame.m_choice7.GetSelection()
	resource3=frame.m_choice8.GetSelection()
	resource4=frame.m_choice9.GetSelection()
	try:
		f=open('tradeconfig.json','w')
		d={'server':server,'resource1':resource1,'resource2':resource2,'resource3':resource3,'resource4':resource4}
		json.dump(d,f)
		f.close()
	except:
		pass
	thrd=Thread(target=fff,args=(["market.exe",server,(" ".join([str(resource1),str(resource2),str(resource3),str(resource4)]))],))
	thrd.daemon=True
	thrd.start()
	lastupdate=time.time()
	wx.CallLater(1000,checkprocess)
frame.m_button2.Bind(wx.EVT_BUTTON,exectrade)
frame.Show()
app.MainLoop()