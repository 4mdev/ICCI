import wx
#import CC_Panel_Gieldowy_gui
import icci_trading_panel_gui as CC_Panel_Gieldowy_gui

import ccxt
import sys   
import urllib
import CC_bbay_offerts
from wx.adv import BitmapComboBox   # Phoenix
import CC_info_opisy
import time
valid_list = ['gdax','bithumb','binance','kraken','bitflyer','luno','bitfinex','bitstamp','gemini','bitbay','okex','poloniex','huobi','coinone','bitz',]

import CC_kalkulator
 

class Panel_Gieldowy(CC_Panel_Gieldowy_gui.Panel_Gieldowy):

    def __init__(self,parent):

        CC_Panel_Gieldowy_gui.Panel_Gieldowy.__init__(self,parent)
        url_chart = 'https://icci.info/wykres'
        #self.wykres_htmlWin4.LoadURL(url_chart)
        
    def kalkulator_start(self,event):
        ##print('kalkulator')
        CC_kalkulator.Kalkulator(None).Show()

    def zmiana_wykresu(self):
        gielda = self.gielda_choice_box.GetStringSelection() 
        self.rynek_choice_box.SetSelection( 0 )
        market = self.rynek_choice_box.GetStringSelection()
        
        try:
            if gielda == 'bitfinex':
                if market == 'BTC/USD':
                    url_chart = 'https://icci.info/wykres'
                    self.wykres_htmlWin4.LoadURL(url_chart)
            else:
                url_chart = url_chart = 'https://www.icci.info/wp-content/uploads/2018/06/soon.jpg'
                self.wykres_htmlWin4.LoadURL(url_chart)

        except:
            print('brak wykresu')


    def zmiana_waluty1(self,event):
        print('zmiana valuty 1')

        gielda = self.gielda_choice_box.GetStringSelection()
        #print('gielda')
        if gielda in valid_list:

            exchange = eval('ccxt.' + gielda + '()')
            
            try:
                if gielda == 'bitfinex':
                    rynki = ['BTC/USD', 'LTC/USD', 'LTC/BTC', 'ETH/USD', 'ETH/BTC', 'ETC/BTC', 'ETC/USD', 'RRT/USD', 'RRT/BTC', 'ZEC/USD', 'ZEC/BTC', 'XMR/USD', 'XMR/BTC', 'DASH/USD', 'DASH/BTC', 'BTC/EUR', 'BTC/JPY', 'XRP/USD', 'XRP/BTC', 'IOTA/USD', 'IOTA/BTC', 'IOTA/ETH', 'EOS/USD', 'EOS/BTC', 'EOS/ETH', 'SAN/USD', 'SAN/BTC', 'SAN/ETH', 'OMG/USD', 'OMG/BTC', 'OMG/ETH', 'BCH/USD', 'BCH/BTC', 'BCH/ETH', 'NEO/USD', 'NEO/BTC', 'NEO/ETH', 'ETP/USD', 'ETP/BTC', 'ETP/ETH', 'QTUM/USD', 'QTUM/BTC', 'QTUM/ETH', 'AVT/USD', 'AVT/BTC', 'AVT/ETH', 'EDO/USD', 'EDO/BTC', 'EDO/ETH', 'BTG/USD', 'BTG/BTC', 'DATA/USD', 'DATA/BTC', 'DATA/ETH', 'QASH/USD', 'QASH/BTC', 'QASH/ETH', 'YOYOW/USD', 'YOYOW/BTC', 'YOYOW/ETH', 'GNT/USD', 'GNT/BTC', 'GNT/ETH', 'SNT/USD', 'SNT/BTC', 'SNT/ETH', 'IOTA/EUR', 'BAT/USD', 'BAT/BTC', 'BAT/ETH', 'MANA/USD', 'MANA/BTC', 'MANA/ETH', 'FUN/USD', 'FUN/BTC', 'FUN/ETH', 'ZRX/USD', 'ZRX/BTC', 'ZRX/ETH', 'TNB/USD', 'TNB/BTC', 'TNB/ETH', 'SPANK/USD', 'SPANK/BTC', 'SPANK/ETH', 'TRX/USD', 'TRX/BTC', 'TRX/ETH', 'RCN/USD', 'RCN/BTC', 'RCN/ETH', 'RLC/USD', 'RLC/BTC', 'RLC/ETH', 'AID/USD', 'AID/BTC', 'AID/ETH', 'SNGLS/USD', 'SNGLS/BTC', 'SNGLS/ETH', 'REP/USD', 'REP/BTC', 'REP/ETH', 'ELF/USD', 'ELF/BTC', 'ELF/ETH', 'BTC/GBP', 'ETH/EUR', 'ETH/JPY', 'ETH/GBP', 'NEO/EUR', 'NEO/JPY', 'NEO/GBP', 'EOS/EUR', 'EOS/JPY', 'EOS/GBP', 'IOTA/JPY', 'IOTA/GBP', 'IOS/USD', 'IOS/BTC', 'IOS/ETH', 'AIO/USD', 'AIO/BTC', 'AIO/ETH', 'REQ/USD', 'REQ/BTC', 'REQ/ETH', 'RDN/USD', 'RDN/BTC', 'RDN/ETH', 'LRC/USD', 'LRC/BTC', 'LRC/ETH', 'WAX/USD', 'WAX/BTC', 'WAX/ETH', 'DAI/USD', 'DAI/BTC', 'DAI/ETH', 'CFI/USD', 'CFI/BTC', 'CFI/ETH', 'AGI/USD', 'AGI/BTC', 'AGI/ETH', 'BFT/USD', 'BFT/BTC', 'BFT/ETH', 'MTN/USD', 'MTN/BTC', 'MTN/ETH', 'ODE/USD', 'ODE/BTC', 'ODE/ETH', 'ANT/USD', 'ANT/BTC', 'ANT/ETH', 'DTH/USD', 'DTH/BTC', 'DTH/ETH', 'MIT/USD', 'MIT/BTC', 'MIT/ETH', 'STJ/USD', 'STJ/BTC', 'STJ/ETH', 'XLM/USD', 'XLM/EUR', 'XLM/JPY', 'XLM/GBP', 'XLM/BTC', 'XLM/ETH', 'XVG/USD', 'XVG/EUR', 'XVG/JPY', 'XVG/GBP', 'XVG/BTC', 'XVG/ETH', 'BCI/USD', 'BCI/BTC', 'MKR/USD', 'MKR/BTC', 'MKR/ETH', 'VEN/USD', 'VEN/BTC', 'VEN/ETH', 'KNC/USD', 'KNC/BTC', 'KNC/ETH', 'POA/USD', 'POA/BTC', 'POA/ETH', 'LYM/USD', 'LYM/BTC', 'LYM/ETH', 'UTK/USD', 'UTK/BTC', 'UTK/ETH', 'VEE/USD', 'VEE/BTC', 'VEE/ETH', 'DAD/USD', 'DAD/BTC', 'DAD/ETH']
                else:
                    markets = (exchange.load_markets ())
                    rynki = list(exchange.markets.keys())    #print (exchange.id, symbols) 
                
                self.rynek_choice_box.Clear()
                print('rynek_choice_box')
                self.rynek_choice_box.Append(rynki)
            
            except:
                print('błąd - gielda')

            self.zmiana_wykresu()
        else:
            pass

    def zmiana_waluty2(self,event):
        #self.saldo_portfela()
        #self.lista_ofert()
        self.zmiana_wykresu()

    def info_box(self,event):
        text_dbox = CC_info_opisy.panel_gieldowy_info
        title_dbox = CC_info_opisy.panel_gieldowy_title
        wx.MessageBox(text_dbox, title_dbox ,wx.OK | wx.ICON_INFORMATION )  



if __name__ == "__main__":

    app = wx.App(False)
    frame = Panel_Gieldowy(None)
    frame.Show(True)
    app.MainLoop()
