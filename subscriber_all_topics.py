import paho.mqtt.client as paho
from datetime import datetime


def on_subscribe(client, userdata, mid, granted_qos):
    #print("Subscribed: "+str(mid)+" "+str(granted_qos))
    global f
    f.write("\nSubscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    global f
    f.write("\n"+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

now = datetime.now()
dt_string = now.strftime("%H_%M_%S")
f = open("logfile_"+dt_string+".txt", "w")

host_ip="192.168.0.29"
this_client_id = "Subscriber-1"

client = paho.Client(client_id=this_client_id, clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.will_set("my/lastwill", this_client_id+ " Gone Offline",qos=1,retain=False)

client.connect(host=host_ip, port=1883)
client.subscribe("my/topic_1", qos=1)
client.subscribe("my/topic_2", qos=1)
client.subscribe("my/topic_3", qos=1)

client.loop_forever()

f.close()
