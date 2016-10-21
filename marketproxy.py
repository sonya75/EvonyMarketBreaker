from GUIMARKET import *
from GUIPROXY import *
import wx
app=wx.App()
frame1=MyFrame1(None)
frame2=MyFrame2(None)
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
def showdetails(event):
	if (frame1.m_button21.GetLabel())=="Hide Details":
		frame1.m_button21.SetLabel("Show Details")
		frame2.Hide()
		frame1.m_textCtrl3.Show()
		return
	frame1.m_button21.SetLabel("Hide Details")
	frame1.m_textCtrl3.Hide()
	frame2.Show()
	return
def oncloseframe(event):
	frame1.m_button21.SetLabel("Show Details")
	frame2.Hide()
	frame1.m_textCtrl3.Show()
	return
frame2.Bind(wx.EVT_CLOSE,oncloseframe)
frame1.m_button21.Bind(wx.EVT_BUTTON,showdetails)
frame1.Show()
app.MainLoop()