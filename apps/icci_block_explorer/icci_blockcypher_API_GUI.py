# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,120 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL,  )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		bc_waluta_Sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.lista_kryptoChoices = [ ]
		self.lista_krypto = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.lista_kryptoChoices, 0 )
		self.lista_krypto.SetSelection( 0 )
		bc_waluta_Sizer.Add( self.lista_krypto, 0, wx.ALL, 5 )
		
		bSizer29.Add( bc_waluta_Sizer, 0, wx.EXPAND, 5 )
		
		bc_do_wypelnienia_Sizer = wx.FlexGridSizer( 3, 3, 0, 0 )
		bc_do_wypelnienia_Sizer.SetFlexibleDirection( wx.BOTH )
		bc_do_wypelnienia_Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bc_portfel_label = wx.StaticText( self, wx.ID_ANY, u"portfel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bc_portfel_label.Wrap( -1 )
		bc_do_wypelnienia_Sizer.Add( self.bc_portfel_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bc_portfel_nr_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bc_portfel_nr_input.SetMinSize( wx.Size( 520,-1 ) )
		
		bc_do_wypelnienia_Sizer.Add( self.bc_portfel_nr_input, 0, wx.ALL, 5 )
		
		self.bc_portfel_getinfo_button = wx.Button( self, wx.ID_ANY, u"info", wx.DefaultPosition, wx.DefaultSize, 0 )
		bc_do_wypelnienia_Sizer.Add( self.bc_portfel_getinfo_button, 0, wx.ALL, 5 )
		
		self.bc_transakcja_label = wx.StaticText( self, wx.ID_ANY, u"transakcja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bc_transakcja_label.Wrap( -1 )
		bc_do_wypelnienia_Sizer.Add( self.bc_transakcja_label, 0, wx.ALL, 5 )
		
		self.bc_transakcja_nr_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 520,-1 ), 0 )
		bc_do_wypelnienia_Sizer.Add( self.bc_transakcja_nr_input, 0, wx.ALL, 5 )
		
		self.bc_transakcja_getinfo_button = wx.Button( self, wx.ID_ANY, u"info", wx.DefaultPosition, wx.DefaultSize, 0 )
		bc_do_wypelnienia_Sizer.Add( self.bc_transakcja_getinfo_button, 0, wx.ALL, 5 )
		
		self.bc_blok_label = wx.StaticText( self, wx.ID_ANY, u"blok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bc_blok_label.Wrap( -1 )
		bc_do_wypelnienia_Sizer.Add( self.bc_blok_label, 0, wx.ALL, 5 )
		
		self.bc_blok_nr_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 520,-1 ), 0 )
		bc_do_wypelnienia_Sizer.Add( self.bc_blok_nr_input, 0, wx.ALL, 5 )
		
		self.bc_blok_getinfo_button = wx.Button( self, wx.ID_ANY, u"info", wx.DefaultPosition, wx.DefaultSize, 0 )
		bc_do_wypelnienia_Sizer.Add( self.bc_blok_getinfo_button, 0, wx.ALL, 5 )
		
		bSizer29.Add( bc_do_wypelnienia_Sizer, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer29 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bc_portfel_getinfo_button.Bind( wx.EVT_BUTTON, self.bc_portfel_getinfo_funkcja )
		self.bc_transakcja_getinfo_button.Bind( wx.EVT_BUTTON, self.bc_transakcja_getinfo_funkcja )
		self.bc_blok_getinfo_button.Bind( wx.EVT_BUTTON, self.bc_blok_getinfo_funkcja )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def bc_portfel_getinfo_funkcja( self, event ):
		event.Skip()
	
	def bc_transakcja_getinfo_funkcja( self, event ):
		event.Skip()
	
	def bc_blok_getinfo_funkcja( self, event ):
		event.Skip()
	

