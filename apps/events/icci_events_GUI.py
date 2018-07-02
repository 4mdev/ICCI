# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.html, wx.adv, wx.html2

###########################################################################
## Class Events_Panel
###########################################################################

class Events_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,120 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL,  )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		wybor_kalendarzaChoices = [ u"CoinMarketCall", u"Coindar" ]
		self.wybor_kalendarza = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wybor_kalendarzaChoices, 0 )
		self.wybor_kalendarza.SetSelection( 0 )
		bSizer3.Add( self.wybor_kalendarza, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.start_date = wx.adv.DatePickerCtrl(self, size=(120,-1),
                                style = wx.adv.DP_DROPDOWN
                                      | wx.adv.DP_SHOWCENTURY
                                      | wx.adv.DP_ALLOWNONE )
		bSizer3.Add( self.start_date, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.finish_date = wx.adv.DatePickerCtrl(self, size=(120,-1),
                                style = wx.adv.DP_DROPDOWN
                                      | wx.adv.DP_SHOWCENTURY
                                      | wx.adv.DP_ALLOWNONE )
		bSizer3.Add( self.finish_date, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		wybor_walutyChoices = []
		self.wybor_waluty = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wybor_walutyChoices, 0 )
		self.wybor_waluty.SetSelection( 0 )
		bSizer3.Add( self.wybor_waluty, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		wybor_kategoriiChoices = []
		self.wybor_kategorii = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wybor_kategoriiChoices, 0 )
		self.wybor_kategorii.SetSelection( 0 )
		bSizer3.Add( self.wybor_kategorii, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		sortowanieChoices = []
		self.sortowanie = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sortowanieChoices, 0 )
		self.sortowanie.SetSelection( 0 )
		bSizer3.Add( self.sortowanie, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		filtrChoices = []
		self.filtr = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filtrChoices, 0 )
		self.filtr.SetSelection( 0 )
		bSizer3.Add( self.filtr, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.pokaz = wx.Button( self, wx.ID_ANY, u"Pokaż", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.pokaz, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		bSizer2.Add( bSizer3, 0, 0, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_htmlWin1 = wx.html2.WebView.New(self)
		bSizer4.Add( self.m_htmlWin1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.pokaz.Bind( wx.EVT_BUTTON, self.kalendarz_pokaz_funkcja )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def kalendarz_pokaz_funkcja( self, event ):
		event.Skip()
	

