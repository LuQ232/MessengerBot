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


class Bot(Client):

    def wyloguj(self):
        self.logout()

    def wyslij_wiadomosc(self,wiadomosc,odbiorca,typ_konwersacji):
            self.send(Message(text=wiadomosc), thread_id=odbiorca, thread_type=typ_konwersacji)

    def pobierz_wszystkie_konwersacje(self):
        konwersacje = self.fetchAllUsers()
        return konwersacje

    def pobierz_najczestsze_konwersacje(self):
        konwersacje = self.fetchThreadList()
        return konwersacje
    def reaguj_na_wiadomosc(self,bodziec,odpowiedz):
        try:
            while True:

                for osoba in self.pobierz_najczestsze_konwersacje():
                    Wiadomosci = self.fetchThreadMessages(thread_id=osoba.uid, limit=1)
                    for wiadomosc in Wiadomosci:
                        if wiadomosc.text == bodziec:
                           self.wyslij_wiadomosc(odpowiedz, osoba.uid, osoba.type)
                        else:
                            pass
                time.sleep(1)
                print("Pracuje")
        except KeyboardInterrupt:
            print('interrupted!')





class Uzytkownik:
    pass


Moj_Bot=Bot(zwroc_login(),zwroc_haslo())


Moj_Bot.reaguj_na_wiadomosc("Witam","Hej")

Moj_Bot.wyloguj()

