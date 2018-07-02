#https://stackoverflow.com/questions/41218148/wxpython-fetch-remote-image-and-threading
# czy sprawdza czy linkzostal pobrany project_link_list a jak nie to pobiera pojedynczy?
# zrobic nowa liste bez nieaktualnych ico (przy ladowaniu zbioru) 

import wx
import wx.lib.scrolledpanel
import json
import requests as r
import wx
import wx.html2
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
#import numpy as np
import pickle
from urllib.request import Request, urlopen
import io
import os.path
from pathlib import Path
import pathlib
import CC_get_app_patch
application_path = CC_get_app_patch.pobierz_app_patch()

do_save = False

try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO

import CC_get_app_patch
application_path = CC_get_app_patch.pobierz_app_patch()

def get_IWL_data(url):
    try:
        events = (r.post(url))
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result

def get_IWL_live_ico():
    return get_IWL_data("https://api.icowatchlist.com/public/v1/live")['ico']['live']

def get_IWL_upcoming_ico():
    return get_IWL_data("https://api.icowatchlist.com/public/v1/upcoming")['ico']['upcoming']

def get_IWL_finished_ico():
    return get_IWL_data("https://api.icowatchlist.com/public/v1/finished")['ico']['finished']

def scrap_url(icowatchlist_url):
    print (icowatchlist_url)
    req = Request(icowatchlist_url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    try:
        project_website = str(soup.find('a', attrs={'class': 'btn btn-default btn-lg btn-block btnSuccess oblink'})).split()[9].split('=')[1]
    except:
        project_website = 'brak'

    try:
        project_whitepapper = str(soup.find('a', attrs={'class': 'btn btn-default btn-lg btn-block btnGrey oblink'})).split()[9].split('=')[1]
    except:
        project_whitepapper = 'brak'

    try:
        project_video = (str(soup.find('div', attrs={'class': 'embed-container'}))).split('src=')[1].split('<')[0].replace('>','')
        project_video = project_video +'?autoplay=1&amp;modestbranding=1&amp;rel=0&amp;'
    except:
        project_video = 'brak'

    return project_website , project_whitepapper, project_video

def save_obj(obj, name ):
    with open(application_path + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    print(application_path + '/' + name + '.pkl')
    with open(application_path + '/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def make_live_ico_html():
    source = ''
    live_ico = get_IWL_live_ico()
    do_save = False

    try:
        project_link_list = load_obj('project_link_list' )
        print('1. wczytałem project_link_list',project_link_list)
    except:
        print('błąd wczytania project_link_list',project_link_list)
        project_link_list = []

    for event in live_ico:
        name = event['name']
        image = event['image']
        description = event['description']
        website_link = event['website_link']
        icowatchlist_url = event['icowatchlist_url']
        start_time = event['start_time']
        end_time = event['end_time']
        timezone = event['timezone']
        #coin_symbol = event['coin_symbol']
        #price_usd = event['price_usd']
        #all_time_roi =  event['all_time_roi']

        project_link = [d[name] for d in project_link_list if name in d]
        print(project_link)

        if project_link != []:
            project_link = project_link[0]
            print('jest! ', project_link)
            print(type(project_link))
        else:
            project_link = scrap_url(icowatchlist_url)
            project_link_list.append({name:project_link})
            print('dodalem : ', {name:project_link})   
            do_save = True   

    if do_save == True:
        save_obj(project_link_list, 'project_link_list' )
        print('project_link_list saved')

    return source

def load_image(url):
    print(url)

    Im = url.split('https://icowatchlist.com/logos/')[1]
    print('Link do  logo', Im)
    Image = u''+application_path+"/IcoLogo/"+ Im

    #make dir for icons
    app_folder = application_path + '/IcoLogo/'
    print('tworzę folder:', app_folder)
    pathlib.Path(app_folder).mkdir(parents=True, exist_ok=True) 

    my_file = Path(Image)
    if my_file.is_file():
        print('plik istnieje:',Image)
        pass
    else:
        img_data = r.get(url).content
        with open(Image, 'wb') as handler:
            handler.write(img_data)

    Image = application_path+'/IcoLogo/'+Im
    print(Image)
  
    return Image

class Wyswietlanie_ICO ( wx.Panel ):
	
    def __init__( self, parent ):
        #wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,120 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL,  )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        bSizer23 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow2.SetScrollRate( 5, 5 )
        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        source = ''
        live_ico = get_IWL_live_ico()
        do_save = False
        print(live_ico)

        try:    
            project_link_list = load_obj('project_link_list' )
            print('OK! project_link_list loaded',project_link_list)
        except:
            print('ERR! project_link_list not loaded project_link_list')
            project_link_list = []

        for event in live_ico:
            name = event['name']
            image = event['image']
            description = event['description']
            website_link = event['website_link']
            icowatchlist_url = event['icowatchlist_url']
            start_time = event['start_time']
            end_time = event['end_time']
            timezone = event['timezone']

            self.m_panel1 = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
            self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

            bSizer25 = wx.BoxSizer( wx.VERTICAL )

            self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), wx.TAB_TRAVERSAL )
            bSizer26 = wx.BoxSizer( wx.VERTICAL )

            #logo
            img = load_image(image) #error
            #wx.StaticBitmap(Panel, -1, Image, (10,10))
            self.logo = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( img, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )

            #self.logo = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, img, wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer26.Add( self.logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            #empty line
            self.przerwa1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.przerwa1.Wrap( -1 )
            bSizer26.Add( self.przerwa1, 0, wx.ALL|wx.EXPAND, 5 )

            # Title
            self.Title1 = wx.StaticText( self.m_panel2, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.Title1.Wrap( -1 )

            self.Title1.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
            self.Title1.SetForegroundColour( wx.Colour( 34, 255, 11 ) )
            bSizer26.Add( self.Title1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            #description
            self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, description, wx.DefaultPosition, wx.DefaultSize, 0 )

            self.m_staticText1.SetForegroundColour((0,0,255)) # set text back color
            
            self.m_staticText1.Wrap( -1 )
            self.m_staticText1.Wrap((500))
            
            bSizer26.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

            #empty line
            self.przerwa1 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.przerwa1.Wrap( -1 )
            bSizer26.Add( self.przerwa1, 0, wx.ALL|wx.EXPAND, 5 )
            
            #buttons

            bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

            #button strona projektu
            bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
            self.strona_projektu_button = wx.Button( self.m_panel2, wx.ID_ANY, u"strona projektu", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer12.Add( self.strona_projektu_button, 0, wx.ALL, 5 )
            
            self.strona_projektu_button.Bind(wx.EVT_BUTTON, lambda evt, name=icowatchlist_url: self.wyswietl_web(evt, name, 'project_website'))

            #button whitepapper
            self.whitepapper_button = wx.Button( self.m_panel2, wx.ID_ANY, u"whitepapper", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer12.Add( self.whitepapper_button, 0, wx.ALL, 5 )

            self.whitepapper_button.Bind(wx.EVT_BUTTON, lambda evt, name=icowatchlist_url: self.wyswietl_web(evt, name, 'project_whitepapper'))

            #self.strona_projektu_button.Bind(wx.EVT_BUTTON, lambda evt, name=icowatchlist_url: self.wyswietl_web(evt, name))

            ######

            self.video_button = wx.Button( self.m_panel2, wx.ID_ANY, u"video", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer12.Add( self.video_button, 0, wx.ALL, 5 )

            self.video_button.Bind(wx.EVT_BUTTON, lambda evt, name=icowatchlist_url: self.wyswietl_web(evt, name, 'project_video'))

            ###

            self.m_button8 = wx.Button( self.m_panel2, wx.ID_ANY, u"twitter", wx.DefaultPosition, wx.DefaultSize, 0 )

            bSizer12.Add( self.m_button8, 0, wx.ALL, 5 )

            bSizer26.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

            #empty line
            self.przerwa1 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.przerwa1.Wrap( -1 )
            bSizer26.Add( self.przerwa1, 0, wx.ALL|wx.EXPAND, 5 )

            self.m_panel2.SetSizer( bSizer26 )
            self.m_panel2.Layout()
            bSizer26.Fit( self.m_panel2 )
            bSizer25.Add( self.m_panel2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
            self.m_panel1.SetSizer( bSizer25 )
            self.m_panel1.Layout()
            bSizer25.Fit( self.m_panel1 )
            bSizer24.Add( self.m_panel1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_scrolledWindow2.SetSizer( bSizer24 )
            self.m_scrolledWindow2.Layout()
            bSizer24.Fit( self.m_scrolledWindow2 )
            bSizer24.Layout()
        
        bSizer23.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
        self.SetSizer( bSizer23 )
        self.Layout()
        self.Centre( wx.BOTH )


    def wyswietl_web( self, event, icowatchlist_url, project_web_type ):
        butt = event.GetEventObject()
        
        print('wyswietl_web')
        print(icowatchlist_url)
        
        print('butt',butt)
        print(butt.GetId())
        print(butt.GetName())
        print(butt.GetLabel())


        #tuple project_website, project_whitepaper
        url_project = scrap_url(icowatchlist_url)

        if project_web_type == 'project_website':
            url_p = url_project[0]
        elif project_web_type == 'project_whitepapper':
            url_p = url_project[1]
        elif project_web_type == 'project_video':
            url_p = url_project[2]

        if url_p != 'brak':
            dialog = MyBrowser(None) 
            if project_web_type == 'project_website' or project_web_type == 'project_whitepapper':
                dialog.Maximize(True)
            dialog.browser.LoadURL(str(url_p.replace('"',''))) 
            dialog.Show() 
        else: 
            butt.SetLabel('Brak '+str(project_web_type.split('_')[1])) 
            print('url_p',url_p)


class MyBrowser(wx.Frame): 
    def __init__(self, *args, **kwds): 
        wx.Frame.__init__(self, *args, **kwds) 
        self.Bind ( wx.EVT_CLOSE, self.on_close )
        sizer = wx.BoxSizer(wx.VERTICAL) 
        self.browser = wx.html2.WebView.New(self) 
        sizer.Add(self.browser, 1, wx.EXPAND, 10) 
        self.SetSizer(sizer) 
        self.SetSize((1000, 700)) 

    def on_close ( self, event ):    
        self.Destroy()

if __name__=='__main__':
    app = wx.App(0)
    frame = Wyswietlanie_ICO(None).Show()
    app.MainLoop()