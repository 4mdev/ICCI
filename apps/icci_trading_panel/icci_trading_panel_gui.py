# -*- coding: utf-8 -*- 
#self.chart_name = wx.html2.WebView.New( self )
#sbSizer14.Add( self.chart_name, 1, wx.ALL|wx.EXPAND, 5 )
###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
#self.chart_name = wx.html2.WebView.New( self )
#sbSizer14.Add( self.chart_name, 1, wx.ALL|wx.EXPAND, 5 )


import wx
import wx.html2

import CC_get_app_patch
application_path = CC_get_app_patch.pobierz_app_patch()

from gielda_choice_boxChoices_lista import markets_choice_boxChoices_lista_b
from wx.adv import BitmapComboBox   # Phoenix

valid_list = ['gdax','bithumb','binance','kraken','bitflyer','luno','bitfinex','bitstamp','gemini','bitbay','okex','poloniex','huobi','coinone','bitz',]
valid_list.sort()
invalid_list = ['acx', 'allcoin', 'anxpro', 'bit2c', 'bitbank', 'btcchina', 'bitkk','bitmex', 'bitlish', 'bitmarket', 'bitso', 'bl3p', 'bleutrade', 'braziliex','bittrex', 'btcbox', 'btcexchange', 'btcmarkets', 'btctradeim','btctradeua', 'btcturk', 'bxinth', 'ccex', 'cex', 'chilebit', 'cobinhood', 'coincheck', 'coinegg', 'coinex', 'coinexchange', 'coinfloor', 'coingi', 'coinmate', 'coinnest', 'coinone', 'coinspot', 'cryptopia', 'dsx', 'ethfinex', 'exmo', 'exx', 'flowbtc', 'foxbit', 'fybse', 'fybsg', 'gatecoin', 'getbtc', 'hadax', 'huobicny', 'huobipro', 'ice3x', 'independentreserve', 'indodax', 'itbit', 'jubi', 'kucoin', 'kuna', 'lbank', 'liqui', 'livecoin', 'lykke', 'mixcoins', 'negociecoins', 'nova', 'okcoincny', 'okcoinusd', 'paymium', 'quadrigacx', 'quoinex', 'southxchange', 'surbitcoin', 'therock', 'tidex', 'vbtc', 'wex', 'xbtce', 'yobit', 'yunbi', 'zaif', 'zb']
invalid_list.sort()


###########################################################################
## Class Panel_Gieldowy
###########################################################################

class Panel_Gieldowy ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1260,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		global sbSizer122
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Chart" ), wx.VERTICAL )
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel5 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		self.wykres_htmlWin4 = wx.html2.WebView.New( self.m_panel5)
		bSizer25.Add( self.wykres_htmlWin4, 1, wx.ALL|wx.EXPAND, 5 )
		self.m_panel5.SetSizer( bSizer25 )
		self.m_panel5.Layout()
		bSizer25.Fit( self.m_panel5 )
		self.m_notebook2.AddPage( self.m_panel5, u"Wykres", False )
		
		sbSizer14.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer22.Add( sbSizer14, 1, wx.EXPAND, 5 )
		
		bSizer18.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		self.bSizer63 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.info_label = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.info_label.Wrap( -1 )
		self.bSizer63.Add( self.info_label, 1, wx.ALL, 5 )

		self.gielda_choice_box = BitmapComboBox( self, wx.ID_ANY, 'bitfinex', wx.DefaultPosition, wx.Size( 150,-1 ))

		image = wx.Image(u''+application_path+"/ikony_dashboard/vvalid.png")
		valid_bmp = wx.Bitmap(image)
		image = wx.Image(u''+application_path+"/ikony_dashboard/vinvalid.png")
		invalid_bmp = wx.Bitmap(image)
		for i in valid_list:
		    self.gielda_choice_box.Append(i, bitmap=valid_bmp)
		for i in invalid_list:
		    self.gielda_choice_box.Append(i, bitmap=invalid_bmp)
		self.bSizer63.Add( self.gielda_choice_box, 0, wx.ALL, 5 )


		#gielda_choice_boxChoices = gielda_choice_boxChoices_lista_b()
		#self.gielda_choice_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, gielda_choice_boxChoices, 0 )
		self.gielda_choice_box.SetSelection( 2 )
		#self.bSizer63.Add( self.gielda_choice_box, 0, wx.ALL, 5 )
		
		rynek_choice_boxChoices = [ 'BTC/USD']
		self.rynek_choice_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, rynek_choice_boxChoices, 0 )
		self.rynek_choice_box.SetSelection( 0 )
		self.bSizer63.Add( self.rynek_choice_box, 0, wx.ALL, 5 )
		
		#self.portfel1 = wx.StaticText( self, wx.ID_ANY, u"portfel1", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.portfel1.Wrap( -1 )
		#self.bSizer63.Add( self.portfel1, 0, wx.ALL, 5 )
		
		#self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.m_staticText22.Wrap( -1 )
		#self.bSizer63.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		#self.portfel2 = wx.StaticText( self, wx.ID_ANY, u"portfel2", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.portfel2.Wrap( -1 )
		#self.bSizer63.Add( self.portfel2, 0, wx.ALL, 5 )
		
		bSizer18.Add( self.bSizer63, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer122 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Wystawione oferty" ), wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		sbSizer122.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		sbSizer122.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		sbSizer122.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		sbSizer122.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		sbSizer122.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		sbSizer122.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		sbSizer122.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		sbSizer122.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		bSizer23.Add( sbSizer122, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		self.transakcyjny = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_market = wx.Panel( self.transakcyjny, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		sizer_opcje = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14.Add( sizer_opcje, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj = wx.BoxSizer( wx.HORIZONTAL )
		
		box_kup2 = wx.StaticBoxSizer( wx.StaticBox( self.panel_market, wx.ID_ANY, u"kup" ), wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText133 = wx.StaticText( self.panel_market, wx.ID_ANY, u"ilość", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133.Wrap( -1 )
		bSizer17.Add( self.m_staticText133, 0, wx.ALL, 5 )
		
		self.pole_ilosc_market_kup = wx.TextCtrl( self.panel_market, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.pole_ilosc_market_kup, 0, wx.ALL, 5 )
		
		self.market_kup = wx.Button( self.panel_market, wx.ID_ANY, u"ZAKUP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.market_kup, 0, wx.ALL, 5 )
		
		box_kup2.Add( bSizer17, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj.Add( box_kup2, 1, wx.EXPAND, 5 )
		
		box_sprzedaj2 = wx.StaticBoxSizer( wx.StaticBox( self.panel_market, wx.ID_ANY, u"sprzedaj" ), wx.VERTICAL )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText134 = wx.StaticText( self.panel_market, wx.ID_ANY, u"ilość", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )
		bSizer181.Add( self.m_staticText134, 0, wx.ALL, 5 )
		
		self.pole_ilosc_market_sprzedaj = wx.TextCtrl( self.panel_market, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.pole_ilosc_market_sprzedaj, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.panel_market, wx.ID_ANY, u"SPRZEDAŻ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.m_button14, 0, wx.ALL, 5 )
		
		box_sprzedaj2.Add( bSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj.Add( box_sprzedaj2, 1, wx.EXPAND, 5 )
		
		bSizer14.Add( sizer_kup_sprzedaj, 1, 0, 5 )
		
		self.panel_market.SetSizer( bSizer14 )
		self.panel_market.Layout()
		bSizer14.Fit( self.panel_market )
		self.transakcyjny.AddPage( self.panel_market, u"MARKET", False )
		self.panel_limit = wx.Panel( self.transakcyjny, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		sizer_opcje1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.opcja_limit_ukryty = wx.CheckBox( self.panel_limit, wx.ID_ANY, u"hidden", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje1.Add( self.opcja_limit_ukryty, 0, wx.ALL, 5 )
		
		self.opcja_limit_OCO = wx.CheckBox( self.panel_limit, wx.ID_ANY, u"OCO", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje1.Add( self.opcja_limit_OCO, 0, wx.ALL, 5 )
		
		self.opcja_limit_post = wx.CheckBox( self.panel_limit, wx.ID_ANY, u"post", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje1.Add( self.opcja_limit_post, 0, wx.ALL, 5 )
		
		bSizer141.Add( sizer_opcje1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj1 = wx.BoxSizer( wx.HORIZONTAL )
		
		box_kup1 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, u"kup" ), wx.VERTICAL )
		
		bSizer171 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer19 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText1331 = wx.StaticText( self.panel_limit, wx.ID_ANY, u"ilość", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1331.Wrap( -1 )
		sbSizer19.Add( self.m_staticText1331, 0, wx.ALL, 5 )
		
		self.pole_ilosc_limit_kup = wx.TextCtrl( self.panel_limit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer19.Add( self.pole_ilosc_limit_kup, 0, wx.ALL, 5 )
		
		bSizer171.Add( sbSizer19, 1, wx.EXPAND, 5 )
		
		sbSizer191 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText13311 = wx.StaticText( self.panel_limit, wx.ID_ANY, u"cena", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13311.Wrap( -1 )
		sbSizer191.Add( self.m_staticText13311, 0, wx.ALL, 5 )
		
		self.pole_cena_limit_kup = wx.TextCtrl( self.panel_limit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer191.Add( self.pole_cena_limit_kup, 0, wx.ALL, 5 )
		
		bSizer171.Add( sbSizer191, 1, wx.EXPAND, 5 )
		
		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.button_limit_zakup = wx.Button( self.panel_limit, wx.ID_ANY, u"ZAKUP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer23.Add( self.button_limit_zakup, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer171.Add( sbSizer23, 1, wx.EXPAND, 5 )
		
		box_kup1.Add( bSizer171, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj1.Add( box_kup1, 1, wx.EXPAND, 5 )
		
		box_sprzedaj1 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, u"sprzedaj" ), wx.VERTICAL )
		
		bSizer1711 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer192 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText13312 = wx.StaticText( self.panel_limit, wx.ID_ANY, u"ilość", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13312.Wrap( -1 )
		sbSizer192.Add( self.m_staticText13312, 0, wx.ALL, 5 )
		
		self.pole_ilosc_limit_sprzedaj = wx.TextCtrl( self.panel_limit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer192.Add( self.pole_ilosc_limit_sprzedaj, 0, wx.ALL, 5 )
		
		bSizer1711.Add( sbSizer192, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer1911 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText133111 = wx.StaticText( self.panel_limit, wx.ID_ANY, u"cena", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133111.Wrap( -1 )
		sbSizer1911.Add( self.m_staticText133111, 0, wx.ALL, 5 )
		
		self.pole_cena_limit_sprzedaj = wx.TextCtrl( self.panel_limit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1911.Add( self.pole_cena_limit_sprzedaj, 0, wx.ALL, 5 )
		
		bSizer1711.Add( sbSizer1911, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer231 = wx.StaticBoxSizer( wx.StaticBox( self.panel_limit, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.button_limit_sprzedaz = wx.Button( self.panel_limit, wx.ID_ANY, u"SPRZEDAŻ", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer231.Add( self.button_limit_sprzedaz, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer1711.Add( sbSizer231, 1, wx.EXPAND, 5 )
		
		box_sprzedaj1.Add( bSizer1711, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj1.Add( box_sprzedaj1, 1, wx.EXPAND, 5 )
		
		bSizer141.Add( sizer_kup_sprzedaj1, 0, wx.EXPAND, 5 )
		
		self.panel_limit.SetSizer( bSizer141 )
		self.panel_limit.Layout()
		bSizer141.Fit( self.panel_limit )
		self.transakcyjny.AddPage( self.panel_limit, u"LIMIT", False )
		self.panel_stop = wx.Panel( self.transakcyjny, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1411 = wx.BoxSizer( wx.VERTICAL )
		
		sizer_opcje11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.opcja_stop_ukryty = wx.CheckBox( self.panel_stop, wx.ID_ANY, u"hidden", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opcja_stop_ukryty.SetValue(True) 
		sizer_opcje11.Add( self.opcja_stop_ukryty, 0, wx.ALL, 5 )
		
		self.opcja_stop_OCO = wx.CheckBox( self.panel_stop, wx.ID_ANY, u"OCO", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje11.Add( self.opcja_stop_OCO, 0, wx.ALL, 5 )
		
		self.opcja_stop_post = wx.CheckBox( self.panel_stop, wx.ID_ANY, u"post", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje11.Add( self.opcja_stop_post, 0, wx.ALL, 5 )
		
		bSizer1411.Add( sizer_opcje11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj11 = wx.BoxSizer( wx.HORIZONTAL )
		
		box_kup11 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, u"kup" ), wx.VERTICAL )
		
		bSizer1712 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer193 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText13313 = wx.StaticText( self.panel_stop, wx.ID_ANY, u"ilość", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13313.Wrap( -1 )
		sbSizer193.Add( self.m_staticText13313, 0, wx.ALL, 5 )
		
		self.pole_ilosc_stop_kup = wx.TextCtrl( self.panel_stop, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer193.Add( self.pole_ilosc_stop_kup, 0, wx.ALL, 5 )
		
		bSizer1712.Add( sbSizer193, 1, wx.EXPAND, 5 )
		
		sbSizer1912 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText133112 = wx.StaticText( self.panel_stop, wx.ID_ANY, u"cena", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133112.Wrap( -1 )
		sbSizer1912.Add( self.m_staticText133112, 0, wx.ALL, 5 )
		
		self.pole_cena_stop_kup = wx.TextCtrl( self.panel_stop, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1912.Add( self.pole_cena_stop_kup, 0, wx.ALL, 5 )
		
		bSizer1712.Add( sbSizer1912, 1, wx.EXPAND, 5 )
		
		sbSizer232 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.button_stop_zakup = wx.Button( self.panel_stop, wx.ID_ANY, u"ZAKUP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer232.Add( self.button_stop_zakup, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer1712.Add( sbSizer232, 1, wx.EXPAND, 5 )
		
		box_kup11.Add( bSizer1712, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj11.Add( box_kup11, 1, wx.EXPAND, 5 )
		
		box_sprzedaj11 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, u"sprzedaj" ), wx.VERTICAL )
		
		bSizer17111 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1921 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText133121 = wx.StaticText( self.panel_stop, wx.ID_ANY, u"ilość", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133121.Wrap( -1 )
		sbSizer1921.Add( self.m_staticText133121, 0, wx.ALL, 5 )
		
		self.pole_ilosc_stop_sprzedaj = wx.TextCtrl( self.panel_stop, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1921.Add( self.pole_ilosc_stop_sprzedaj, 0, wx.ALL, 5 )
		
		bSizer17111.Add( sbSizer1921, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer19111 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText1331111 = wx.StaticText( self.panel_stop, wx.ID_ANY, u"cena", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1331111.Wrap( -1 )
		sbSizer19111.Add( self.m_staticText1331111, 0, wx.ALL, 5 )
		
		self.pole_cena_stop_sprzedaj = wx.TextCtrl( self.panel_stop, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer19111.Add( self.pole_cena_stop_sprzedaj, 0, wx.ALL, 5 )
		
		bSizer17111.Add( sbSizer19111, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer2311 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stop, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.button_stop_sprzedaz = wx.Button( self.panel_stop, wx.ID_ANY, u"SPRZEDAŻ", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2311.Add( self.button_stop_sprzedaz, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer17111.Add( sbSizer2311, 1, wx.EXPAND, 5 )
		
		box_sprzedaj11.Add( bSizer17111, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj11.Add( box_sprzedaj11, 1, wx.EXPAND, 5 )
		
		bSizer1411.Add( sizer_kup_sprzedaj11, 0, wx.EXPAND, 5 )
		
		self.panel_stop.SetSizer( bSizer1411 )
		self.panel_stop.Layout()
		bSizer1411.Fit( self.panel_stop )
		self.transakcyjny.AddPage( self.panel_stop, u"STOP", False )
		self.panel_stoplimit = wx.Panel( self.transakcyjny, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1412 = wx.BoxSizer( wx.VERTICAL )
		
		sizer_opcje12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.opcja_stoplimit_ukryty = wx.CheckBox( self.panel_stoplimit, wx.ID_ANY, u"hidden", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje12.Add( self.opcja_stoplimit_ukryty, 0, wx.ALL, 5 )
		
		self.opcja_stoplimit_OCO = wx.CheckBox( self.panel_stoplimit, wx.ID_ANY, u"OCO", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje12.Add( self.opcja_stoplimit_OCO, 0, wx.ALL, 5 )
		
		self.opcja_stoplimit_post = wx.CheckBox( self.panel_stoplimit, wx.ID_ANY, u"post", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_opcje12.Add( self.opcja_stoplimit_post, 0, wx.ALL, 5 )
		
		bSizer1412.Add( sizer_opcje12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj12 = wx.BoxSizer( wx.HORIZONTAL )
		
		box_kup = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, u"kup" ), wx.VERTICAL )
		
		bSizer1713 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer68 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText162 = wx.StaticText( self.panel_stoplimit, wx.ID_ANY, u"cena min.   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )
		sbSizer68.Add( self.m_staticText162, 0, wx.ALL, 5 )
		
		self.pole_cenamin_stoplimit_kup = wx.TextCtrl( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer68.Add( self.pole_cenamin_stoplimit_kup, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer1713.Add( sbSizer68, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer194 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText13314 = wx.StaticText( self.panel_stoplimit, wx.ID_ANY, u"ilość           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13314.Wrap( -1 )
		sbSizer194.Add( self.m_staticText13314, 1, wx.ALL, 5 )
		
		self.pole_ilosc_stoplimit_kup = wx.TextCtrl( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer194.Add( self.pole_ilosc_stoplimit_kup, 0, wx.ALL, 5 )
		
		bSizer1713.Add( sbSizer194, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer1913 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText133113 = wx.StaticText( self.panel_stoplimit, wx.ID_ANY, u"cena maks  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133113.Wrap( -1 )
		sbSizer1913.Add( self.m_staticText133113, 0, wx.ALL, 5 )
		
		self.pole_cenamax_stoplimit_kup = wx.TextCtrl( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1913.Add( self.pole_cenamax_stoplimit_kup, 0, wx.ALL, 5 )
		
		bSizer1713.Add( sbSizer1913, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer233 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.button_stoplimit_zakup = wx.Button( self.panel_stoplimit, wx.ID_ANY, u"ZAKUP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer233.Add( self.button_stoplimit_zakup, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer1713.Add( sbSizer233, 1, wx.EXPAND, 5 )
		
		box_kup.Add( bSizer1713, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj12.Add( box_kup, 1, wx.EXPAND, 5 )
		
		box_sprzedaj = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, u"kup" ), wx.VERTICAL )
		
		bSizer17131 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer681 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText1621 = wx.StaticText( self.panel_stoplimit, wx.ID_ANY, u"cena min.   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1621.Wrap( -1 )
		sbSizer681.Add( self.m_staticText1621, 0, wx.ALL, 5 )
		
		self.pole_cenamin_stoplimit_sprzedaj = wx.TextCtrl( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer681.Add( self.pole_cenamin_stoplimit_sprzedaj, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer17131.Add( sbSizer681, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer1941 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText133141 = wx.StaticText( self.panel_stoplimit, wx.ID_ANY, u"ilość           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133141.Wrap( -1 )
		sbSizer1941.Add( self.m_staticText133141, 1, wx.ALL, 5 )
		
		self.pole_ilosc_stoplimit_sprzedaj = wx.TextCtrl( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1941.Add( self.pole_ilosc_stoplimit_sprzedaj, 0, wx.ALL, 5 )
		
		bSizer17131.Add( sbSizer1941, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer19131 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText1331131 = wx.StaticText( self.panel_stoplimit, wx.ID_ANY, u"cena maks  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1331131.Wrap( -1 )
		sbSizer19131.Add( self.m_staticText1331131, 0, wx.ALL, 5 )
		
		self.pole_cenamax_stoplimit_sprzedaj = wx.TextCtrl( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer19131.Add( self.pole_cenamax_stoplimit_sprzedaj, 0, wx.ALL, 5 )
		
		bSizer17131.Add( sbSizer19131, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer2331 = wx.StaticBoxSizer( wx.StaticBox( self.panel_stoplimit, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.button_stoplimit_sprzedaz = wx.Button( self.panel_stoplimit, wx.ID_ANY, u"SPRZEDAŻ", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2331.Add( self.button_stoplimit_sprzedaz, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer17131.Add( sbSizer2331, 1, wx.EXPAND, 5 )
		
		box_sprzedaj.Add( bSizer17131, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer_kup_sprzedaj12.Add( box_sprzedaj, 1, wx.EXPAND, 5 )
		
		bSizer1412.Add( sizer_kup_sprzedaj12, 0, wx.EXPAND, 5 )
		
		self.panel_stoplimit.SetSizer( bSizer1412 )
		self.panel_stoplimit.Layout()
		bSizer1412.Fit( self.panel_stoplimit )
		self.transakcyjny.AddPage( self.panel_stoplimit, u"STOP LIMIT", False )
		
		bSizer23.Add( self.transakcyjny, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM, 5 )
		
		sbSizer1222 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Portfele" ), wx.VERTICAL )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		sbSizer1222.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		bSizer23.Add( sbSizer1222, 1, wx.TOP|wx.EXPAND, 5 )
		
		bSizer18.Add( bSizer23, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.gielda_choice_box.Bind( wx.EVT_COMBOBOX, self.zmiana_waluty1 )
		self.rynek_choice_box.Bind( wx.EVT_CHOICE, self.zmiana_waluty2 )
		self.market_kup.Bind( wx.EVT_BUTTON, self.info_box )
		self.m_button14.Bind( wx.EVT_BUTTON, self.info_box )
		self.button_limit_zakup.Bind( wx.EVT_BUTTON, self.info_box )
		self.button_limit_sprzedaz.Bind( wx.EVT_BUTTON, self.info_box )
		self.button_stop_zakup.Bind( wx.EVT_BUTTON, self.info_box )
		self.button_stop_sprzedaz.Bind( wx.EVT_BUTTON, self.info_box )
		self.button_stoplimit_zakup.Bind( wx.EVT_BUTTON, self.info_box )
		self.button_stoplimit_sprzedaz.Bind( wx.EVT_BUTTON, self.info_box )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def zmiana_waluty1( self, event ):
		event.Skip()
	
	def zmiana_waluty2( self, event ):
		event.Skip()
	
	def market_zakup_button( self, event ):
		event.Skip()
	
	def market_sprzedaz_button( self, event ):
		event.Skip()
	
	def limit_zakup_button( self, event ):
		event.Skip()
	
	def limit_sprzedaz_button( self, event ):
		event.Skip()
	
	def stop_zakup_button( self, event ):
		event.Skip()
	
	def stop_sprzedaz_button( self, event ):
		event.Skip()
	
	def stoplimit_zakup_button( self, event ):
		event.Skip()
	
	def stoplimit_sprzedaz_button( self, event ):
		event.Skip()
	
