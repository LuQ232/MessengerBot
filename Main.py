from fbchat import *
from fbchat.models import *
import fbchat
import requests
from bs4 import BeautifulSoup
import random

commands= ["!mem","!cat","!kod","Hejka","@everyone","!translate","!weather"]


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

    def list_to_tag_everyone(self,id):
        list_of_participants = []
        for participant in self.fetchGroupInfo(id).get(f'{id}').participants:
            list_of_participants.append(Mention(participant,0,9))
        return list_of_participants

    def polish_english_translator(word):
        translated_words = []
        url = "https://en.bab.la/dictionary/english-polish/" + word
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        meanings_div = soup.find(class_="sense-group-results")
        meanings_str = meanings_div.__str__()
        list = meanings_str.split('\n')

        for meaning in list:
            if "dictionary/polish-english/" in meaning or "/dictionary/english-polish/" in meaning:
                pass
            else:
                list.remove(meaning)

        list.pop()  # Im deleting last element on list (idk why its always there and always bad)?? weird solution but works

        for meaning in list:
            word = meaning.split("'>")[1].split("</a>")[0]
            translated_words.append(word)
        listToStr = '\n'.join(map(str, translated_words))
        return listToStr

    def read_data_base(self,database_name):
        with open(f'{database_name}') as f:
            lines = f.read().splitlines()
        return random.choice(lines)

    def weather_forecast(self,miejscowosc):
        url = "https://www.meteoprog.pl/pl/weather/" + miejscowosc + "/#1"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #########################TODAY########################
        div = soup.find(class_='sliderWeather')
        today_str = div.__str__().split('data-daynumber="0" title="')[1]
        today_description = today_str.split('">')[0]
        today_tmp = today_description.replace("..", " do ", 1)
        today = "Temperatura dziś wyniesie od " + today_tmp + "\n"
        ########################TOMMOROW#######################
        div = soup.find(class_='sliderWeather')
        tommorow_str = div.__str__().split('data-daynumber="1" title="')[1]
        tommorow_description = tommorow_str.split('">')[0]
        tommorow_tmp = tommorow_description.replace("..", " do ", 1)
        tommorow = "Temperatura jutro wyniesie od " + tommorow_tmp + "\n"
        ###################DAY AFTER TOMMOROW##################
        div = soup.find(class_='sliderWeather')
        day_after_tommorow_str = div.__str__().split('data-daynumber="2" title="')[1]
        day_after_tommorow_description = day_after_tommorow_str.split('">')[0]
        day_after_tommorow_tmp = day_after_tommorow_description.replace("..", " do ", 1)
        day_after_tommorow = "Temperatura pojutrze wyniesie od " + day_after_tommorow_tmp + "\n"

        answear = today + tommorow + day_after_tommorow
        return answear

    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None,
                  thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):

        if author_id == self.uid:
            pass
        elif "hejka" in message.lower():
            self.sendMessage("Witam!",thread_id,thread_type)
        elif "spierdalaj" in message.lower():
            self.sendMessage("Sam spierdalaj!!", thread_id, thread_type)
        elif "!mem" in message.lower():
            self.sendRemoteFiles(self.random_meme_url(), None, thread_id, thread_type)
        elif "!cat" in message.lower():
            self.sendRemoteFiles(self.random_cat_url(), None, thread_id, thread_type)
        elif "!kod" in message.lower():
            self.sendMessage("https://github.com/LuQ232/MessengerBot", thread_id, thread_type)
        elif  "@everyone" in message.lower():
             self.send(Message("@everyone", self.list_to_tag_everyone(thread_id)), thread_id, thread_type)
        elif "!translate" in message.lower():
            word = message.lower().split("!translate ")[1]
            self.sendMessage(self.polish_english_translator(word),thread_id,thread_type)
        elif "!weather" in message.lower():
            city = message.lower().split("!weather ")[1]
            self.sendMessage(self.weather_forecast(city),thread_id,thread_type)
        elif "seks" in message.lower():
            self.send(self.read_data_base("urls_1.txt"),thread_id,thread_type)



Moj_Bot=Bot(zwroc_login(),zwroc_haslo())
Moj_Bot.listen()



