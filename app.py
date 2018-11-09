from flask import Flask
import paho.mqtt.client as paho
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:
        print("Connection failed")

Connected = False   #global variable for the state of the connection

app = Flask(__name__)

broker_address = "m15.cloudmqtt.com"
port = 16735
user = "bawbwoee"
password = "fNQwDsCtKigz"
client = paho.Client("echo-api")
topic = 'Alice'

client.username_pw_set(user, password=password)
client.on_connect= on_connect
client.connect(broker_address, port=port)

client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)

@app.route("/<route_var>", methods=['GET'])
def update(route_var):
    client.publish(topic,route_var)
    return route_var

if __name__=='__main__':
    app.run(debug=True)
