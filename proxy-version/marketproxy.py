from GUIMARKET import *
from proxymanager import ProxyManager
import wx
import json
import sys
import os
from threading import Thread
import time
from market import *
app=wx.App()
frame1=MyFrame1(None)
frame2=ProxyManager()
if os.path.exists('tradeconfig.json'):
	try:
		frame1.m_textCtrl905.SetValue("30")
		config=json.loads(open('tradeconfig.json','r').read())
		if 'server' in config:
			frame1.m_textCtrl1.SetValue(config['server'])
		if 'resource1' in config:
			frame1.m_choice6.SetSelection(config['resource1'])
		if 'resource2' in config:
			frame1.m_choice7.SetSelection(config['resource2'])
		if 'resource3' in config:
			frame1.m_choice8.SetSelection(config['resource3'])
		if 'resource4' in config:
			frame1.m_choice9.SetSelection(config['resource4'])
		if 'totalconnections' in config:
			frame1.m_textCtrl4.SetValue(str(config['totalconnections']))
		if 'maxchecking' in config:
			frame1.m_textCtrl5.SetValue(str(config['maxchecking']))
		if 'usebroker' in config:
			frame1.m_checkBox1.SetValue(config['usebroker'])
		if 'maxperproxy' in config:
			frame1.m_textCtrl95.SetValue(str(config['maxperproxy']))
		if "timeout" in config:
			frame1.m_textCtrl905.SetValue(str(config['timeout']))
	except:
		pass
def finishdatahandler(value):
	global totalfoodsold,totalwoodsold,totalironsold,totalstonesold
	if (value[:15]!='SUCCESSFULTRADE'):
		frame1.m_textCtrl3.AppendText(value+"\n")
		return
	value=value[15:]
	value1=value.split(' ')
	if value1[0]=='food':
		totalfoodsold+=int(value1[1])
		frame1.m_staticText17.SetLabel("Food Sold : "+str(totalfoodsold))
		return
	if value1[0]=='wood':
		totalwoodsold+=int(value1[1])
		frame1.m_staticText23.SetLabel("Wood Sold : "+str(totalwoodsold))
		return
	if value1[0]=='stone':
		totalstonesold+=int(value1[1])
		frame1.m_staticText24.SetLabel("Stone Sold : "+str(totalstonesold))
		return
	if value1[0]=='iron':
		totalironsold+=int(value1[1])
		frame1.m_staticText25.SetLabel("Iron Sold : "+str(totalironsold))
		return
def showdetails(event):
	frame2.Show()
	frame2.SetFocus()
frame1.m_button21.Bind(wx.EVT_BUTTON,showdetails)
def checkstopped():
	if frame2.killsignal==True:
		wx.CallLater(1000,checkstopped)
		return
	frame1.m_button2.Enable()
def onstop():
	if frame1.m_button2.GetLabel()=="Start":
		return
	frame2.stop()
	frame1.m_button2.SetLabel("Start")
	frame1.m_button2.Disable()
	checkstopped()
def clearlog():
	if frame1.m_button2.GetLabel()=="Start":
		return
	frame1.m_textCtrl3.SetValue("")
	wx.CallLater(10000,clearlog)
def exectrade(event):
	if frame1.m_button2.GetLabel()=="Stop":
		onstop()
		return
	global totalironsold,totalwoodsold,totalstonesold,totalfoodsold
	frame1.m_button2.SetLabel("Stop")
	server=frame1.m_textCtrl1.GetValue()
	resource1=frame1.m_choice6.GetSelection()
	resource2=frame1.m_choice7.GetSelection()
	resource3=frame1.m_choice8.GetSelection()
	resource4=frame1.m_choice9.GetSelection()
	try:
		totalconnections=int(frame1.m_textCtrl4.GetValue())
		maxchecking=int(frame1.m_textCtrl5.GetValue())
		maxperproxy=int(frame1.m_textCtrl95.GetValue())
		timeout=int(frame1.m_textCtrl905.GetValue())
		if maxperproxy<=0:
			raise
	except:
		frame1.m_button2.SetLabel("Start")
		return
	usebroker=frame1.m_checkBox1.GetValue()
	try:
		d=open('tradeconfig.json','w')
		e={'server':server,'resource1':resource1,'timeout':timeout,'usebroker':usebroker, 'resource2':resource2,'resource3':resource3,'resource4':resource4,'totalconnections':totalconnections,'maxchecking':maxchecking,'maxperproxy':maxperproxy}
		json.dump(e,d)
		d.close()
	except:
		pass
	frame2.MAX_CHECKS=maxchecking
	frame2.MAX_PROCESS=totalconnections
	frame2.handlelogs=True
	totalironsold=0
	totalstonesold=0
	totalwoodsold=0
	totalfoodsold=0
	if usebroker:
		t=Thread(target=frame2.startbroker)
		t.daemon=True
		t.start()
	frame2.startchecker()
	frame2.runprocess(startmarket,server,[resource1,resource2,resource3,resource4],totalconn=maxperproxy,timeout=timeout,callback=finishdatahandler)
	wx.CallLater(10000,clearlog)
def onclose(event):
	onstop()
	sys.exit()
frame1.m_button2.Bind(wx.EVT_BUTTON,exectrade)
frame1.Bind(wx.EVT_CLOSE,onclose)
frame1.Show()
app.MainLoop()