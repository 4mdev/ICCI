#clientid 906_3e8w8a4nox6ogk0gs8c4k88wsk4o4g4w80c0k8040wcg0csc0k
#client secret 6cz6n3bwr2o84g0g04ws8o80coc08cgoss4s4koksw0s4ocg00

import coinmarketcal
 
#token = 'BTC'
# Get Token
#token = (coinmarketcal.getToken('906_3e8w8a4nox6ogk0gs8c4k88wsk4o4g4w80c0k8040wcg0csc0k', '6cz6n3bwr2o84g0g04ws8o80coc08cgoss4s4koksw0s4ocg00'))['access_token']

# Get coins list
#print(coinmarketcal.getCoins(token))
#print(coin_list)
# Get categories list
#(coinmarketcal.getCategories(token))
# Get default events
#events_coinmarketcal = coinmarketcal.getEvents(token)


##############################################

import wx
import datetime
from datetime import timedelta

import requests
import re
import operator
from pathlib import Path

import CC_events_GUI
import CC_get_app_patch
application_path = CC_get_app_patch.pobierz_app_patch()

token = (coinmarketcal.getToken('906_3e8w8a4nox6ogk0gs8c4k88wsk4o4g4w80c0k8040wcg0csc0k', '6cz6n3bwr2o84g0g04ws8o80coc08cgoss4s4koksw0s4ocg00'))['access_token']
print(token)

class Kalendarz(CC_events_GUI.Events_Panel):

    def __init__(self,parent):
        #initialize parent class
        CC_events_GUI.Events_Panel.__init__(self,parent)

        self.Bind ( wx.EVT_CLOSE, self.on_close ) # gdy nastapi zamkniecie 
        self.kategorie = coinmarketcal.getCategories(token)
        self.dane_do_wyboru_coinmarketcall()
        self.wybor_kalendarza.Bind( wx.EVT_CHOICE, self.zmiana_kalendarza_funkcja )

    def zmiana_kalendarza_funkcja(self,event):
        kalendarz = self.wybor_kalendarza.GetStringSelection()
        if kalendarz == 'CoinMarketCall':
            self.dane_do_wyboru_coinmarketcall()
        elif kalendarz == 'Coindar':
            self.dane_do_wyboru_coindar()
              
    def dane_do_wyboru_coindar(self):
        self.wybor_waluty.Clear()
        self.sortowanie.Clear()
        self.wybor_waluty.AppendItems(['1','2'])
        self.wybor_kategorii.Clear()
        self.filtr.Clear()

    def set_finish_date(self,now):
        try:
            next_month = (now.replace(day=1) + timedelta(days=31)).replace(day=now.day)
        except ValueError:  # January 31 will return last day of February.
            next_month = (now + timedelta(days=31)).replace(day=1) - timedelta(days=1)
        self.finish_date.SetValue(next_month)

    def dane_do_wyboru_coinmarketcall(self):

        now = datetime.datetime.now()
        # uzupelnienie choice boxow        
        self.start_date.SetValue(now)
        self.set_finish_date(now)
        
        #coin
        c_list = []
        coin_list = coinmarketcal.getCoins(token)
        
        for c in coin_list:
            id_c = c['id']
            c_list.append(id_c)

        c_list.sort()
        c_list.insert(0,'coin')

        self.wybor_waluty.Clear()
        self.wybor_waluty.AppendItems(c_list)
        self.wybor_waluty.SetSelection(0)

        #kategorie self.kategorie - wszystkie
        # kategorie sprawdzic po nazwie i dopasowac kategorię
        self.kategorie_choices= []
  
        print(self.kategorie)

        for k in self.kategorie:
            id_c = k['name']
            self.kategorie_choices.append(id_c)
        
        self.kategorie_choices.sort()
        self.kategorie_choices.insert(0,'kategoria')
        self.wybor_kategorii.AppendItems(self.kategorie_choices)
        self.wybor_kategorii.SetSelection(0)

        #sortowanie         #created_desc,hot_events
        sortowanie_choices = ['sortowanie','data utworzenia','polecane']
        self.sortowanie.AppendItems(sortowanie_choices)

        #filtr   #hot_events
        filtr_choices = [ "filtr - wszystkie", "gorące", ]
        self.filtr.AppendItems(filtr_choices)


    def kalendarz_pokaz_funkcja(self,event):
        #pobieranie danych z wxChoice
        kalendarz = self.wybor_kalendarza.GetStringSelection()
        if kalendarz == 'CoinMarketCall':
            self.kalendarz_pokaz_funkcja_coinmarketcall()
        elif kalendarz == 'Coindar':

            start_date, finish_date = self.start_finish_date()
            print('start_date',start_date,'finish_date',finish_date)
            start_date = start_date.split('/')
            finish_date = finish_date.split('/')
            
            print(start_date,finish_date)
            sorter_start_date = str(start_date[2]) + str(start_date[1]) + str(start_date[0])
            sorter_finish_date = str(finish_date[2]) + str(finish_date[1]) + str(finish_date[0])

            print(sorter_start_date,sorter_finish_date)
            rodzaj_eventow = self.wybor_waluty.GetSelection()
            cd = Coindar()
            source = cd.wyswietlanie(sorter_start_date,sorter_finish_date,rodzaj_eventow)
            
            self.wyswietlanie(source)
        
    def start_finish_date(self):

        start_d = self.start_date.GetValue()

        start_d_day = str(start_d.day) 
        if len(start_d_day) == 1:
            start_d_day = '0'+str(start_d_day)
        else:
            start_d_day = str(start_d_day)
        
        start_d_month = str(start_d.month+1)
        if len(start_d_month) == 1:
            start_d_month = '0'+str(start_d_month)
        else:
            start_d_month = str(start_d_month)

        start_d_year = str(start_d.year)

        start_d = start_d_day + '/' + start_d_month + '/' + start_d_year

        finish_d = self.finish_date.GetValue()
        finish_d_day = str(finish_d.day) 
        if len(finish_d_day) == 1:
            finish_d_day = '0'+str(finish_d_day)
        else:
            finish_d_day = str(finish_d_day)
        
        finish_d_month = str(finish_d.month+1)
        if len(finish_d_month) == 1:
            finish_d_month = '0'+str(finish_d_month)
        else:
            finish_d_month = str(finish_d_month)

        finish_d_year = str(finish_d.year)

        finish_d = finish_d_day + '/' + finish_d_month + '/' + finish_d_year

        return start_d, finish_d

    def kalendarz_pokaz_funkcja_coinmarketcall(self):
        coin = self.wybor_waluty.GetSelection()
        print('1',coin)
        sortowanie = self.sortowanie.GetSelection()
        filtr = self.filtr.GetSelection()

        #pobieranie wartości pól 
        kalendarz = self.wybor_kalendarza.GetStringSelection()

        #kategoria id
        kategoria = self.wybor_kategorii.GetSelection()
        print('kategoria',kategoria)
        if kategoria == 0:
            kategoria = None
        
        elif kategoria != 0:
            for k in self.kategorie:
                if k['name'] == self.wybor_kategorii.GetStringSelection():
                    kategoria = k['id']

        print('kategoria',kategoria)

        #wybor waluty

        if coin != 0:
            coin = self.wybor_waluty.GetStringSelection()
            print('##2',coin)
        elif coin == 0:
            coin = None
            print('##3',coin)
            
            
        if sortowanie != 0:
            sortowanie = self.sortowanie.GetStringSelection()
            if sortowanie == 'data utworzenia':
                sortowanie = 'created_desc'
            elif sortowanie == 'polecane':
                sortowanie = 'hot_events' 
        if sortowanie == 0:
            sortowanie = None
        
        print('sortowanie',sortowanie)


        if filtr != 0:
            filtr = self.filtr.GetStringSelection()
            if filtr == 'gorące':
                filtr = 'hot_events'
            else:
                 filtr = None
        elif filtr == 0:
            filtr = None

        start_d, finish_d = self.start_finish_date()

        if self.start_date.GetValue() <= self.finish_date.GetValue():
            self.pobranie_eventow_coinmarketcall(kalendarz,coin,kategoria,sortowanie,filtr,start_d,finish_d)

        else:
            wx.MessageBox('Data startu jest późniejsza niż data zakończenia.', 'Błąd.' ,wx.OK | wx.ICON_INFORMATION)  

    def pobierz_dane(self,pg, kalendarz,coin,kategoria,sortowanie,filtr,start_d,finish_d):

        eventy = (coinmarketcal.getEvents(token, page=pg, max=150, dateRangeStart=start_d, dateRangeEnd=finish_d, coins=coin, categories=kategoria, sortBy=sortowanie, showOnly=filtr))
        return eventy

    def pobranie_eventow_coinmarketcall(self,kalendarz,coin,kategoria,sortowanie,filtr,start_d,finish_d):
        print('pobranie_eventow_coinmarketcall')
        #import coinmarketcal

        pg = 1
        
        eventy_wszystkie = []
        while True:
            
            print(pg)
            eventy = self.pobierz_dane(pg,kalendarz,coin,kategoria,sortowanie,filtr,start_d,finish_d)
            pg = pg + 1
            print(type(eventy),eventy) 
            
            if type(eventy) == dict:
                print('eventy[message]',eventy['message'])
                break    

            eventy_wszystkie.append(eventy)

        source1 = ''
        for eventy in eventy_wszystkie:

            
            for e in eventy:
                #print(eventy)
                #print(e)
                
                try:
                    coins_name = e['coins'][0]['name']
                    coins_symbol = e['coins'][0]['symbol']
                    start_date = e['date_event']
                    start_date = start_date[0:10]
                    title = e['title']
                    description = e['description']
                    event_source = e['source']
                    event_proof = e['proof']
                    is_hot = e['is_hot']

                    if is_hot == True:
                        is_hot = 'Hot'
                    elif is_hot == False:
                        is_hot = 'Nie hot'
                    
                    vote_count = str(e['vote_count'])
                    positive_vote_count = str(e['positive_vote_count'])
                    percentage = str(e['percentage'])
                    twitter_account = str(e['twitter_account'])

                    image = Path(u''+application_path+ '/cryptoicons128/'+coins_symbol.lower()+'.png')
                    if image.is_file():
                        image = u''+application_path+ '/cryptoicons128/'+coins_symbol.lower()+'.png'
                    else:
                        image = u''+application_path+ '/cryptoicons128/icci_kolo_160.png'

                    

                    #source = '<hr /><p>&nbsp;</p><table style="height: 169px; margin-left: auto; margin-right: auto; width: 603px;"><tbody><tr><td style="width: 143px; text-align: center;"><img src="'+ image +'" alt="" width="128" height="128" /></td><td style="width: 446px;"><h2 style="text-align: center;"><span style="color: #0000ff;"><strong>' + coins_name + '</strong></span>&nbsp;<span style="color: #0000ff;">' + coins_symbol + '</span></h2><h1 style="text-align: center;"><span style="color: #00ff00;"><strong>' + description + '</strong></span></h1><h2 style="text-align: center;"><span style="color: #ffcc00;">' + start_date + '</span></h2></td></tr></tbody></table>'
                    source = '<hr /><p>&nbsp;</p><table style="height: 169px; margin-left: auto; margin-right: auto; width: 603px;"><tbody><tr><td style="width: 143px; text-align: center;"><img src="'+ image +'" alt="" width="128" height="128" /></td><td style="width: 446px;"><h2 style="text-align: center;"><span style="color: #0000ff;"><strong>' + coins_name + '</strong></span>&nbsp;<span style="color: #0000ff;">' + coins_symbol + '</span></h2><h1 style="text-align: center;"><span style="color: #00ff00;"><strong>' + description + '</strong></span></h1><h2 style="text-align: center;"><span style="color: #ffcc00;">' + start_date + '</span></h2></td><td style="width: 446px;"><blockquote><p style="text-align: center;"><strong>vote_count:' + vote_count +'</strong></p><p style="text-align: center;"><span style="text-align: center;">positive_vote_count:' + positive_vote_count + '</span></p><p style="text-align: center;"><span style="text-align: center;">percentage:'+percentage+'</span></p><p style="text-align: center;"><span style="text-align: center;">twitter' +twitter_account + '</span></p><p style="text-align: center;"><span style="text-align: center;">event_source +&nbsp;</span><span style="text-align: center;">'+event_source+'</span><span style="text-align: center;"></span></p><p style="text-align: center;"><span style="text-align: center;">event_proof&nbsp;</span><span style="text-align: center;"></span></p></blockquote><div>&nbsp;</div></td></tr></tbody></table>'

                    source1 += source
                except:
                    pass

        self.wyswietlanie( source1)

    def wyswietlanie(self, source1):
        self.m_htmlWin1.SetPage(source1, "")

    def on_close ( self, event ):    
        self.Destroy()


class Coindar():
    
    def get_data(self,sorter_start_date,sorter_finish_date):
        coindar_events_up_to_date = []
        coindar_events_00 = []
        r = requests.get(url='https://coindar.org/api/v1/lastEvents')
        coindar_events = r.json()
        now = datetime.datetime.now()
        

        for event in coindar_events:
            #time.sleep(0.5)
            coindar_caption = event['caption']
            coindar_proof = event['proof']
            coindar_public_date = event['public_date']
            coindar_start_date = event['start_date']
            coindar_end_date = event['end_date']
            coindar_coin_name = event['coin_name']
            coindar_coin_symbol = event['coin_symbol']
            
            #print(coindar_start_date)
            start = coindar_start_date
            podzielone = start.split('-')
            #print(podzielone)

            #dodanie dnia jezeli nie istnieje
            if len(podzielone) == 2:
                podzielone.append('00')

            rok = podzielone[0]
            miesiac = podzielone[1]
            dzien = podzielone[2]
            dzien = dzien[0:2]

            if len(miesiac) == 1:
                miesiac = '0'+miesiac

            
            sorter = int(rok+miesiac+dzien)
            #print('sorter',sorter))

            '''
            miesiac = int(miesiac)
            rok = int(rok)
            
            if rok >= now.year and miesiac >= now.month:
                if int(str(sorter)[-2:]) >= now.day or str(sorter)[-2:]=='00':

            '''

            sorter_last_2 = str(sorter)
            sorter_last_2 = sorter_last_2[6:8]
            sorter_pierwszy_miesiac = str(sorter_start_date[0:6]) + '00'
            #print('sorter_pierwszy_miesiac',sorter_pierwszy_miesiac)
            #sorter_start_date = 
            # dodac event dla sorter dla pierwszego miesiaca z 00
            if sorter >= int(sorter_start_date) and sorter <= int(sorter_finish_date) or sorter == int(sorter_pierwszy_miesiac):
            
                event = {
                    'wydarzenie':coindar_caption,
                    'start':coindar_start_date,
                    'koniec':coindar_end_date,
                    'coin':coindar_coin_name,
                    'coin_symbol':coindar_coin_symbol,
                    'sorter':sorter              
                    }
                
                
                coindar_events_up_to_date.append(event)

            #data startu i data konca - sorter 
            #porownac czy sa w zakresie dat

             

            sorter_ost_2 = str(sorter)[6:8]
            sort_miesiac = str(sorter_start_date)[0:6]+'00'
            #print('sort_miesiac',sort_miesiac)
            if sorter_last_2 == '00':
                #print('sorter_last_2',sorter_last_2)
                #print('sorter_start_date',sorter_start_date,'sorter_finish_date',sorter_finish_date)
                if sorter >= int(sort_miesiac) and sorter <= int(sorter_finish_date):
                    #print(sorter)
                    #print('dodalem')
                    event = {
                        'wydarzenie':coindar_caption,
                        'start':coindar_start_date,
                        'koniec':coindar_end_date,
                        'coin':coindar_coin_name,
                        'coin_symbol':coindar_coin_symbol,
                        'sorter':sorter              
                        }
                    
                    coindar_events_00.append(event)

        coindar_events_00.sort(key=operator.itemgetter('sorter'))
        coindar_events_up_to_date.sort(key=operator.itemgetter('sorter'))

        #print(coindar_events_00)
        print('koniec ')
        #print(coindar_events_up_to_date)
        return coindar_events_up_to_date, coindar_events_00
        

    def wyswietlanie(self,sorter_start_date,sorter_finish_date,rodzaj_eventow):
        
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
        coindar_events_up_to_date, coindar_events_00 = self.get_data(sorter_start_date,sorter_finish_date)
        
        source1 = ''

        #sorter_start_date_zero = str(sorter_start_date[0:6]) + '00'

        print('rodzaj_eventow',rodzaj_eventow)

        if rodzaj_eventow == 0:
            for event in coindar_events_up_to_date:
                sorter = int(event['sorter'])
                
                if str(sorter)[6:8] != '00':

                    wydarzenie = event['wydarzenie']
                    start = event['start']
                    koniec = event['koniec']
                    coin = event['coin']
                    coin_symbol = event['coin_symbol']

                    if koniec == '':
                        pass
                    else:
                        koniec = 'koniec: ' + str(koniec)

                    image = Path(u''+application_path+ '/cryptoicons128/'+coin_symbol.lower()+'.png')
                    if image.is_file():
                        image = u''+application_path+ '/cryptoicons128/'+coin_symbol.lower()+'.png'
                    else:
                        image = u''+application_path+ '/cryptoicons128/icci_kolo_160.png'

                    source = '<hr /><p>&nbsp;</p><table style="height: 169px; margin-left: auto; margin-right: auto; width: 603px;"><tbody><tr><td style="width: 143px; text-align: center;"><img src="'+ image +'" alt="" width="128" height="128" /></td><td style="width: 446px;"><h2 style="text-align: center;"><span style="color: #0000ff;"><strong>' + coin + '</strong></span>&nbsp;<span style="color: #0000ff;">' + coin_symbol + '</span></h2><h1 style="text-align: center;"><span style="color: #00ff00;"><strong>' + wydarzenie + '</strong></span></h1><h2 style="text-align: center;"><span style="color: #ffcc00;">' + start + koniec + '</span></h2></td></tr></tbody></table>'
                    source1 += source
        
        if rodzaj_eventow == 1:
            for event in coindar_events_00:
                sorter = int(event['sorter'])

                wydarzenie = event['wydarzenie']
                start = event['start']
                koniec = event['koniec']
                coin = event['coin']
                coin_symbol = event['coin_symbol']

                if koniec == '':
                    pass
                else:
                    koniec = 'koniec: ' + str(koniec)

                image = Path(u''+application_path+ '/cryptoicons128/'+coin_symbol.lower()+'.png')
                if image.is_file():
                    image = u''+application_path+ '/cryptoicons128/'+coin_symbol.lower()+'.png'
                else:
                    image = u''+application_path+ '/cryptoicons128/icci_kolo_160.png'

                source = '<hr /><p>&nbsp;</p><table style="height: 169px; margin-left: auto; margin-right: auto; width: 603px;"><tbody><tr><td style="width: 143px; text-align: center;"><img src="'+ image +'" alt="" width="128" height="128" /></td><td style="width: 446px;"><h2 style="text-align: center;"><span style="color: #0000ff;"><strong>' + coin + '</strong></span>&nbsp;<span style="color: #0000ff;">' + coin_symbol + '</span></h2><h1 style="text-align: center;"><span style="color: #00ff00;"><strong>' + wydarzenie + '</strong></span></h1><h2 style="text-align: center;"><span style="color: #ffcc00;">' + start + koniec + '</span></h2></td></tr></tbody></table>'
                source1 += source

        return source1
            
if __name__=='__main__':
    app = wx.App(False)
    frame = Kalendarz(None)
    frame.Show(True)
    app.MainLoop()


