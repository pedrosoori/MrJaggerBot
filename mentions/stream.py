import requests
import time
from twitchAPI.twitch import Twitch
import twitter
import tweepy
from datetime import datetime
import os
from os import environ

print('hola')

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

api2 = twitter.Api(consumer_key=environ['consumer_key'],
                  consumer_secret=environ['consumer_secret'],
                  access_token_key=environ['access_token_key'],
                  access_token_secret=environ['access_token_secret'])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


client_id = environ['client_id']
client_secret = environ['client_secret']

twitch = Twitch(client_id, client_secret)
twitch.authenticate_app([])

TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/kraken/streams/{}"

API_HEADERS = {
    'Client-ID' : client_id,
    'Accept' : 'application/vnd.twitchtv.v5+json',
}

def checkUser(user): #returns true if online, false if not
    userid = twitch.get_users(logins=[user])['data'][0]['id']
    url = TWITCH_STREAM_API_ENDPOINT_V5.format(userid)
    try:
        req = requests.Session().get(url, headers=API_HEADERS)
        jsondata = req.json()
        if 'stream' in jsondata:
            if jsondata['stream'] is not None: 
                return True
            else:
                return False
    except Exception as e:
        print("Error checking user: ", e)
        return False

inicio='inicio.txt'
def retrieve_inicio(inicio):
    f_read = open(inicio, 'r')
    inicio = int(float(f_read.read().strip()))
    f_read.close()
    return inicio

x=0
y=0
while True:
    checkUser('JaggerPrincesa')
    if checkUser('JaggerPrincesa')==True and x==0:
        api.update_status('@MisterJagger_ ESTA EN DIRECTO EN TWITCH https://www.twitch.tv/jaggerprincesa')
        print('EMPIEZA EMPIEZA EMPIEZA')
        arcinic=open(inicio,"w")
        hora=str(time.time())
        arcinic.write(str(hora))
        arcinic.close()
        x+=1
        y+=1
    elif checkUser('JaggerPrincesa')==False and y==1:
        final=int(time.time())
        inicio=int(retrieve_inicio(inicio))
        segundos=final-inicio
        horas=int(segundos/3600)
        segundos-=horas*3600
        minutos=int(segundos/60)
        segundos-=minutos*60
        segundos=int(segundos)

        api.update_status('@MisterJagger_ ACABA DE CERRAR STREAM. Duracion: %s horas %s minutos %s segundos' % (horas,minutos,segundos))
        print('ACABA ACABA ACABA')
        y=0
        x=0
    time.sleep(10)
