from flask import Flask, render_template
import random
import urllib.request
import requests
import threading
import json

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1363480/feeds.json?api_key='
    KEY='60UWZTDQ0TC3G8PX'
    HEADER='&results=1'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)
    data_link=urllib.request.urlopen(NEW_URL)
    get_data=requests.get(NEW_URL).json()

    
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    print(feild_1)
    #return [feild_1['field1'],feild_1['field2']]
    t=[]
    for x in feild_1:
        #print(x['field1'])
        t.append(x['field1'])
        t.append(x['field1'])
    return t
    
        
app = Flask('testapp')

@app.route('/')
def index():
#    return render_template('index.html', variable='12345')
    [s1,s2]=read_data_thingspeak()
    return render_template('index.html', status1=str(s1), status2=str(s2), status3=str(random.randint(1,30)), status4=str(random.randint(1,30)))

if __name__ == '__main__':
    app.run()
    
    
