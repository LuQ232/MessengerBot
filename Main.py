from fbchat import *
from fbchat.models import *
import fbchat
import requests
from bs4 import BeautifulSoup
import random

commands= ["!mem","!cat","!kod","Hejka"]

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
        jajco_div = soup.find(class_='imgcut')
        jajco_div_to_str = jajco_div.__str__()
        new_str = jajco_div_to_str.split('src="')[1]
        url= new_str.split('"')[0]
        return url

    def random_memy_url(self):
        page = requests.get("https://memy.pl/losuj")
        soup = BeautifulSoup(page.content, 'html.parser')
        jeja_div = soup.find(class_='figure-item')
        jeja_div_to_str = jeja_div.__str__()
        new_str = jeja_div_to_str.split('src="')[1]
        url = new_str.split('"')[0]
        if (".mp4" in url) == True:
            url = "https://memy.pl" + url
        return url

    def random_meme_url(self):
        random_value = random.randint(1,5)
        if random_value == 1:
            return self.random_demotywator_url()
        elif random_value == 2:
            return self.random_jeja_url()
        elif random_value == 3:
            return self.random_mistrzowe_url()
        elif random_value == 4:
            return self.random_jajco_url()
        elif random_value == 5:
            return self.random_memy_url()
        else:
            pass
    def random_cat_url(self):
        page = requests.get("https://random.cat/")
        soup = BeautifulSoup(page.content, 'html.parser')
        jeja_div = soup.find("a")
        jeja_div_to_str = jeja_div.__str__()
        new_str = jeja_div_to_str.split('src="')[1]
        url = new_str.split('"')[0]
        return url
    def tag_everyone(self,id):
        for participant in self.fetchGroupInfo(id).get(f'{id}').participants:
            print(participant)
       # print(self.fetchGroupInfo(id).get(f'{id}').participants)

        #print(type(self.fetchGroupInfo(id).get(f'{id}').participants))

    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None,
                  thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        if author_id == self.uid:
            pass
        elif message.lower() =="hejka":
            self.sendMessage("Witam!",thread_id,thread_type)
        elif message.lower() =="spierdalaj":
            self.sendMessage("Sam spierdalaj!!", thread_id, thread_type)
        elif message.lower() =="!mem":
            self.sendRemoteFiles(self.random_meme_url(), None, thread_id, thread_type)
        elif message.lower() =="!cat":
            self.sendRemoteFiles(self.random_cat_url(), None, thread_id, thread_type)
        elif message.lower() == "!kod":
            self.sendMessage("https://github.com/LuQ232/MessengerBot", thread_id, thread_type)
        elif message.lower() == "@everyone":
            #self.tag_everyone(thread_id)
            pass


Moj_Bot=Bot(zwroc_login(),zwroc_haslo())
Moj_Bot.tag_everyone(2721940484564018)
Moj_Bot.listen()



