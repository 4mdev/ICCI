
#  File "/Users/se/Desktop/iccy/iccy-v.1.4.6-publicBeta/CC_wyszukiwarka_spreadow.py", line 147, in pobierz_spready
#    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
#UnboundLocalError: local variable 'orderbook' referenced before assignment
#Jezeli jest ban na gieldzie to powinien zzerować wyniki a nie wyswietlac te z błędem (stare)
#######

import operator
import wx
import wx.lib.mixins.listctrl as listmix
import sys
import ccxt
import CC_get_app_patch
#import CC_info_opisy
application_path = CC_get_app_patch.pobierz_app_patch()
global blokuj_insert 
blokuj_insert = False
nr_lini = 0
zbior_rynkow_lista = {}

#nie odjete?
#ccxt.base.errors.RequestTimeout: bittrex, coinex,coinexchange,exx,huobicny,bitfinex,yobit,okcoinusd
#requires api key coinspot, 'xbtce',southxchange
#,braziliex,btcchina,btcexchange,btctradeua,bxinth,cobinhood,coinegg,coinnest,cryptopia,huobi,ice3x,jubi,yunbi,nova,livecoin,lbank

#bitz,bittrex

ma_fetch_all = ['bithumb', 'binance', 'bitfinex', 'kraken', 'luno', 'okex', 'poloniex', 'bitz', 'acx', 'bitlish', 'bleutrade', 'bittrex', 'btctradeim', 'btcturk', 'ccex', 'cex', 'coingi', 'dsx', 'ethfinex', 'exmo', 'gatecoin', 'kucoin', 'kuna', 'liqui', 'quoinex', 'therock', 'wex']

lista_gield = ['gdax','bithumb','binance' , 'bitfinex' ,'kraken','bitflyer','luno','bitstamp','gemini','bitbay','okex','poloniex','coinone','bitz','acx', 'anxpro', 'bit2c', 'bitbank', 'bitkk','bitmex', 'bitlish', 'bitmarket', 'bitso', 'bl3p', 'bleutrade','bittrex', 'btcbox', 'btcmarkets', 'btctradeim', 'btcturk', 'ccex', 'cex', 'chilebit', 'coincheck', 'coinfloor', 'coingi', 'coinmate', 'dsx', 'ethfinex', 'exmo', 'flowbtc', 'foxbit', 'fybse', 'fybsg', 'gatecoin', 'getbtc', 'hadax', 'huobipro', 'independentreserve', 'indodax', 'itbit', 'kucoin', 'kuna', 'liqui', 'lykke', 'mixcoins', 'negociecoins', 'okcoincny', 'paymium', 'quadrigacx', 'quoinex', 'surbitcoin', 'therock', 'tidex', 'vbtc', 'wex', 'zaif', 'zb']
lista_gield.sort()

class SortedListCtrl(wx.ListCtrl, listmix.ColumnSorterMixin):
    
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, style = wx.LC_REPORT, )
        
        self.Bind ( wx.EVT_CLOSE, self.on_close ) # gdy nastapi zamkniecie 

    def on_close1(self,event):
        global czy_wylaczyc
        czy_wylaczyc = True
         
    def tabela(self,gielda_wybrana,data):
        global blokuj_insert 
        self.data = data
        self.itemDataMap = self.data

        if blokuj_insert == False:
            # Spaltenüberschriften
            self.InsertColumn(sys.maxsize, "giełda")
            self.InsertColumn(sys.maxsize, "rynek")
            self.InsertColumn(sys.maxsize, "bid", wx.LIST_FORMAT_RIGHT )
            self.InsertColumn(sys.maxsize, "ask", wx.LIST_FORMAT_RIGHT)
            self.InsertColumn(sys.maxsize, "spread", wx.LIST_FORMAT_RIGHT)
            self.InsertColumn(sys.maxsize, "spread %", wx.LIST_FORMAT_RIGHT)        
        
            l = 100
            self.SetColumnWidth(0, 160)
            self.SetColumnWidth(1, l)
            self.SetColumnWidth(2, l)
            self.SetColumnWidth(3, l)
            self.SetColumnWidth(4, l)
            self.SetColumnWidth(5, l)

        blokuj_insert = True

        # wypisanie danych w tabeli

        for key in sorted(self.data.keys()):
            gielda_tabela, market_tabela, bid_tabela, ask_tabela, spread_tabela,spread_proc_tabela = self.data[key]
            index = self.InsertItem(sys.maxsize, gielda_tabela)
            self.SetItemData(index, key) #muss sein
            self.SetItem(index, 1, str(market_tabela))
            self.SetItem(index, 2, str(bid_tabela))
            self.SetItem(index, 3, str(ask_tabela))
            self.SetItem(index, 4, str(spread_tabela))
            self.SetItem(index, 5, str(spread_proc_tabela))
            
            index += 1

        listmix.ColumnSorterMixin.__init__(self, numColumns = 6)

    def GetListCtrl(self):
        return self

    def zamek(self):
        self.Destroy()

    def on_close ( self, event ):
        #print('onclose')
        self.Destroy()

class MyFrame(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.Bind ( wx.EVT_CLOSE, self.on_close ) # gdy nastapi zamkniecie 

        
        vbox_main = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox_main)
        
        boxInfo = wx.BoxSizer(wx.VERTICAL)
        vbox_main.Add(boxInfo,0,wx.ALL|wx.EXPAND,20) 

        self.conf_btn_portfele = wx.BitmapButton( self, -1, wx.Bitmap(u''+application_path+"/ikony_dashboard/znak_zapytania.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        boxInfo.Add( self.conf_btn_portfele, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        self.conf_btn_portfele.Bind( wx.EVT_BUTTON, self.info_app )

        self.rynek_choice_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lista_gield, 0 )
        self.rynek_choice_box.SetSelection( 0 )
        boxInfo.Add( self.rynek_choice_box, 0, wx.ALL, 5 )

        self.btn_szukaj = wx.Button(self, 10, "pobierz / odśwież")
        boxInfo.Add(self.btn_szukaj , 0, wx.ALL|wx.ALIGN_LEFT) 
        self.btn_szukaj.Bind(wx.EVT_BUTTON,self.OnClicked)

        self.live_checkbox = wx.CheckBox( self, wx.ID_ANY, u"Live!", wx.DefaultPosition, wx.DefaultSize, 0 )
        boxInfo.Add( self.live_checkbox, 0, wx.ALL, 5 )
        self.live_checkbox.Bind( wx.EVT_CHECKBOX, self.funkcja_live )
                
        self.reload_text = wx.StaticText(self, )
        boxInfo.Add(self.reload_text, 0, wx.EXPAND)


        self.my_list = SortedListCtrl(self)
        vbox_main.Add(self.my_list, 1, wx.EXPAND | wx.ALL, 10)
        
    def tt(self):
        print('tt')
        if self.live_checkbox.GetValue() == True:
            self.OnClicked(wx.EVT_BUTTON)
            self.funkcja_live(wx.EVT_CHECKBOX)

    def funkcja_live(self,event):
        print('funkcja_live')
        live_checkbox_value = self.live_checkbox.GetValue()
        print(live_checkbox_value)
        if live_checkbox_value == True:
            gielda_wybrana = self.rynek_choice_box.GetStringSelection() 
            exchange = eval('ccxt.'+gielda_wybrana+ '()')
            #rateLimit = float(exchange.rateLimit) 
            #ilosc_rynkow = len(exchange.load_markets ())
            #print('rateLimit',rateLimit)

            #import locale
            #locale.setlocale(locale.LC_TIME, "sv_SE")
            #import datetime
            #today = datetime.date.today()
            import time
            formatted_time = time.strftime("%H:%M:%S")
            #print (time.strftime("%a, %d %b %Y))

            rateLimit = 15
            
            self.reload_text.SetLabel(str('Ostatnia akualizacja: ' + formatted_time + '   (co %s s.)' %rateLimit ))
            
            wx.CallLater(int(rateLimit*1000), self.tt)#self.funkcja_live(wx.EVT_CHECKBOX))
                
        if live_checkbox_value == False:
            self.reload_text.SetLabel(str(''))
            pass


    def on_close1(self,event):
        global czy_wylaczyc
        czy_wylaczyc = True

    def pobierz_spready(self,gielda_wybrana):
        try:
            zbior_rynkow_lista = {}
            global wiersze_do_wyswietlenia
            exchange = eval('ccxt.'+gielda_wybrana+ '()')
            exchange.load_markets ()
            spread_exchange = []
            ilosc_rynkow = len(exchange.symbols)

            dlgPro = wx.ProgressDialog(u"Pobieranie:",
                                        u"łączę",
                                        ilosc_rynkow,
                                        None,
                                        wx.PD_APP_MODAL|
                                        wx.PD_AUTO_HIDE )
            dlgPro.Bind ( wx.EVT_CLOSE, self.on_close1 ) # gdy nastapi zamkniecie 
            
            wiersze_do_wyswietlenia ={}
            w = 0
            global czy_wylaczyc 
            czy_wylaczyc = False

            
            if gielda_wybrana in ma_fetch_all:
                ob = exchange.fetch_tickers()
                for mark in exchange.symbols:
                    if czy_wylaczyc == False:
                        w +=1
                        try:
                            bid_ask = ob[mark]
                            bid = bid_ask['bid']
                            ask = bid_ask['ask']

                            dlgPro.Update(w, str(w)+ '/' + str(ilosc_rynkow)+ '  ' + str(mark))
                            wx.Yield()
                        
                            spread = (ask - bid) if (bid and ask) else None
                            spread_proc_tabela = (ask * 100 / bid - 100) if (bid and ask) else None
                        
                        except:
                            blad = ('Error: {}'.format(sys.exc_info()[0]))
                            bid = 0
                            ask = 0
                            spread = 0
                            spread_proc_tabela = 0
                            dlgPro.Update(w, str(w)+ '/' + str(ilosc_rynkow)+ '  ' + str(mark) + ' !błąd' )
                            wx.Yield()
                        
                        #############

                    try:
                        spread_proc_tabela = round(spread_proc_tabela,2)
                    except:
                        pass

                    spread_market = {
                        'exchange':exchange.id,
                        'market':mark,
                        'bid': bid, 
                        'ask': ask, 
                        'spread': spread,
                        'spread_proc_tabela':spread_proc_tabela

                        }
                    spread_exchange.append(spread_market)

            else:
            

                ### pojedyncze pobieranie orderbook dla kazdego marketu
                for mark in exchange.symbols:
                    if czy_wylaczyc == False:
                        w +=1
                        try:
                            czy_wylaczyc = False
                            orderbook = exchange.fetch_order_book (mark)
                            dlgPro.Update(w, str(w)+ '/' + str(ilosc_rynkow)+ '  ' + str(mark))
                            wx.Yield()
                        
                            bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
                            ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
                            spread = (ask - bid) if (bid and ask) else None
                            spread_proc_tabela = (ask * 100 / bid - 100) if (bid and ask) else None

                        except:
                            blad = ('Error: {}'.format(sys.exc_info()[0]))
                            bid = 0
                            ask = 0
                            spread = 0
                            spread_proc_tabela = 0
                            dlgPro.Update(w, str(w)+ '/' + str(ilosc_rynkow)+ '  ' + str(mark) + ' !błąd' )
                            wx.Yield()

                        #############

                        try:
                            spread_proc_tabela = round(spread_proc_tabela,2)
                        except:
                            pass

                        spread_market = {
                            'exchange':exchange.id,
                            'market':mark,
                            'bid': bid, 
                            'ask': ask, 
                            'spread': spread,
                            'spread_proc_tabela':spread_proc_tabela

                            }
                        spread_exchange.append(spread_market)
                        #spread_market = {}

                    else:
                        dlgPro.Update(w, str(w)+ '/' + str(ilosc_rynkow)+ '  ' + str(mark) + ' !błąd' )
                        wx.Yield()
            nr_lini = 1
            wiersze_do_wyswietlenia ={}

            nowy_spread_exchange = []
            for spr in spread_exchange:
                if spr['spread'] != None:
                    nowy_spread_exchange.append(spr)
                
            spread_exchange = nowy_spread_exchange
            spread_exchange.sort(key=operator.itemgetter('spread_proc_tabela'))
            spread_exchange = spread_exchange[::-1]

            for a in spread_exchange:
                gielda_tabela = a['exchange']
                market_tabela = a['market']
                bid_tabela = a['bid']
                ask_tabela = a['ask']
                spread_tabela = a['spread']
            
                try:
                    spread_proc_tabela = ask_tabela * 100 / bid_tabela - 100
                    spread_proc_tabela = round(spread_proc_tabela,2)

                except:
                    spread_proc_tabela = 0
                
                try:
                    spread_tabela = round(spread_tabela,8)
                except:
                    pass

                
                wiersz = (gielda_tabela, market_tabela, spread_tabela,spread_proc_tabela)
                wiersze_do_wyswietlenia.update({nr_lini:wiersz})

                #print(gielda_tabela, market_tabela, bid_tabela,ask_tabela,spread_tabela,spread_proc_tabela)

                if bid_tabela and ask_tabela !=0:
                    zbior_rynkow_lista[nr_lini] = (gielda_tabela, market_tabela, float(bid_tabela),float(ask_tabela), float(spread_tabela), float(spread_proc_tabela))
                    nr_lini += 1

            #print('zbior_rynkow_lista',zbior_rynkow_lista)
            return zbior_rynkow_lista
            
        except Exception as inst:     
            er =   gielda_wybrana + ' {"error":"ERR_RATE_LIMIT"}'
            
            if str(inst) == str(er):
                er1 = 'przekroczony limit połączeń'
            
                zbior_rynkow_lista = {
                    1: (str(er1), '', 0, 0, 0, 0),
                    2: ('spróbuj za chwilę', '', 0, 0, 0, 0)
                    }
            
            else:
                zbior_rynkow_lista = {
                    1: (str(inst), '', 0, 0, 0, 0),
                    2: ('spróbuj za chwilę', '', 0, 0, 0, 0)
                    }

            return zbior_rynkow_lista
        

    def OnClicked(self,event):
        wybrana_gielda = self.rynek_choice_box.GetStringSelection() 
        ilosc_wierszy = self.my_list.GetItemCount()

        self.data = self.pobierz_spready(wybrana_gielda)
        
        # czyszczenie listy
        try:
            for item in range(ilosc_wierszy):
                self.my_list.DeleteItem(0)
        except:
            pass
        
        self.itemDataMap = self.data
        data = self.data
        
        SortedListCtrl.tabela(self.my_list,wybrana_gielda,data)

    def on_close ( self, event ):
        self.Destroy()
        SortedListCtrl.zamek(self)

    def info_app(self,event):
        text_dbox = 'Funkcja wyświetla spready bid/ask dla poszczególnych rynków wybranej giełdy.\n\nW przypadku przekroczenia limitu połączeń (różnego dla każdej giełdy) funkcja zwróci wyniki częściowe.\n\nPo zaznaczeniu opcji LIVE funkcja udostępnia możliwość automatycznej aktualizacji danych. '
        title_dbox = 'Spready v. 0.1'
        wx.MessageBox(text_dbox, title_dbox ,wx.OK | wx.ICON_INFORMATION)  


def main():
    """Testing"""
    app = wx.App()
    f = MyFrame()
    f.Center()
    f.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()