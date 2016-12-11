# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 539,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 2 )
		
		
		bSizer1.Add( bSizer2, 0, 0, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Resource (Priority 1)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 7 )
		
		m_choice6Choices = [ wx.EmptyString, u"food", u"wood", u"stone", u"iron" ]
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		fgSizer2.Add( self.m_choice6, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Resource (Priority 2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		m_choice7Choices = [ wx.EmptyString, u"food", u"wood", u"stone", u"iron" ]
		self.m_choice7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		fgSizer2.Add( self.m_choice7, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Resource (Priority 3)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		m_choice8Choices = [ wx.EmptyString, u"food", u"wood", u"stone", u"iron" ]
		self.m_choice8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		fgSizer2.Add( self.m_choice8, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Resource (Priority 4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		m_choice9Choices = [ wx.EmptyString, u"food", u"wood", u"stone", u"iron" ]
		self.m_choice9 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0 )
		self.m_choice9.SetSelection( 0 )
		fgSizer2.Add( self.m_choice9, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer2, 0, wx.ALL|wx.FIXED_MINSIZE, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Food Sold : 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Wood Sold : 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer3.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Stone Sold : 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gSizer3.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Iron Sold : 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gSizer3.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 200 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Proxy-Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Use Proxybroker", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer21, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Max number of proxies to be used", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		bSizer4.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 2 )
		
		
		bSizer1.Add( bSizer4, 0, 0, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Max number of proxies to be checked simultaneously", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		bSizer5.Add( self.m_staticText121, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Max number of connections per proxy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer75.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		self.m_textCtrl95 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_textCtrl95, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer75, 0, wx.EXPAND, 5 )

		bSizer705 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText901 = wx.StaticText( self, wx.ID_ANY, u"Timeout(in seconds)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText901.Wrap( -1 )
		bSizer705.Add( self.m_staticText901, 0, wx.ALL, 5 )
		
		self.m_textCtrl905 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer705.Add( self.m_textCtrl905, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer705, 0, wx.EXPAND, 5 )



		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer1.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

