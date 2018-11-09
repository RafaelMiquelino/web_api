from flask import Flask
import paho.mqtt.client as paho
import time
import os

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:
        print("Connection failed")

Connected = False   #global variable for the state of the connection

broker_address = os.environ['BRK_ADD']
port = int(os.environ['BRK_PORT'])
user = os.environ['BRK_USER']
password = os.environ['BRK_PWD']
client = paho.Client(os.environ['BRK_CLIENT'])
topic = os.environ['BRK_TOPIC']

client.username_pw_set(user, password=password)
client.on_connect= on_connect
client.connect(broker_address, port=port)

client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)

app = Flask(__name__)

@app.route("/<route_var>", methods=['GET'])
def update(route_var):
    client.publish(topic,route_var)
    return route_var

if __name__=='__main__':
    app.run(debug=True)
