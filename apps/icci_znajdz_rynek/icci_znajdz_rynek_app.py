import ccxt
import wx
import sys
from wx.lib.mixins.listctrl import ColumnSorterMixin
import os
import CC_get_app_patch
import CC_info_opisy

application_path = CC_get_app_patch.pobierz_app_patch()

global pierwsza_waluta_do_pary,druga_waluta_do_pary
pierwsza_waluta_do_pary = ''
druga_waluta_do_pary = ''


def pobierz_pary_walutowe():
    pobrane_markety_wyszukiwarka = eval(open(application_path+"/apps/icci_wyszukiwarka_rynkow/rynki.txt", 'r').read())
    return pobrane_markety_wyszukiwarka

def znajdz_pare_walutowa(para_walutowa_do_znalezienia='',para_walutowa_do_znalezienia_odwrotna=''):

    znaleziona_poj_na_gieldzie = []
    znaleziona_poj_na_gieldzie_odwrotna = []

    for gieldy1 in pobrane_markety_wyszukiwarka:        
        if [y for y in gieldy1[1] if para_walutowa_do_znalezienia in y]:
            mam = [gieldy1[0],[y for y in gieldy1[1] if para_walutowa_do_znalezienia in y]]
            znaleziona_poj_na_gieldzie.append(mam)

        if [y for y in gieldy1[1] if para_walutowa_do_znalezienia_odwrotna in y]:
            mam1 = [gieldy1[0],[y for y in gieldy1[1] if para_walutowa_do_znalezienia_odwrotna in y]]
            znaleziona_poj_na_gieldzie_odwrotna.append(mam1)
                
    return znaleziona_poj_na_gieldzie, znaleziona_poj_na_gieldzie_odwrotna

def podaj_pare_walutowa_do_znalezienia():
    global pierwsza_waluta_do_pary,druga_waluta_do_pary

    para_walutowa_do_znalezienia = pierwsza_waluta_do_pary + '/' + druga_waluta_do_pary
    para_walutowa_do_znalezienia_odwrotna = druga_waluta_do_pary + '/' + pierwsza_waluta_do_pary

    znaleziona_poj_na_gieldzie, znaleziona_poj_na_gieldzie_odwrotna = znajdz_pare_walutowa(para_walutowa_do_znalezienia.upper(),para_walutowa_do_znalezienia_odwrotna.upper())

    return para_walutowa_do_znalezienia ,para_walutowa_do_znalezienia_odwrotna , znaleziona_poj_na_gieldzie, znaleziona_poj_na_gieldzie_odwrotna


def wyszukiwanie_par_gieldowych_start():

    para_walutowa_do_znalezienia,para_walutowa_do_znalezienia_odwrotna , znaleziona_poj_na_gieldzie, znaleziona_poj_na_gieldzie_odwrotna = podaj_pare_walutowa_do_znalezienia()

    wszystkie_znalezione_pary = [ 

    [para_walutowa_do_znalezienia , znaleziona_poj_na_gieldzie],
    [para_walutowa_do_znalezienia_odwrotna , znaleziona_poj_na_gieldzie_odwrotna]
    
    ]

    nr_lini = 1
    wiersze_do_wyswietlenia ={}
    
    for a in wszystkie_znalezione_pary:
        nazwa_pary_szukanej = a[0]
        wszystkie_gielda_i_waluty = a[1]
        
        for market in wszystkie_gielda_i_waluty:            
            nazwa_marketu = market[0]            
            symbole_marketu =  market[1]

            for symbol in symbole_marketu:
                wiersz = (nazwa_pary_szukanej, nazwa_marketu, symbol)
                wiersze_do_wyswietlenia.update({nr_lini:wiersz})
                nr_lini+=1
    
    #print(wiersze_do_wyswietlenia)
    return wiersze_do_wyswietlenia

def wyszukiwarka_rynkow_start():
    global wszystkie_gieldy
    global pobrane_markety_wyszukiwarka
    pobrane_markety_wyszukiwarka = pobierz_pary_walutowe()      

wyszukiwarka_rynkow_start()
wiersze_do_wyswietlenia = wyszukiwanie_par_gieldowych_start()
#print(wiersze_do_wyswietlenia)

class SortedListCtrl(wx.ListCtrl, ColumnSorterMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ColumnSorterMixin.__init__(self, len(wiersze_do_wyswietlenia))
        self.itemDataMap = wiersze_do_wyswietlenia

    def GetListCtrl(self):
        return self

class ListaWalutKlasa(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title = 'wyszukiwarka rynków', size=(460, 560))

        self.Bind ( wx.EVT_CLOSE, self.on_close ) # gdy nastapi zamkniecie 

        hbox = wx.BoxSizer(wx.VERTICAL)

        boxInfo = wx.BoxSizer(wx.VERTICAL)
        hbox.Add(boxInfo,0,wx.ALL|wx.EXPAND,20) 

        boxWyboru = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(boxWyboru,0,wx.ALL|wx.EXPAND,20) 


        panel = wx.Panel(self, -1)


        # info box
        self.conf_btn_portfele = wx.BitmapButton( panel, -1, wx.Bitmap(u''+application_path+"/apps/icci_wyszukiwarka_rynkow/znak_zapytania.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
        boxInfo.Add( self.conf_btn_portfele, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        self.conf_btn_portfele.Bind( wx.EVT_BUTTON, self.info_app )


        # box wyboru waluty
        self.wybierz_label = wx.StaticText(panel, -1, 'I waluta: ') 
        boxWyboru.Add(self.wybierz_label,0,wx.ALL) 

        self.waluta1 = wx.TextCtrl ( panel,-1)
        boxWyboru.Add(self.waluta1 , 0,wx.ALL) 

        self.wybierz_label = wx.StaticText(panel, -1, '   II waluta: ') 
        boxWyboru.Add(self.wybierz_label,0,wx.ALL) 

        self.waluta2 = wx.TextCtrl ( panel,-1)
        boxWyboru.Add(self.waluta2 , 0,wx.ALL) 

        self.przerwa = wx.StaticText(panel, -1, '  ') 
        boxWyboru.Add(self.przerwa,0,wx.ALL) 

        self.btn_szukaj = wx.Button(panel, 10, "szukaj")
        boxWyboru.Add(self.btn_szukaj , 0,wx.ALL) 

        self.btn_szukaj.Bind(wx.EVT_BUTTON,self.OnClicked) 


        #lista
        self.list = SortedListCtrl(panel)
        self.list.InsertColumn(0, 'Poszukiwana para', wx.LIST_FORMAT_CENTER, 140)
        self.list.InsertColumn(1, 'Giełda', wx.LIST_FORMAT_CENTER, 140)
        self.list.InsertColumn(2, 'Znaleziona para', wx.LIST_FORMAT_CENTER, 140)


        global items
        items = wiersze_do_wyswietlenia.items()

        for key, data in items:
            index = self.list.InsertItem(sys.maxsize, data[0])
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2, data[2])
            self.list.SetItemData(index, key)

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        bSizer1.Add( panel, 1, wx.EXPAND, 5 )


        #self.m_checkBox1 = wx.CheckBox(panel, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
        #hbox.Add(self.m_checkBox1, 1, wx.EXPAND)
        #panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

    def on_close ( self, event ):
        #print('onclose destroy')
        self.Destroy()

    def OnClicked(self, event): 

        global pierwsza_waluta_do_pary,druga_waluta_do_pary
        global items

        btn = event.GetEventObject().GetLabel() 
        #print("Label of pressed button = ",btn )
        if btn == 'szukaj':
            pierwsza_waluta_do_pary = self.waluta1.GetValue()
            druga_waluta_do_pary = self.waluta2.GetValue()

            # odswiezyc tabele
            for item in items:

                self.list.DeleteItem(0)

            wiersze_do_wyswietlenia = wyszukiwanie_par_gieldowych_start()
            items = wiersze_do_wyswietlenia.items()

            for key, data in items:
                index = self.list.InsertItem(sys.maxsize, data[0])
                self.list.SetItem(index, 1, data[1])
                self.list.SetItem(index, 2, data[2])
                self.list.SetItemData(index, key)

    def info_app(self,event):
        text_dbox = 'Funkcja umożliwia odnalezienie giełdy dla wskazanej przez użytkownika pary walutowej lub pojedynczej waluty.\n\n W obecnej wersji aplikacja przeszukuje około 100 giełd i kantorów. Ilość ta będzie na bieżąco updatowana.\n'
        title_dbox = 'Znajdź rynek'
        wx.MessageBox(text_dbox, title_dbox ,wx.OK | wx.ICON_INFORMATION)  


def main():
    wyszukiwarka_rynkow_start()
    wiersze_do_wyswietlenia = wyszukiwanie_par_gieldowych_start()
    #print(wiersze_do_wyswietlenia)
    wyszukiwarkaApp = wx.App()
    ListaWalutKlasa(None, -1, 'wiersze_do_wyswietlenia')
    wyszukiwarkaApp.MainLoop()

if __name__ == "__main__":
    main()