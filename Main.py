from fbchat import *
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

    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None,
                  thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        print(message_object)
        print(message_object.text)



Moj_Bot=Bot(zwroc_login(),zwroc_haslo())
Moj_Bot.listen()


