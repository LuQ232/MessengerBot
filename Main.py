from fbchat import *
from fbchat.models import *
import requests
from bs4 import BeautifulSoup


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

    def random_demotywator_url(self):
        page = requests.get("https://demotywatory.pl/losuj")
        soup = BeautifulSoup(page.content, 'html.parser')
        demot_div = soup.find(class_='picwrapper')
        demot_div_to_str = demot_div.__str__()
        new_str = demot_div_to_str.split('src="')[1]
        url= new_str.split('" ')[0]
        return url

    def random_jeja_url(self):
        page = requests.get("https://memy.jeja.pl/losowe")
        soup = BeautifulSoup(page.content, 'html.parser')
        jeja_div = soup.find(class_='ob-left-images')
        jeja_div_to_str = jeja_div.__str__()
        new_str = jeja_div_to_str.split('src="')[1]
        url= new_str.split('"')[0]
        return url

    def random_mistrzowe_url(self):
        page = requests.get("https://mistrzowie.org/losuj")
        soup = BeautifulSoup(page.content, 'html.parser')
        jeja_div = soup.find(class_='pic_wrapper')
        jeja_div_to_str = jeja_div.__str__()
        new_str = jeja_div_to_str.split('src="')[1]
        url= new_str.split('" ')[0]
        url= "https://mistrzowie.org"+url
        return url
    def random_jajco_url(self):
        page = requests.get("http://jajco.pl/rand")
        soup = BeautifulSoup(page.content, 'html.parser')
        jeja_div = soup.find(class_='imgcut')
        jeja_div_to_str = jeja_div.__str__()
        new_str = jeja_div_to_str.split('src="')[1]
        url= new_str.split('"')[0]
        return url

    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None,
                  thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        if author_id == self.uid:
            pass
        elif message.lower() =="hejka":
            self.sendMessage("Witam!",thread_id,thread_type)
        elif message.lower() =="spierdalaj":
            self.sendMessage("Sam spierdalaj!!", thread_id, thread_type)
        elif message.lower() =="!demotywator":
            self.sendRemoteFiles(self.random_demotywator_url(),None,thread_id,thread_type)
        elif message.lower() == "!jeja":
            self.sendRemoteFiles(self.random_jeja_url(), None, thread_id, thread_type)
        elif message.lower() == "!mistrzowie":
            self.sendRemoteFiles(self.random_mistrzowe_url(), None, thread_id, thread_type)
        elif message.lower() == "!jajco":
            self.sendRemoteFiles(self.random_jajco_url(), None, thread_id, thread_type)

Moj_Bot=Bot(zwroc_login(),zwroc_haslo())
Moj_Bot.listen()



