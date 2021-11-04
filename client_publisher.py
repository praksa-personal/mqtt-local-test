import paho.mqtt.client as paho
import time
import json


def on_publish(client, userdata, mid):
    #print("msg.id: "+str(mid))
    ()
 
host_ip="192.168.0.29"
this_client_id = "Publisher-Marko"


client = paho.Client(client_id=this_client_id, userdata=None, protocol=paho.MQTTv31)
client.on_publish = on_publish
client.will_set("my/lastwill", this_client_id+ " Gone Offline",qos=1,retain=False)

client.connect(host=host_ip, port=1883)
client.loop_start()

while True:
    print("Enter topic name you want to publish to:")
    topic = input()
    print("Enter message:")
    msg = input()
    (rc, mid) = client.publish(topic, str(msg), qos=1)


