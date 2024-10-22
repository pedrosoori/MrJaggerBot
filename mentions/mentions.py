import tweepy
import twitter
import time
import random
from datetime import datetime
import sys
import github
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

api2 = twitter.Api(consumer_key=environ['consumer_key'],
                  consumer_secret=environ['consumer_secret'],
                  access_token_key=environ['access_token_key'],
                  access_token_secret=environ['access_token_secret'])

g=github.Github(environ['token'])

print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen_id.txt'
FILE_NAME2= 'jagger.txt'
FILE_NAME3= 'ooc.txt'
FILE_NAME4 = 'ibai.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        
        if '@mrjaggerbot @this_vid' in mention.full_text.lower() or '@mrjaggerbot @downloadbot2' in mention.full_text.lower() or '@mrjaggerbot @downloaderbot' in mention.full_text.lower():
            print('BOT DE DESCARGA DE VIDEOS', flush=True)
            print('responding back...', flush=True)
            try:
                api.create_favorite(mention.id)
            except tweepy.TweepError as e:
                print('Mensaje ya favorito.')
                
            repo = g.get_user().get_repo("MrJaggerBot")
            file = repo.get_contents("/mentions/last_seen_id.txt")
            repo.update_file(path=file.path, message="Update", content=str(last_seen_id), sha=file.sha)
            
        elif '@mrjaggerbot' in mention.full_text.lower():# and len(mention.full_text.lower())==12 and mention.full_text.lower().find('@mrjaggerbot')
            print('found', flush=True)
            print('responding back...', flush=True)

            try:
                api.create_favorite(mention.id)
                
                status=api.show_friendship(source_screen_name=mention.user.screen_name, target_screen_name='MrJaggerBot')
                status=status[0].following
                if status==True:
                    x=random.randint(1,75)
                    if x==1:
                        api2.PostUpdate('@' + mention.user.screen_name +' SISISISISI', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='sisi2.mp4')
                    if x==2:
                        api2.PostUpdate('@' + mention.user.screen_name +' NONONONO', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='nono.mp4')
                    if x==3:
                        api2.PostUpdate('@' + mention.user.screen_name +' JAJSJS SISISI', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='sisi.mp4')
                    if x==4:
                        api2.PostUpdate('@' + mention.user.screen_name +' QUE TE CALLES', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='calles.mp4')
                    if x==5:
                        api2.PostUpdate('@' + mention.user.screen_name +' CALLATE', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='callate.mp4')
                    if x==6:
                        api2.PostUpdate('@' + mention.user.screen_name +' huevo :)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='huevo.mp4')
                    if x==7:
                        api2.PostUpdate('@' + mention.user.screen_name +' eres asqueros@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='asqueroso.mp4')
                    if x==8:
                        api2.PostUpdate('@' + mention.user.screen_name +' toma un platano ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='platano.mp4')
                    if x==9:
                        api2.PostUpdate('@' + mention.user.screen_name +' A', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='A.mp4')
                    if x==10:
                        api2.PostUpdate('@' + mention.user.screen_name +' ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='beso.mp4')
                    if x==11:
                        api2.PostUpdate('@' + mention.user.screen_name +' no, no es lo mismo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='pizza.mp4')
                    if x==12:
                        api2.PostUpdate('@' + mention.user.screen_name +' eres lindisim@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='chupa.mp4')
                    if x==13:
                        api2.PostUpdate('@' + mention.user.screen_name +' me gusta la menta :)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='menta.mp4')
                    if x==14:
                        api2.PostUpdate('@' + mention.user.screen_name +' guap@s ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='guapo.mp4')
                    if x==15:
                        api2.PostUpdate('@' + mention.user.screen_name +' un saludo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='saludo.mp4')
                    if x==16:
                        api2.PostUpdate('@' + mention.user.screen_name +' te dedico este baile', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='baile.mp4')
                    if x==17:
                        api2.PostUpdate('@' + mention.user.screen_name +' fuera tont@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='grita.mp4')
                    if x==18:
                        api2.PostUpdate('@' + mention.user.screen_name +' AAAAA', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='ira.mp4')
                    if x==19:
                        api2.PostUpdate('@' + mention.user.screen_name +' te estaba preguntando', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='pregunta.mp4')
                    if x==20:
                        api2.PostUpdate('@' + mention.user.screen_name +' ERES UNA PESADILLA', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='pesadilla.mp4')
                    if x==21:
                        api2.PostUpdate('@' + mention.user.screen_name +' eres tu', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='mierda.mp4')
                    if x==22:
                        api2.PostUpdate('@' + mention.user.screen_name +' ven aqui', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='azote.mp4')
                    if x==23:
                        api2.PostUpdate('@' + mention.user.screen_name +' que bueno soy', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='bueno.mp4')
                    if x==24:
                        api2.PostUpdate('@' + mention.user.screen_name +' callate', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='callate.mp4')
                    if x==25:
                        api2.PostUpdate('@' + mention.user.screen_name +' estoy fumadisimo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='fumado.mp4')
                    if x==26:
                        api2.PostUpdate('@' + mention.user.screen_name +' eres tont@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='tonto.mp4')
                    if x==27:
                        api2.PostUpdate('@' + mention.user.screen_name +' v a m o s', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='vamos.mp4')
                    if x==28:
                        api2.PostUpdate('@' + mention.user.screen_name +' ah ah ah', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='ahah.mp4')
                    if x==29:
                        api2.PostUpdate('@' + mention.user.screen_name +' uva', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='uva.mp4')
                    if x==30:
                        api2.PostUpdate('@' + mention.user.screen_name +' no se ve el agua', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='agua.mp4')
                    if x==31:
                        api2.PostUpdate('@' + mention.user.screen_name +' te aplaudo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='clap.mp4')
                    if x==32:
                        api2.PostUpdate('@' + mention.user.screen_name +' adios', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='adios.mp4')
                    if x==33:
                        api2.PostUpdate('@' + mention.user.screen_name +' que asco dais', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='asco.mp4')
                    if x==34:
                        api2.PostUpdate('@' + mention.user.screen_name +' gracias y feliz navidad', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='gracias.mp4')
                    if x==35:
                        api2.PostUpdate('@' + mention.user.screen_name +' no no tengo novia', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='novia.mp4')
                    if x==36:
                        api2.PostUpdate('@' + mention.user.screen_name +' ah', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='a2.mp4')
                    if x==37:
                        api2.PostUpdate('@' + mention.user.screen_name +' soy enorme', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='gigante.mp4')
                    if x==38:
                        api2.PostUpdate('@' + mention.user.screen_name +' amor para todos', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='corazon.mp4')
                    if x==39:
                        api2.PostUpdate('@' + mention.user.screen_name +' DESPIERTA', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='dias.mp4')
                    if x==40:
                        api2.PostUpdate('@' + mention.user.screen_name +' buenas noches princesa ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='noches.mp4')
                    if x==41:
                        api2.PostUpdate('@' + mention.user.screen_name +' hoy es noche de sexo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='noches2.mp4')
                    if x==42:
                        api2.PostUpdate('@' + mention.user.screen_name +' toma', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='baile2.mp4')
                    if x==43:
                        api2.PostUpdate('@' + mention.user.screen_name +' has entendido?', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='entendido.mp4')
                    if x==44:
                        api2.PostUpdate('@' + mention.user.screen_name +' feliz navidad', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='navidad.mp4')
                    if x==45:
                        api2.PostUpdate('@' + mention.user.screen_name +' asi asi', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='asi.mp4')
                    if x==46:
                        api2.PostUpdate('@' + mention.user.screen_name +' mi amor', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='amor.mp4')
                    if x==47:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='cancion.mp4')
                    if x==48:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='agradecido.mp4')
                    if x==49:
                        api2.PostUpdate('@' + mention.user.screen_name +' hola', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='hola.mp4')
                    if x==50:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='gruñir.mp4')
                    if x==51:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='callate2.mp4')
                    if x==52:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='baile3.mp4')
                    if x==53:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='vete.mp4')
                    if x==54:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='que_tal.mp4')
                    if x==55:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='amor2.mp4')
                    if x==56:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='especifica.mp4')
                    if x==57:
                        api2.PostUpdate('@' + mention.user.screen_name +' pringao', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='pringao.mp4')
                    if x==58:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='aaaa.mp4')
                    if x==59:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='especifica.mp4')
                    if x==60:
                        api2.PostUpdate('@' + mention.user.screen_name +' asi asi', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='asiasi.mp4')
                    if x==61:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='cantico.mp4')
                    if x==62:
                        api2.PostUpdate('@' + mention.user.screen_name +' membrillo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='membrillo.mp4')
                    if x==63:
                        api2.PostUpdate('@' + mention.user.screen_name +' QUEEEEE', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='quee.mp4')
                    if x==64:
                        api2.PostUpdate('@' + mention.user.screen_name +' jajaja', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='risa.mp4')
                    if x==65:
                        api2.PostUpdate('@' + mention.user.screen_name +' ya vale no?', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='yavale.mp4')
                    if x==66:
                        api2.PostUpdate('@' + mention.user.screen_name +' sisisisi', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='sisi3.mp4')
                    if x==67:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='armadura.mp4')
                    if x==68:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='barres.mp4')
                    if x==69:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='cagon.mp4')
                    if x==70:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='encuentra.mp4')
                    if x==71:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='siguiente.mp4')
                    if x==72:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='sorbos.mp4')
                    if x==73:
                        api2.PostUpdate('@' + mention.user.screen_name +' mira mi pinga', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='trapo.mp4')
                    if x==74:
                        api2.PostUpdate('@' + mention.user.screen_name +' eres tonto', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='tonto2.mp4')
                    if x==75:
                        api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='tonto3.mp4')
                if status==False:
                    #api2.PostUpdate('@' + mention.user.screen_name +' las menciones solo funcionan con seguidores.', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True')
                    api.create_favorite(mention.id)
            except tweepy.TweepError as e:
                print('Mensaje ya favorito.')
                
            repo = g.get_user().get_repo("MrJaggerBot")
            file = repo.get_contents("/mentions/last_seen_id.txt")
            repo.update_file(path=file.path, message="Update", content=str(last_seen_id), sha=file.sha)

def reply_to_jagger():
    #print('buscando ultimo tweet de MrJagger', flush=True)
    last_tweet = retrieve_last_seen_id(FILE_NAME2)
    tweet=api2.GetUserTimeline(screen_name='@MisterJagger_', count=1, include_rts=False, exclude_replies=True)
    for tweets in reversed(tweet):
        if last_tweet != tweets.id:
            last_tweet = tweets.id
            store_last_seen_id(last_tweet, FILE_NAME2)
            print('jagger ha subido tweet')
            print('respondiendo')
            
            try:
                api.create_favorite(tweets.id)
                #api.retweet(tweets.id)
                
                x=random.randint(1,75)
                if x==1:
                    api2.PostUpdate('@' + tweets.user.screen_name +' SISISISISI', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='sisi2.mp4')
                if x==2:
                    api2.PostUpdate('@' + tweets.user.screen_name +' NONONONO', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='nono.mp4')
                if x==3:
                    api2.PostUpdate('@' + tweets.user.screen_name +' JAJSJS SISISI', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='sisi.mp4')
                if x==4:
                    api2.PostUpdate('@' + tweets.user.screen_name +' QUE TE CALLES', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='calles.mp4')
                if x==5:
                    api2.PostUpdate('@' + tweets.user.screen_name +' CALLATE', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='callate.mp4')
                if x==6:
                    api2.PostUpdate('@' + tweets.user.screen_name +' huevo :)', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='huevo.mp4')
                if x==7:
                    api2.PostUpdate('@' + tweets.user.screen_name +' eres asqueros@', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='asqueroso.mp4')
                if x==8:
                    api2.PostUpdate('@' + tweets.user.screen_name +' toma un platano ;)', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='platano.mp4')
                if x==9:
                    api2.PostUpdate('@' + tweets.user.screen_name +' A', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='A.mp4')
                if x==10:
                    api2.PostUpdate('@' + tweets.user.screen_name +' ;)', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='beso.mp4')
                if x==11:
                    api2.PostUpdate('@' + tweets.user.screen_name +' no, no es lo mismo', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='pizza.mp4')
                if x==12:
                    api2.PostUpdate('@' + tweets.user.screen_name +' eres lindisim@', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='chupa.mp4')
                if x==13:
                    api2.PostUpdate('@' + tweets.user.screen_name +' me gusta la menta :)', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='menta.mp4')
                if x==14:
                    api2.PostUpdate('@' + tweets.user.screen_name +' guap@s ;)', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='guapo.mp4')
                if x==15:
                    api2.PostUpdate('@' + tweets.user.screen_name +' un saludo', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='saludo.mp4')
                if x==16:
                    api2.PostUpdate('@' + tweets.user.screen_name +' te dedico este baile', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='baile.mp4')
                if x==17:
                    api2.PostUpdate('@' + tweets.user.screen_name +' fuera tont@', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='grita.mp4')
                if x==18:
                    api2.PostUpdate('@' + tweets.user.screen_name +' AAAAA', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ira.mp4')
                if x==19:
                    api2.PostUpdate('@' + tweets.user.screen_name +' te estaba preguntando', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='pregunta.mp4')
                if x==20:
                    api2.PostUpdate('@' + tweets.user.screen_name +' ERES UNA PESADILLA', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='pesadilla.mp4')
                if x==21:
                    api2.PostUpdate('@' + tweets.user.screen_name +' eres tu', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='mierda.mp4')
                if x==22:
                    api2.PostUpdate('@' + tweets.user.screen_name +' ven aqui', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='azote.mp4')
                if x==23:
                    api2.PostUpdate('@' + tweets.user.screen_name +' que bueno soy', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='bueno.mp4')
                if x==24:
                    api2.PostUpdate('@' + tweets.user.screen_name +' callate', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='callate.mp4')
                if x==25:
                    api2.PostUpdate('@' + tweets.user.screen_name +' estoy fumadisimo', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='fumado.mp4')
                if x==26:
                    api2.PostUpdate('@' + tweets.user.screen_name +' eres tont@', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='tonto.mp4')
                if x==27:
                    api2.PostUpdate('@' + tweets.user.screen_name +' v a m o s', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='vamos.mp4')
                if x==28:
                    api2.PostUpdate('@' + tweets.user.screen_name +' ah ah ah', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ahah.mp4')
                if x==29:
                    api2.PostUpdate('@' + tweets.user.screen_name +' uva', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='uva.mp4')
                if x==30:
                    api2.PostUpdate('@' + tweets.user.screen_name +' no se ve el agua', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='agua.mp4')
                if x==31:
                    api2.PostUpdate('@' + tweets.user.screen_name +' te aplaudo', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='clap.mp4')
                if x==32:
                    api2.PostUpdate('@' + tweets.user.screen_name +' adios', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='adios.mp4')
                if x==33:
                    api2.PostUpdate('@' + tweets.user.screen_name +' que asco dais', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='asco.mp4')
                if x==34:
                    api2.PostUpdate('@' + tweets.user.screen_name +' gracias y feliz navidad', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='gracias.mp4')
                if x==35:
                    api2.PostUpdate('@' + tweets.user.screen_name +' no no tengo novia', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='novia.mp4')
                if x==36:
                    api2.PostUpdate('@' + tweets.user.screen_name +' ah', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='a2.mp4')
                if x==37:
                    api2.PostUpdate('@' + tweets.user.screen_name +' soy enorme', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='gigante.mp4')
                if x==38:
                    api2.PostUpdate('@' + tweets.user.screen_name +' amor para todos', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='corazon.mp4')
                if x==39:
                    api2.PostUpdate('@' + tweets.user.screen_name +' DESPIERTA', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='dias.mp4')
                if x==40:
                    api2.PostUpdate('@' + tweets.user.screen_name +' buenas noches princesa ;)', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='noches.mp4')
                if x==41:
                    api2.PostUpdate('@' + tweets.user.screen_name +' hoy es noche de sexo', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='noches2.mp4')
                if x==42:
                    api2.PostUpdate('@' + tweets.user.screen_name +' toma', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='baile2.mp4')
                if x==43:
                    api2.PostUpdate('@' + tweets.user.screen_name +' has entendido?', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='entendido.mp4')
                if x==44:
                    api2.PostUpdate('@' + tweets.user.screen_name +' feliz navidad', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='navidad.mp4')
                if x==45:
                    api2.PostUpdate('@' + tweets.user.screen_name +' asi asi', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='asi.mp4')
                if x==46:
                    api2.PostUpdate('@' + tweets.user.screen_name +' mi amor', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='amor.mp4')
                if x==47:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='cancion.mp4')
                if x==48:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='agradecido.mp4')
                if x==49:
                    api2.PostUpdate('@' + tweets.user.screen_name +' hola', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='hola.mp4')
                if x==50:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='gruñir.mp4')
                if x==51:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='callate2.mp4')
                if x==52:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='baile3.mp4')
                if x==53:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='vete.mp4')
                if x==54:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='que_tal.mp4')
                if x==55:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='amor2.mp4')
                if x==56:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='especifica.mp4')
                if x==57:
                    api2.PostUpdate('@' + tweets.user.screen_name +' pringao', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='pringao.mp4')
                if x==58:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='aaaa.mp4')
                if x==59:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='especifica.mp4')
                if x==60:
                    api2.PostUpdate('@' + tweets.user.screen_name +' asi asi', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='asiasi.mp4')
                if x==61:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='cantico.mp4')
                if x==62:
                    api2.PostUpdate('@' + tweets.user.screen_name +' membrillo', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='membrillo.mp4')
                if x==63:
                    api2.PostUpdate('@' + tweets.user.screen_name +' QUEEEEE', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='quee.mp4')
                if x==64:
                    api2.PostUpdate('@' + tweets.user.screen_name +' jajaja', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='risa.mp4')
                if x==65:
                    api2.PostUpdate('@' + tweets.user.screen_name +' ya vale no?', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='yavale.mp4')
                if x==66:
                    api2.PostUpdate('@' + tweets.user.screen_name +' sisisisi', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='sisi3.mp4')
                if x==67:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='armadura.mp4')
                if x==68:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='barres.mp4')
                if x==69:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='cagon.mp4')
                if x==70:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='encuentra.mp4')
                if x==71:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='siguiente.mp4')
                if x==72:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='sorbos.mp4')
                if x==73:
                    api2.PostUpdate('@' + tweets.user.screen_name +' mira mi pinga', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='trapo.mp4')
                if x==74:
                    api2.PostUpdate('@' + tweets.user.screen_name +' eres tonto', in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='tonto2.mp4')
                if x==75:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='tonto3.mp4')

                 
            except tweepy.TweepError as e:
                print('Mensaje ya favorito.')
            
            repo = g.get_user().get_repo("MrJaggerBot")
            file2 = repo.get_contents("/mentions/jagger.txt")

            repo.update_file(path=file2.path, message="Update", content=str(last_tweet), sha=file2.sha)
            
def reply_to_ibai():
    #print('buscando ultimo tweet de MrJagger', flush=True)
    last_tweet = retrieve_last_seen_id(FILE_NAME4)
    tweet=api2.GetUserTimeline(screen_name='@IbaiLlanos', count=1, include_rts=False, exclude_replies=True)
    for tweets in reversed(tweet):
        if last_tweet != tweets.id:
            last_tweet = tweets.id
            store_last_seen_id(last_tweet, FILE_NAME4)
            print('ibai ha subido tweet')
            print('respondiendo')
            
            try:
                api.create_favorite(tweets.id)
                #api.retweet(tweets.id)
                
                x=random.randint(1,9)
                if x==1:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai.jpeg')
                if x==2:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai2.jpg')
                if x==3:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai3.jpg')
                if x==4:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai4.jpg')
                if x==5:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai5.jpg')
                if x==6:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai6.jpg')
                if x==7:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai7.jpg')
                if x==8:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai8.jpg')
                if x==9:
                    api2.PostUpdate('@' + tweets.user.screen_name, in_reply_to_status_id= tweets.id, auto_populate_reply_metadata= 'True', media='ibai9.jpg')
                
            except tweepy.TweepError as e:
                print('Mensaje ya favorito.')
            
            repo = g.get_user().get_repo("MrJaggerBot")
            file2 = repo.get_contents("/mentions/ibai.txt")

            repo.update_file(path=file2.path, message="Update", content=str(last_tweet), sha=file2.sha)

def reply_to_ooc():
    #print('buscando ultimo tweet de OOC', flush=True)
    last_tweet2 = retrieve_last_seen_id(FILE_NAME3)
    tweet2=api2.GetUserTimeline(screen_name='@OOC_Jagger', count=1, include_rts=False, exclude_replies=True)
    for tweets2 in reversed(tweet2):
        if last_tweet2 != tweets2.id:
            last_tweet2 = tweets2.id
            store_last_seen_id(last_tweet2, FILE_NAME3)
            print('OOC ha subido tweet')
            print('respondiendo')
            
            try:
                api.create_favorite(tweets2.id)
                #api.retweet(tweets2.id)
                
                x=random.randint(1,75)
                if x==1:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' SISISISISI', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='sisi2.mp4')
                if x==2:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' NONONONO', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='nono.mp4')
                if x==3:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' JAJSJS SISISI', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='sisi.mp4')
                if x==4:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' QUE TE CALLES', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='calles.mp4')
                if x==5:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' CALLATE', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='callate.mp4')
                if x==6:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' huevo :)', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='huevo.mp4')
                if x==7:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' eres asqueros@', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='asqueroso.mp4')
                if x==8:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' toma un platano ;)', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='platano.mp4')
                if x==9:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' A', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='A.mp4')
                if x==10:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' ;)', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='beso.mp4')
                if x==11:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' no, no es lo mismo', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='pizza.mp4')
                if x==12:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' eres lindisim@', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='chupa.mp4')
                if x==13:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' me gusta la menta :)', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='menta.mp4')
                if x==14:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' guap@s ;)', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='guapo.mp4')
                if x==15:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' un saludo', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='saludo.mp4')
                if x==16:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' te dedico este baile', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='baile.mp4')
                if x==17:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' fuera tont@', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='grita.mp4')
                if x==18:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' AAAAA', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='ira.mp4')
                if x==19:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' te estaba preguntando', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='pregunta.mp4')
                if x==20:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' ERES UNA PESADILLA', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='pesadilla.mp4')
                if x==21:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' eres tu', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='mierda.mp4')
                if x==22:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' ven aqui', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='azote.mp4')
                if x==23:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' que bueno soy', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='bueno.mp4')
                if x==24:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' callate', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='callate.mp4')
                if x==25:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' estoy fumadisimo', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='fumado.mp4')
                if x==26:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' eres tont@', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='tonto.mp4')
                if x==27:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' v a m o s', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='vamos.mp4')
                if x==28:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' ah ah ah', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='ahah.mp4')
                if x==29:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' uva', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='uva.mp4')
                if x==30:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' no se ve el agua', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='agua.mp4')
                if x==31:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' te aplaudo', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='clap.mp4')
                if x==32:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' adios', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='adios.mp4')
                if x==33:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' que asco dais', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='asco.mp4')
                if x==34:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' gracias y feliz navidad', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='gracias.mp4')
                if x==35:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' no no tengo novia', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='novia.mp4')
                if x==36:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' ah', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='a2.mp4')
                if x==37:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' soy enorme', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='gigante.mp4')
                if x==38:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' amor para todos', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='corazon.mp4')
                if x==39:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' DESPIERTA', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='dias.mp4')
                if x==40:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' buenas noches princesa ;)', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='noches.mp4')
                if x==41:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' hoy es noche de sexo', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='noches2.mp4')
                if x==42:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' toma', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='baile2.mp4')
                if x==43:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' has entendido?', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='entendido.mp4')
                if x==44:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' feliz navidad', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='navidad.mp4')
                if x==45:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' asi asi', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='asi.mp4')
                if x==46:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' mi amor', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='amor.mp4')
                if x==47:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='cancion.mp4')
                if x==48:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='agradecido.mp4')
                if x==49:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' hola', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='hola.mp4')
                if x==50:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='gruñir.mp4')
                if x==51:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='callate2.mp4')
                if x==52:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='baile3.mp4')
                if x==53:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='vete.mp4')
                if x==54:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='que_tal.mp4')
                if x==55:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='amor2.mp4')
                if x==56:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='especifica.mp4')
                if x==57:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' pringao', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='pringao.mp4')
                if x==58:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='aaaa.mp4')
                if x==59:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='especifica.mp4')
                if x==60:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' asi asi', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='asiasi.mp4')
                if x==61:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='cantico.mp4')
                if x==62:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' membrillo', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='membrillo.mp4')
                if x==63:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' QUEEEEE', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='quee.mp4')
                if x==64:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' jajaja', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='risa.mp4')
                if x==65:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' ya vale no?', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='yavale.mp4')
                if x==66:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' sisisisi', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='sisi3.mp4')
                if x==67:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='armadura.mp4')
                if x==68:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='barres.mp4')
                if x==69:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='cagon.mp4')
                if x==70:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='encuentra.mp4')
                if x==71:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='siguiente.mp4')
                if x==72:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='sorbos.mp4')
                if x==73:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' mira mi pinga', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='trapo.mp4')
                if x==74:
                    api2.PostUpdate('@' + tweets2.user.screen_name +' eres tonto', in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='tonto2.mp4')
                if x==75:
                    api2.PostUpdate('@' + tweets2.user.screen_name, in_reply_to_status_id= tweets2.id, auto_populate_reply_metadata= 'True', media='tonto3.mp4')

                 
            except tweepy.TweepError or twitter.TwitterError as e:
                print('Mensaje ya favorito.')
            
            repo = g.get_user().get_repo("MrJaggerBot")
            file3 = repo.get_contents("/mentions/ooc.txt")

            repo.update_file(path=file3.path, message="Update", content=str(last_tweet2), sha=file3.sha)            
            
while True:
    reply_to_tweets()
    reply_to_jagger()
    reply_to_ibai()
    time.sleep(20)
