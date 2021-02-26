import tweepy
import twitter
import time
import random
from datetime import datetime
import sys
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
CONSUMER_KEY = 'o7lssun3q62CQbAT57m4inwv1'
CONSUMER_SECRET = 'i80Jb9lfUgZT3I7JwzzXyjQ9TjSJtV71Z9nUnWrZ7cjZ2Stt7q'
ACCESS_KEY = '1356760524290162691-miBvmfKQkQOMO5PNwYKD3oyB3nS7CM'
ACCESS_SECRET = 'EoMcJWD0WCo9RKHesORK9QcbkDJppv8OL7HKshHRvQmfF'

api2 = twitter.Api(consumer_key='o7lssun3q62CQbAT57m4inwv1',
                  consumer_secret='i80Jb9lfUgZT3I7JwzzXyjQ9TjSJtV71Z9nUnWrZ7cjZ2Stt7q',
                  access_token_key='1356760524290162691-miBvmfKQkQOMO5PNwYKD3oyB3nS7CM',
                  access_token_secret='EoMcJWD0WCo9RKHesORK9QcbkDJppv8OL7HKshHRvQmfF')



# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen_id.txt'


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
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '@mrjaggerbot' in mention.full_text.lower():
            print('found', flush=True)
            print('responding back...', flush=True)

            x=random.randint(1,50)
            if x==1:
                api2.PostUpdate('@' + mention.user.screen_name +' SISISISISI', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/sisi2.mp4')
            if x==2:
                api2.PostUpdate('@' + mention.user.screen_name +' NONONONO', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/nono.mp4')
            if x==3:
                api2.PostUpdate('@' + mention.user.screen_name +' JAJSJS SISISI', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/sisi.mp4')
            if x==4:
                api2.PostUpdate('@' + mention.user.screen_name +' QUE TE CALLES', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/calles.mp4')
            if x==5:
                api2.PostUpdate('@' + mention.user.screen_name +' CALLATE', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/callate.mp4')
            if x==6:
                api2.PostUpdate('@' + mention.user.screen_name +' huevo :)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/huevo.mp4')
            if x==7:
                api2.PostUpdate('@' + mention.user.screen_name +' eres asqueros@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/asqueroso.mp4')
            if x==8:
                api2.PostUpdate('@' + mention.user.screen_name +' toma un platano ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/platano.mp4')
            if x==9:
                api2.PostUpdate('@' + mention.user.screen_name +' A', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/A.mp4')
            if x==10:
                api2.PostUpdate('@' + mention.user.screen_name +' ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/beso.mp4')
            if x==11:
                api2.PostUpdate('@' + mention.user.screen_name +' no, no es lo mismo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/pizza.mp4')
            if x==12:
                api2.PostUpdate('@' + mention.user.screen_name +' eres lindisim@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/chupa.mp4')
            if x==13:
                api2.PostUpdate('@' + mention.user.screen_name +' me gusta la menta :)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/menta.mp4')
            if x==14:
                api2.PostUpdate('@' + mention.user.screen_name +' guap@s ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/guapo.mp4')
            if x==15:
                api2.PostUpdate('@' + mention.user.screen_name +' un saludo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/saludo.mp4')
            if x==16:
                api2.PostUpdate('@' + mention.user.screen_name +' te dedico este baile', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/baile.mp4')
            if x==17:
                api2.PostUpdate('@' + mention.user.screen_name +' fuera tont@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/grita.mp4')
            if x==18:
                api2.PostUpdate('@' + mention.user.screen_name +' AAAAA', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/ira.mp4')
            if x==19:
                api2.PostUpdate('@' + mention.user.screen_name +' te estaba preguntando', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/pregunta.mp4')
            if x==20:
                api2.PostUpdate('@' + mention.user.screen_name +' ERES UNA PESADILLA', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/pesadilla.mp4')
            if x==21:
                api2.PostUpdate('@' + mention.user.screen_name +' eres tu', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/mierda.mp4')
            if x==22:
                api2.PostUpdate('@' + mention.user.screen_name +' ven aqui', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/azote.mp4')
            if x==23:
                api2.PostUpdate('@' + mention.user.screen_name +' que bueno soy', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/bueno.mp4')
            if x==24:
                api2.PostUpdate('@' + mention.user.screen_name +' callate', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/callate.mp4')
            if x==25:
                api2.PostUpdate('@' + mention.user.screen_name +' estoy fumadisimo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/fumado.mp4')
            if x==26:
                api2.PostUpdate('@' + mention.user.screen_name +' eres tont@', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/tonto.mp4')
            if x==27:
                api2.PostUpdate('@' + mention.user.screen_name +' v a m o s', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/vamos.mp4')
            if x==28:
                api2.PostUpdate('@' + mention.user.screen_name +' ah ah ah', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/ahah.mp4')
            if x==29:
                api2.PostUpdate('@' + mention.user.screen_name +' uva', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/uva.mp4')
            if x==30:
                api2.PostUpdate('@' + mention.user.screen_name +' no se ve el agua', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/agua.mp4')
            if x==31:
                api2.PostUpdate('@' + mention.user.screen_name +' te aplaudo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/clap.mp4')
            if x==32:
                api2.PostUpdate('@' + mention.user.screen_name +' adios', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/adios.mp4')
            if x==33:
                api2.PostUpdate('@' + mention.user.screen_name +' que asco dais', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/asco.mp4')
            if x==34:
                api2.PostUpdate('@' + mention.user.screen_name +' gracias y feliz navidad', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/gracias.mp4')
            if x==35:
                api2.PostUpdate('@' + mention.user.screen_name +' no no tengo novia', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/novia.mp4')
            if x==36:
                api2.PostUpdate('@' + mention.user.screen_name +' ah', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/a2.mp4')
            if x==37:
                api2.PostUpdate('@' + mention.user.screen_name +' soy enorme', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/gigante.mp4')
            if x==38:
                api2.PostUpdate('@' + mention.user.screen_name +' amor para todos', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/corazon.mp4')
            if x==39:
                api2.PostUpdate('@' + mention.user.screen_name +' DESPIERTA', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/dias.mp4')
            if x==40:
                api2.PostUpdate('@' + mention.user.screen_name +' buenas noches princesa ;)', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/noches.mp4')
            if x==41:
                api2.PostUpdate('@' + mention.user.screen_name +' hoy es noche de sexo', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/noches2.mp4')
            if x==42:
                api2.PostUpdate('@' + mention.user.screen_name +' toma', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/baile2.mp4')
            if x==43:
                api2.PostUpdate('@' + mention.user.screen_name +' has entendido?', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/entendido.mp4')
            if x==44:
                api2.PostUpdate('@' + mention.user.screen_name +' feliz navidad', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/navidad.mp4')
            if x==45:
                api2.PostUpdate('@' + mention.user.screen_name +' asi asi', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/asi.mp4')
            if x==46:
                api2.PostUpdate('@' + mention.user.screen_name +' mi amor', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/amor.mp4')
            if x==47:
                api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/cancion.mp4')
            if x==48:
                api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/agradecido.mp4')
            if x==49:
                api2.PostUpdate('@' + mention.user.screen_name +' hola', in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/hola.mp4')
            if x==50:
                api2.PostUpdate('@' + mention.user.screen_name, in_reply_to_status_id= mention.id, auto_populate_reply_metadata= 'True', media='MrJaggerBot/mentions/gruñir.mp4')

            try:
                api.create_favorite(mention.id)
            except tweepy.TweepError as e:
                print(e)

            hora = datetime.now().hour
            minutes = datetime.now().minute
            if hora == 20 and minutes == 27:
                sys.exit()

while True:
    reply_to_tweets()
    time.sleep(20)
