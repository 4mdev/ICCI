print('importuje apps.block_exporer.icci_blockcypher_API_GUI as bc_gui')
import apps.block_exporer.icci_blockcypher_API_GUI as bc_gui
print('importuje wx')
import wx
print('importuje apps.block_exporer.blockcypher as blockcypher')
import apps.block_exporer.blockcypher as blockcypher
print('importuje from blockcypher import constants')
from blockcypher import constants

class Dashboard(bc_gui.MyFrame2):

    def __init__(self,parent):
        #initialize parent class
        bc_gui.MyFrame2.__init__(self,parent)
        self.lista_krypto.Append(constants.COIN_SYMBOL_LIST)

    def bc_portfel_getinfo_funkcja(self,event):
        try:
            wallet_adress = self.bc_portfel_nr_input.GetValue() 
            #wallet_adress = '1BTCorgHwCg6u2YSAWKgS17qUad6kHmtQW'
            #ltc LbtF3xpYFvocPqXjuYok8cahJ3GWeDA5w1
            #dodge DPHPoGQVKwgDsSG7r9329V45fLi7fpBWjA
            #dash XitN7K1KLTc6kd7MBZMSkzFH8XwejukXWz

            coin_symbol =  self.lista_krypto.GetStringSelection() 
            bc_wallet_details = blockcypher.get_address_details(wallet_adress,coin_symbol=coin_symbol)
            print('bc_wallet_details',bc_wallet_details)
            
            wallet_address = 'adres portfela: ' + str(bc_wallet_details['address'])
            print(wallet_address)
            if coin_symbol == 'btc':
                wallet_total_received = 'Otrzymane: ' + str(blockcypher.from_satoshis(bc_wallet_details['total_received'], coin_symbol)) + ' ' + coin_symbol.upper()
                wallet_total_sent = 'Wysłane: ' + str(blockcypher.from_satoshis(bc_wallet_details['total_sent'], coin_symbol)) + ' ' + coin_symbol.upper()
                wallet_balance = 'Saldo: ' + str(blockcypher.from_satoshis(bc_wallet_details['balance'], coin_symbol)) + ' ' + coin_symbol.upper()
                wallet_unconfirmed_balance = 'Saldo niepotwierdzone: ' + str(blockcypher.from_satoshis(bc_wallet_details['unconfirmed_balance'], coin_symbol)) + ' ' + coin_symbol.upper()
                wallet_final_balance = 'Saldo ostateczne: ' + str(blockcypher.from_satoshis(bc_wallet_details['final_balance'], coin_symbol)) + ' ' + coin_symbol.upper()

            else:
                wallet_total_received = 'Otrzymane: ' + str(bc_wallet_details['total_received']) + ' ' + coin_symbol.upper()
                wallet_total_sent = 'Wysłane: ' + str(bc_wallet_details['total_sent']) + ' ' + coin_symbol.upper()     
                wallet_balance = 'Saldo: ' + str(bc_wallet_details['balance']/100000000) + ' ' + coin_symbol.upper()
                wallet_unconfirmed_balance = 'Saldo niepotwierdzone: ' + str(bc_wallet_details['unconfirmed_balance']/100000000) + ' ' + coin_symbol.upper()
                wallet_final_balance = 'Saldo ostateczne: ' + str(bc_wallet_details['final_balance']/100000000) + ' ' + coin_symbol.upper()
    
            wallet_nr_transactions = 'Ilość transakcji: ' + str(bc_wallet_details['n_tx'])
            wallet_unconfirmed_nr_transactions = 'Ilość niepotwierdzonych transakcji: : '+str(bc_wallet_details['unconfirmed_n_tx'])
            wallet_final_nr_transactions = 'Ostateczna ilość transakcji: : '+str(bc_wallet_details['final_n_tx'])

            wx.MessageBox((str(wallet_address) +'\n' +'\n' +'\n'  + str(wallet_balance)+'\n'  + str(wallet_unconfirmed_balance)+'\n' + str(wallet_final_balance)+'\n'  + str(wallet_nr_transactions)+'\n'  + str(wallet_unconfirmed_nr_transactions)+'\n'  + str(wallet_final_nr_transactions)), 'Informacje o portfelu' ,wx.OK | wx.ICON_INFORMATION)  
        except:
            wx.MessageBox('Błąd - sprawdź adres i typ kryptowaluty. \nJeżeli błąd się powtarza spróbuj później lub skontaktuj się z IccI - support.', 'Informacje o bloku' ,wx.OK | wx.ICON_INFORMATION)

    def bc_transakcja_getinfo_funkcja(self,event):
        try:
            transakcja_hash = self.bc_transakcja_nr_input.GetValue()
            #transakcja_hashbtc = '400f3daead6ce20f3b6e1639e041dff9f563ec8b87cfb33a95efd37b8883c6e4'
            #ltc 03ae8088de52d8073be112629dce77c588e34320ccc923630d60fc453b87b091
            coin_symbol =  self.lista_krypto.GetStringSelection()

            #transakcja
            bc_transaction_details = blockcypher.get_transaction_details(transakcja_hash,coin_symbol=coin_symbol)  # BTC unless specified 
            print('bc_transaction_details',bc_transaction_details)

            bc_trans_confirmed = 'Potwierdzone: ' + str(bc_transaction_details['confirmed'])
            bc_trans_received = 'Złożone: ' + str(bc_transaction_details['received'])

            #transakcja
            bc_number_of_confirmations = 'Ilość potwierdzeń: ' + str(blockcypher.get_num_confirmations(transakcja_hash,coin_symbol=coin_symbol))
            #print('\n\nbc_number_of_confirmations',bc_number_of_confirmations)

            if coin_symbol == 'btc':
                #transakcja
                bc_satoshis_transacted = blockcypher.get_satoshis_transacted(transakcja_hash,coin_symbol=coin_symbol)
                #print('\n\nbc_satoshis_transacted',bc_satoshis_transacted)

                transaction_from_satoshi = 'Kwota: ' + str(blockcypher.from_satoshis(bc_satoshis_transacted,coin_symbol)) + ' ' +coin_symbol.upper()
                #print('transaction_from_satoshi',transaction_from_satoshi)

            else:
                            #transakcja

                transaction_from_satoshi = 'Kwota: ' + str(bc_transaction_details['total']/100000000) + ' ' +coin_symbol.upper()
                #print('transaction_from_satoshi',transaction_from_satoshi)



            hash_transakcji = ('Hash_transakcji: '+str(transakcja_hash))

            if coin_symbol == 'btc-testnet':
                block_hash = ''
                block_height = ''
                block_index = ''


            else:
                block_hash = 'Hash bloku: ' + str(bc_transaction_details['block_hash'])
                block_height = 'Wysokość: ' + str(bc_transaction_details['block_height'])
                block_index = 'Indeks bloku: ' + str(bc_transaction_details['block_index'])
                
            adresy = bc_transaction_details['addresses']
            try:
                adres_zleceniodawcy = str(adresy[0])
                adres_odbiorcy = str(adresy[1])
            except:
                adres_zleceniodawcy = ''
                adres_odbiorcy = ''

            if coin_symbol == 'btc':
                transaction_fees = 'Opłaty: ' + str(blockcypher.from_satoshis(bc_transaction_details['fees'],coin_symbol)) + ' ' + coin_symbol.upper()
            else:
                transaction_fees = 'Opłaty: ' + str(bc_transaction_details['fees']/100000000) + ' ' + coin_symbol.upper()


            wx.MessageBox((str(hash_transakcji) +'\n\n'+ str(bc_number_of_confirmations) +'\n\n' + str(transaction_from_satoshi) + '\n' + transaction_fees +'\n\n' + bc_trans_confirmed+ '\n' + bc_trans_received +'\n\n'+ str(block_hash) +'\n\n' + str(block_height)+'\n' + str(block_index) +'\n\n' + 'Adres zleceniodawcy:'+ '\n'+ adres_zleceniodawcy +'\n\n' +'Adres odbiorcy:' + (adres_odbiorcy)+ '\n\n' ), 'Informacje o transakcji' ,wx.OK | wx.ICON_INFORMATION)  

        except:
            wx.MessageBox('Błąd - sprawdź adres i typ kryptowaluty. \nJeżeli błąd się powtarza spróbuj później lub skontaktuj się z IccI - support.', 'Informacje o bloku' ,wx.OK | wx.ICON_INFORMATION)

    def bc_blok_getinfo_funkcja(self,event):
        try:
            blok_hash = self.bc_blok_nr_input.GetValue()
            #blok_hash = '12345'
            coin_symbol =  self.lista_krypto.GetStringSelection()

            bc_block_info = blockcypher.get_block_overview(blok_hash,coin_symbol=coin_symbol)
            print('\n\nbc_block_info',bc_block_info)
            block_hash = str('Blok hash: ' + '\n' + bc_block_info['hash'])
            block_height = str('Wysokość: ' + str(bc_block_info['height']))
            block_chain = str('Łańcuch: ' + str(bc_block_info['chain']))
            block_total = str('Wolumen transakcji: ' + str(bc_block_info['total']/100000000)+ ' ' + coin_symbol.upper())
            block_fees = str('Opłaty transakcyjne: ' + str(bc_block_info['fees']))
            block_time = str('Czas: ' + str(bc_block_info['time']))
            block_nonce = str('Nonce: ' + str(bc_block_info['nonce']))
            block_prev = str('Poprzedni blok: '+ '\n' + str(bc_block_info['prev_block']))
            
            wx.MessageBox((str(block_hash) +'\n\n'+ str(block_height) +'\n' + str(block_chain)+'\n\n'  + str(block_total)+'\n'  + str(block_fees)+'\n\n' + str(block_time)+'\n'+ block_nonce+'\n\n'+ block_prev), 'Informacje o bloku' ,wx.OK | wx.ICON_INFORMATION)  
        except:
            wx.MessageBox('Błąd - sprawdź adres i typ kryptowaluty. \nJeżeli błąd się powtarza spróbuj później lub skontaktuj się z IccI - support.', 'Informacje o bloku' ,wx.OK | wx.ICON_INFORMATION)
            

if __name__=='__main__':
    app = wx.App(False)
    frame = Dashboard(None)
    frame.Show(True)
    app.MainLoop()