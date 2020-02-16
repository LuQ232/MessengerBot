from fbchat import Client
import time
from fbchat.models import *

def czytaj_plik():
    f = open("TEST.txt", "r")
    if f.mode== 'r':
        tekst=f.read()
        lista = list(tekst.split(","))
        return lista
    else:
        print("NIEPOPRAWNIE ODCZYTANO LOGIN I HASLO!!!!!")
        return 0

def zwroc_login():
    lista=czytaj_plik()
    return lista[0]

def zwroc_haslo():
    lista=czytaj_plik()
    return lista[1]


class Bot:
    def zaloguj(self,login,haslo):
        global client
        client = Client(login, haslo)

    def wyloguj(self):
        client.logout()

    def wyslij_wiadomosc(self,wiadomosc,odbiorca,typ_konwersacji):
            client.send(Message(text=wiadomosc), thread_id=odbiorca, thread_type=typ_konwersacji)

    def pobierz_wszystkie_konwersacje(self):
        konwersacje = client.fetchAllUsers()
        return konwersacje

    def pobierz_najczestsze_konwersacje(self):
        konwersacje = client.fetchThreadList()
        return konwersacje

class Uzytkownik:
    pass




Moj_Bot=Bot()
Moj_Bot.zaloguj(zwroc_login(),zwroc_haslo())



try:
    while True:

        for osoba in Moj_Bot.pobierz_najczestsze_konwersacje():
            Wiadomosci = client.fetchThreadMessages(thread_id=osoba.uid, limit=1)
            for wiadomosc in Wiadomosci:
                if wiadomosc.text == "jestem super":
                    Moj_Bot.wyslij_wiadomosc("dokladnie tak tak tak tak :)))))", osoba.uid, osoba.type)
                else:
                    pass
        time.sleep(1)
        print("Pracuje")
except KeyboardInterrupt:
    print('interrupted!')

Moj_Bot.wyloguj()

