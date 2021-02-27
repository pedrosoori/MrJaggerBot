import requests
import time
from twitchAPI.twitch import Twitch
import twitter
from datetime import datetime
import os
from os import environ

api2 = twitter.Api(consumer_key=environ['consumer_key'],
                  consumer_secret=environ['consumer_secret'],
                  access_token_key=environ['access_token_key'],
                  access_token_secret=environ['access_token_secret'])

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
    checkUser('pedrosoori')
    if checkUser('pedrosoori')==True and x==0:
        api2.PostUpdate(status='@MisterJagger_ ESTA EN DIRECTO EN TWITCH https://www.twitch.tv/jaggerprincesa')
        arcinic=open(inicio,"w")
        hora=str(time.time())
        arcinic.write(str(hora))
        arcinic.close()
        x+=1
        y+=1
    elif checkUser('pedrosoori')==False and y==1:
        final=int(time.time())
        inicio=int(retrieve_inicio(inicio))
        segundos=final-inicio
        horas=int(segundos/3600)
        segundos-=horas*3600
        minutos=int(segundos/60)
        segundos-=minutos*60
        segundos=int(segundos)
        
        api2.PostUpdate(status='@MisterJagger_ ACABA DE CERRAR STREAM. Duracion: %s horas %s minutos %s segundos' % (horas,minutos,segundos))
        print('adios. Duracion del streaming: %s horas %s minutos %s segundos' % (horas,minutos,segundos))
        y=0
        x=0
    time.sleep(10)

         